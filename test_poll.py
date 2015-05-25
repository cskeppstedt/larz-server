from poll import Poll
from pytest_bdd import scenario, given, then
import helpers
import httpretty
import re
import time


# --- polling match tokens ---


@scenario('poll.feature', 'Polling match tokens')
def test_polling_match_tokens():
    pass


@given('a list of userid')
def list_of_userid():
    return ['1', '2']


@then('it should pull matches for each userid')
def pull_foreach_userid(list_of_userid):
    req_urls = []
    expected_urls = map(helpers.match_history_uri, list_of_userid)

    httpretty.enable()
    add_fixtures(lambda _, uri, __: req_urls.append(uri))

    Poll().match_tokens(list_of_userid)

    assert req_urls == expected_urls
    teardown()


@then('it should return the match tokens')
def return_tokens(list_of_userid):
    httpretty.enable()
    add_fixtures()

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
    add_fixtures(lambda _, uri, __: req_urls.append(uri))

    Poll().matches(list_of_token)
    matches_url = req_urls[0]

    assert matches_url == expected_url
    teardown()


@then('it should return the match data')
def return_matches(list_of_token):
    httpretty.enable()
    add_fixtures()

    result = Poll().matches(list_of_token)
    first = result[0]

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
    add_fixtures(lambda _, uri, __: req_urls.append(uri))

    Poll().player_stats(list_of_userid)

    assert req_urls == expected_urls
    teardown()


@then('it should return the player stats')
def return_player_stats(list_of_userid):
    httpretty.enable()
    add_fixtures()

    result = Poll().player_stats(list_of_userid)

    today = time.strftime("%Y-%m-%d")

    assert result['date'] == today
    assert result['data'] == {
        'Schln': {
            'nickname': 'Schln',
            'mmr': '1574.691',
            'games_played': '1843',
            'wins': '914',
            'losses': '929',
            'concedes': '851',
            'concedevotes': '174',
            'buybacks': '66',
            'wards': '8138',
            'consumables': '11549',
            'actions': '9068281',
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
            'seconds_dead': '439133',
            'seconds_earning_exp': '4040452',
            'disconnects': '6',
            'kicked': '0',
            'level': '39',
            'deaths': '10986',
            'herokills': '6935',
            'heroassists': '18994',
            'smackdown': '0',
            'humiliation': '10',
            'nemesis': '5552',
            'retribution': '171',
        },
        'skepparn_': {
            'nickname': 'skepparn_',
            'mmr': '1550.637',
            'games_played': '1166',
            'wins': '585',
            'losses': '581',
            'concedes': '529',
            'concedevotes': '142',
            'buybacks': '114',
            'wards': '4957',
            'consumables': '9805',
            'actions': '4586202',
            'bloodlust': '112',
            'doublekill': '404',
            'triplekill': '48',
            'quadkill': '8',
            'annihilation': '0',
            'ks3': '345',
            'ks4': '183',
            'ks5': '74',
            'ks6': '37',
            'ks7': '24',
            'ks8': '12',
            'ks9': '11',
            'ks10': '7',
            'ks15': '0',
            'seconds_played': '2531580',
            'seconds_dead': '400039',
            'seconds_earning_exp': '2525213',
            'disconnects': '3',
            'kicked': '0',
            'level': '31',
            'deaths': '7535',
            'herokills': '4717',
            'heroassists': '12061',
            'smackdown': '0',
            'humiliation': '1',
            'nemesis': '3617',
            'retribution': '143',
        }
    }

    teardown()
    pass


# --- helpers ---

def add_fixtures(response_cb=None):
    def cb(req, uri, headers):
        if response_cb is not None:
            response_cb(req, uri, headers)

        body = helpers.fixture_for(uri)
        return (200, headers, body)

    httpretty.register_uri(httpretty.GET,
                           re.compile("(.*)"),
                           body=cb,
                           content_type="application/json")


def teardown():
    httpretty.disable()
    httpretty.reset()
