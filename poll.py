import requests
import vars
import helpers
import re


class Poll:
    def matches(self, list_of_userid):
        last_response = None
        id_set = set([])
        expr = re.compile("([0-9]+)\|[^,]*")

        for userid in list_of_userid:
            url = helpers.match_history_uri(userid)
            response = requests.get(url).json()
            for match_id in expr.findall(response[0]["history"]):
                id_set.add(match_id)
            
        match_ids = list(id_set)
        match_ids.sort()

        match_ids_slug = "+".join(match_ids)
        url = helpers.multi_match_uri(match_ids_slug)
        response = requests.get(url).json()
        
