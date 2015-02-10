import vars
import re


# reads the content of a fixture json file, the
# path is based on the uri (see below)
def fixture_for(uri):
    relative_path = "./fixtures/{}response.json".format(uri_to_path(uri))
    with open(relative_path, 'r') as content_file:
        content = content_file.read()
        return content

# convert an API uri to a relative path e.g:
# in:  api.heroesofnewerth.com/match_history/ranked/nickname/abc/?token=xyz
# out: match_history/ranked/nickname/abc/
def uri_to_path(uri):
    expr = re.compile("{}\/([^?]+)".format(vars.API_BASE_URL))
    match = expr.match(uri)
    return match.group(1)

def match_history_uri(userid):
    return "{}/match_history/ranked/nickname/{}/?token={}".format(vars.API_BASE_URL, userid, vars.API_TOKEN)

def multi_match_uri(match_ids_slug):
    return "{}/multi_match/statistics/matchids/{}/?token={}".format(vars.API_BASE_URL, match_ids_slug, vars.API_TOKEN)

