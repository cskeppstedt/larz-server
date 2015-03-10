import requests
import vars
import helpers
import re
import sys
from itertools import groupby


class Poll:
    # =====================================================
    #  Public API
    # =====================================================
    def matches(self, list_of_userid):
        print " - fetching match ids"
        matches = self.fetch_matches(list_of_userid)

        print " - fetching data for {} unique match ids".format(len(matches))
        data = self.fetch_match_data(matches)
        
        print " - converting {} objects to match_models".format(len(data))
        models = self.to_match_models(matches, data)

        return list(models)


    # =====================================================
    #  Private API
    # =====================================================
    def fetch_matches(self, list_of_userid):
        matches = {}
        expr = re.compile("([0-9]+)\|(?:[^\|]+)\|(\d{2})\/(\d{2})\/(\d{4}),?")

        for userid in list_of_userid:
            url = helpers.match_history_uri(userid)
            print " - fetching match_history for " + userid
            response = requests.get(url).json()
            for m in expr.finditer(response[0]["history"]):
                (match_id, mm, dd, yyyy) = m.groups()
                matches[match_id] = '%s-%s-%s' % (yyyy,mm,dd)
            
        unique_list = [(m, d) for m, d in matches.iteritems()]
        sorted_list = sorted(unique_list, key = lambda (m, d): (d, m), reverse=True)
        
        return sorted_list[:10]


    def fetch_match_data(self, list_of_match):
        match_ids_slug = "+".join([x[0] for x in list_of_match])

        url = helpers.multi_match_uri(match_ids_slug)
        print " - fetching match data from " + url
        print " - dates: {}".format(", ".join(x[1] for x in list_of_match))
        try:
            return requests.get(url).json()
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            raise
        except Exception:
            print "Unexpected error:", sys.exc_info()[0]
            raise


    def to_match_models(self, list_of_match, list_of_data):
        lookup = dict(list_of_match)
        for match_id, data in groupby(list_of_data, lambda m: m['match_id']):
            date = lookup[match_id]
            yield self.to_match_model(match_id, date, list(data))


    def to_match_model(self, match_id, date, list_of_match):
        match = {
            'match_id': match_id,
            'date': date,
            'team1': map(self.to_player, [p for p in list_of_match if p['team'] == '1']),
            'team2': map(self.to_player, [p for p in list_of_match if p['team'] == '2'])
        }

        for p in list_of_match:
            if p['wins'] == '1':
                match['winning_team'] = p['team']
                break

        return match


    def to_player(self, data):
        keys = ['deaths', 'herokills', 'level', 'hero_id', 'nickname', 'heroassists']
        return { k: data[k] for k in keys }

