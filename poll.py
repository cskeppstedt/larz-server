from itertools import groupby
from transform import to_player, to_player_stats
import helpers
import re
import requests
import sys
import time


def log(message):
    print "  [ poll ]  ", message


def log_url(url, failed=False):
    if failed is True:
        log("  (ERR)  " + url)
    else:
        log("  (OK ) " + url)


class Poll:
    # =====================================================
    #  Public API
    # =====================================================
    def match_tokens(self, list_of_userid):
        return self.fetch_matches(list_of_userid)

    def matches(self, list_of_token):
        log("fetching data for %d match ids" % len(list_of_token))
        data = self.fetch_match_data(list_of_token)

        if data is None:
            return []

        log("converting %d objects to match_models" % len(data))
        models = self.to_match_models(list_of_token, data)

        return list(models)

    def player_stats(self, list_of_userid):
        log("fetching player_stats for %d users" % len(list_of_userid))
        data = self.fetch_player_stats(list_of_userid)
        models = self.to_player_stats_models(data)

        return models

    # =====================================================
    #  Private API
    # =====================================================
    def fetch_matches(self, list_of_userid):
        matches = {}
        expr = re.compile("([0-9]+)\|(?:[^\|]+)\|(\d{2})\/(\d{2})\/(\d{4}),?")

        for userid in list_of_userid:
            url = helpers.match_history_uri(userid)
            log("fetching match_history for " + userid)
            try:
                response = requests.get(url)
                try:
                    json = response.json()
                    log_url(url)
                    for m in expr.finditer(json[0]["history"]):
                        (match_id, mm, dd, yyyy) = m.groups()
                        matches[match_id] = '%s-%s-%s' % (yyyy, mm, dd)
                except ValueError:
                    log_url(url, True)
                    log('  %s: %s' % (str(response.status_code),
                                      response.text))
            except IOError as e:
                log_url(url, True)
                log("I/O error({0}): {1}".format(e.errno, e.strerror))
                raise
            except Exception:
                log_url(url, True)
                log("unexpected error: " + str(sys.exc_info()[0]))
                raise

        unique_list = [(m, d) for m, d in matches.iteritems()]
        sorted_list = sorted(unique_list,
                             key=lambda (m, d): (d, m), reverse=True)

        return sorted_list[:10]

    def fetch_match_data(self, list_of_match):
        match_ids_slug = "+".join([x[0] for x in list_of_match])

        url = helpers.multi_match_uri(match_ids_slug)
        log("fetching match data from " + url)
        log("dates: %s" % ", ".join(x[1] for x in list_of_match))
        try:
            response = requests.get(url)

            try:
                data = response.json()
                log_url(url)
                return data
            except ValueError:
                log_url(url, True)
                log('  %s: %s' % (str(response.status_code), response.text))
                return None
        except IOError as e:
            log_url(url)
            log("I/O error({0}): {1}".format(e.errno, e.strerror))
            return None
        except Exception:
            log_url(url, True)
            log("unexpected error: " + str(sys.exc_info()[0]))
            return None

    def fetch_player_stats(self, list_of_userid):
        stats = []

        for userid in list_of_userid:
            url = helpers.player_stats_uri(userid)
            log("fetching player_stats for " + userid)
            try:
                response = requests.get(url)
                try:
                    json = response.json()
                    log_url(url)
                    stats.append(json)
                except ValueError:
                    log_url(url, True)
                    log('  %s: %s' % (str(response.status_code),
                                      response.text))
            except IOError as e:
                log_url(url, True)
                log("I/O error({0}): {1}".format(e.errno, e.strerror))
                raise
            except Exception:
                log_url(url, True)
                log("unexpected error: " + str(sys.exc_info()[0]))
                raise

        return stats

    def to_player_stats_models(self, list_of_stats):
        models = map(to_player_stats, list_of_stats)
        return {
            'date': time.strftime("%Y-%m-%d"),
            'data': {m['nickname']: m for m in models}
        }

    def to_match_models(self, list_of_match, list_of_data):
        lookup = dict(list_of_match)
        for match_id, data in groupby(list_of_data, lambda m: m['match_id']):
            date = lookup[match_id]
            yield self.to_match_model(match_id, date, list(data))

    def to_match_model(self, match_id, date, list_of_match):
        match = {
            'match_id': match_id,
            'date': date,
            'team1': map(to_player,
                         [p for p in list_of_match if p['team'] == '1']),
            'team2': map(to_player,
                         [p for p in list_of_match if p['team'] == '2'])
        }

        for p in list_of_match:
            if p['wins'] == '1':
                match['winning_team'] = p['team']
                break

        return match
