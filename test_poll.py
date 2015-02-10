from pytest_bdd import scenario, given, when, then
from poll import Poll
import httpretty
import re
import requests
import vars
import helpers


@scenario('poll.feature', 'Polling matches')
def test_polling_matches():
    pass


@given('a list of userid')
def list_of_userid():
    return ['1','2']


@then('it should pull matches for each userid')
def pull_foreach_userid(list_of_userid):
    req_urls = []
    expected_urls = map(helpers.match_history_uri, list_of_userid)

    httpretty.enable()
    add_fixtures(list_of_userid, helpers.match_history_uri, lambda _, uri, __: req_urls.append(uri))

    instance = Poll()
    result = instance.matches(list_of_userid)

    assert req_urls[:-1] == expected_urls
    teardown()


@then('it should pull stats for the 10 latest, unique matches')
def pull_matches(list_of_userid):
    match_ids_slug = "136020720+136021420+136023435+136026090+136028023+136095625+136097421+136198877+136199362+136199918+136200860"
    req_urls = []
    expected_url = helpers.multi_match_uri(match_ids_slug)

    httpretty.enable()
    add_fixtures(list_of_userid, helpers.match_history_uri, lambda _, uri, __: req_urls.append(uri))
    add_fixtures([match_ids_slug], helpers.multi_match_uri, lambda _, uri, __: req_urls.append(uri)) 

    instance = Poll()
    result = instance.matches(list_of_userid)

    assert req_urls[-1] == expected_url
    teardown()


@then('it should return the matches')
def no_duplicate_matches(list_of_userid):
    pass


# --- helpers ---

def add_fixtures(list_of_id, uri_fn, response_cb=None):
    expected_urls = map(uri_fn, list_of_id)
    
    def cb(req, uri, headers):
        if response_cb != None: response_cb(req, uri, headers)
        body = helpers.fixture_for(uri)
        return (200, headers, body)
    
    httpretty.register_uri(httpretty.GET,
                           re.compile("(.*)"),
                           body=cb,
                           content_type="application/json")

def teardown():
    httpretty.disable()
    httpretty.reset()
