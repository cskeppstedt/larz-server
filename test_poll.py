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
def return_matches(list_of_userid):
    match_ids_slug = "136020720+136021420+136023435+136026090+136028023+136095625+136097421+136198877+136199362+136199918+136200860"

    httpretty.enable()
    add_fixtures(list_of_userid, helpers.match_history_uri)
    add_fixtures([match_ids_slug], helpers.multi_match_uri) 

    instance = Poll()
    result = instance.matches(list_of_userid)
    expected = [
        { 'match_id':'136020720', 'team1': [{'nickname': u'DB_Killer'}, {'nickname': u'Thumping'}, {'nickname': u'One_of_Few'}, {'nickname': u'm0zak'}, {'nickname': u'Counsellor'}], 'team1': [{'nickname': u'deimi'}, {'nickname': u'Schln'}, {'nickname': u'skepparn_'}, {'nickname': u'dolanduck101'}, {'nickname': u'__I1I__'}] }
#        { 'match_id':'136021420' },
#        { 'match_id':'136023435' },
#        { 'match_id':'136026090' },
#        { 'match_id':'136028023' },
#        { 'match_id':'136095625' },
#        { 'match_id':'136097421' },
#        { 'match_id':'136198877' },
#        { 'match_id':'136199362' },
#        { 'match_id':'136199918' },
#        { 'match_id':'136200860' }
    ]

    assert result[0]['match_id'] == expected[0]['match_id']
    teardown()


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
