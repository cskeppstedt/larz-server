from pytest_bdd import scenario, given, when, then
from poll import Poll
import httpretty
import re
import requests
import vars


@scenario('poll.feature', 'Polling matches')
def test_polling_matches():
    pass

@given('a list of userid')
def list_of_userid():
    return ['1','2']

@then('it should pull matches for each userid')
def pull_foreach_userid(list_of_userid):
    body = '{"asd": "foo"}'
    req_urls = []

    def make_url(userid): return "{}/match_history/ranked/nickname/{}/?token={}".format(vars.API_BASE_URL, userid, vars.API_TOKEN)
    expected_urls = map(make_url, list_of_userid)
    
    def cb(req, uri, headers):
        req_urls.append(uri)
        return (200, headers, body)
    
    httpretty.enable()
    httpretty.register_uri(httpretty.GET, re.compile("(.*)"),
                           body=cb,
                           content_type="application/json")

    instance = Poll()
    result = instance.matches(list_of_userid)

    assert result == {'asd': 'foo'}
    assert req_urls == expected_urls

    httpretty.disable()
    httpretty.reset()

@then('it should pull stats for the 10 latest, unique matches')
def pull_matches(list_of_userid):
    pass

@then('it should return the matches')
def no_duplicate_matches(list_of_userid):
    pass

