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
        ids  = self.fetch_match_ids(list_of_userid)
        data = self.fetch_match_data(ids)
        models = self.to_match_models(data)

        return list(models)


    # =====================================================
    #  Private API
    # =====================================================
    def fetch_match_ids(self, list_of_userid):
        id_set = set([])
        expr = re.compile("([0-9]+)\|[^,]*")

        for userid in list_of_userid:
            url = helpers.match_history_uri(userid)
            response = requests.get(url).json()
            for match_id in expr.findall(response[0]["history"]):
                id_set.add(match_id)
            
        match_ids = list(id_set)
        match_ids.sort()

        return match_ids


    def fetch_match_data(self, list_of_matchid):
        match_ids_slug = "+".join(list_of_matchid)

        url = helpers.multi_match_uri(match_ids_slug)
        return requests.get(url).json()


    def to_match_models(self, list_of_match):
        for match_id, data in groupby(list_of_match, lambda m: m['match_id']):
            yield self.to_match_model(match_id, list(data))


    def to_match_model(self, match_id, list_of_match):
        return {
            'match_id': match_id,
            'team1': map(self.to_player, [p for p in list_of_match if p['team'] == '1']),
            'team2': map(self.to_player, [p for p in list_of_match if p['team'] == '2'])
        }


    def to_player(self, data):
        return {
            'nickname': data['nickname']
        }
