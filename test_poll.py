from pytest_bdd import scenario, given, when, then
from poll import Poll
import json
import httpretty
import re
import requests
import vars
import helpers
import time


# --- polling match tokens ---


@scenario('poll.feature', 'Polling match tokens')
def test_polling_match_tokens():
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

    result = Poll().match_tokens(list_of_userid)

    assert req_urls == expected_urls
    teardown()


@then('it should return the match tokens')
def return_tokens(list_of_userid):
    httpretty.enable()
    add_fixtures(list_of_userid, helpers.match_history_uri)

    result = Poll().match_tokens(list_of_userid)
    expected_tokens = [
        (u'136200860', u'2015-02-07'),
        (u'136199918', u'2015-02-07'),
        (u'136199362', u'2015-02-07'),
        (u'136198877', u'2015-02-07'),
        (u'136097421', u'2015-02-03'),
        (u'136095625', u'2015-02-03'),
        (u'136028023', u'2015-02-01'),
        (u'136026090', u'2015-02-01'),
        (u'136020720', u'2015-02-01'),
        (u'136023435', u'2015-01-01')
    ]

    assert result == expected_tokens
    teardown()


# --- polling matches ---

@scenario('poll.feature', 'Polling matches')
def test_polling_matches():
    pass


@given('a list of match tokens')
def list_of_token():
    return [
        ('136200860', '2015-03-15'),
        ('136199918', '2015-04-15')
    ]


@then('it should pull the matches')
def pull_matches(list_of_token):
    match_ids_slug = "136200860+136199918"
    req_urls = []
    expected_url = helpers.multi_match_uri(match_ids_slug)

    httpretty.enable()
    add_fixtures([match_ids_slug], helpers.multi_match_uri, lambda _, uri, __: req_urls.append(uri)) 

    result = Poll().matches(list_of_token)
    matches_url = req_urls[0]

    assert matches_url == expected_url
    teardown()


@then('it should return the match data')
def return_matches(list_of_token):
    match_ids_slug = "136200860+136199918"

    httpretty.enable()
    add_fixtures([match_ids_slug], helpers.multi_match_uri) 

    result = Poll().matches(list_of_token)
    first  = result[0]
    assert first['date'] == '2015-04-15'
    teardown()


# --- polling matches ---

@scenario('poll.feature', 'Polling player stats')
def test_polling_player_stats():
    pass


@then('it should pull player stats for each userid')
def poll_player_stats(list_of_userid):
    req_urls = []
    expected_urls = map(helpers.player_stats_uri, list_of_userid)

    httpretty.enable()
    add_fixtures(list_of_userid, helpers.player_stats_uri, lambda _, uri, __: req_urls.append(uri))

    result = Poll().player_stats(list_of_userid)

    assert req_urls == expected_urls
    teardown()


@then('it should return the player stats')
def return_player_stats(list_of_userid):
    expected_urls = map(helpers.player_stats_uri, list_of_userid)

    httpretty.enable()
    add_fixtures(list_of_userid, helpers.player_stats_uri)

    result = Poll().player_stats(list_of_userid)

    today = time.strftime("%Y-%m-%d")

    assert result[0]['date'] == today
    assert result[0]['data'] == {
        'nickname': 'Schln',
        'mmr': '1574.691', 
        'games_played': '1843',
        'wins': '914',
        'losses': '929',
        'concedes': '851',
        'concedevotes': '174',
        'buybacks': '66',
        'wards': '8138',
        'bloodlust': '158',
        'doublekill': '523',
        'triplekill': '45',
        'quadkill': '3',
        'annihilation': '0',
        'ks3': '512',
        'ks4': '237',
        'ks5': '135',
        'ks6': '68',
        'ks7': '37',
        'ks8': '21',
        'ks9': '12',
        'ks10': '9',
        'ks15': '0',
        'seconds_played': '4045284',
        'disconnects': '6'
    }

    assert result[1]['date'] == today
    assert result[1]['data']['nickname'] == 'skepparn_'

    teardown()
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
