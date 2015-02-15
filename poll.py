import requests
import vars
import helpers
import re
from itertools import groupby


class Poll:
    # =====================================================
    #  Public API
    # =====================================================
    def matches(self, list_of_userid):
        print " - fetching match ids"
        ids  = self.fetch_match_ids(list_of_userid)

        print " - fetching data for {} unique match ids".format(len(ids))
        data = self.fetch_match_data(ids)
        
        print " - converting {} objects to match_models".format(len(data))
        models = self.to_match_models(data)

        return list(models)


    # =====================================================
    #  Private API
    # =====================================================
    def fetch_match_ids(self, list_of_userid):
        id_set = set([])
        id_list = []
        expr = re.compile("([0-9]+)\|[^,]*")

        for userid in list_of_userid:
            url = helpers.match_history_uri(userid)
            print " - fetching match_history for " + userid
            response = requests.get(url).json()
            for match_id in expr.findall(response[0]["history"]):
                if match_id not in id_set:
                    id_list.append(match_id)
            
        return id_list[-10:]


    def fetch_match_data(self, list_of_matchid):
        match_ids_slug = "+".join(list_of_matchid)

        url = helpers.multi_match_uri(match_ids_slug)
        print " - fetching match data from " + url
        try:
            return requests.get(url).json()
        except:
            return []


    def to_match_models(self, list_of_match):
        for match_id, data in groupby(list_of_match, lambda m: m['match_id']):
            yield self.to_match_model(match_id, list(data))


    def to_match_model(self, match_id, list_of_match):
        match = {
            'match_id': match_id,
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

