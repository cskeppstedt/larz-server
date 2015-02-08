import requests
import vars


class Poll:
    def matches(self, list_of_userid):
        last_response = None

        for userid in list_of_userid:
            url = "{}/match_history/ranked/nickname/{}/?token={}".format(vars.API_BASE_URL, userid, vars.API_TOKEN)
            last_response = requests.get(url)
        
        return last_response.json()
