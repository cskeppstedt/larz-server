from mock import Mock
from push import Push
from pytest_bdd import scenario, given, then
import helpers
import json


@scenario('push.feature', 'Pushing matches')
def test_pushing_matches():
    pass


@given('a list of matches')
def list_of_match():
    content = helpers.read_file("./fixtures/push_list-of-match.json")
    return json.loads(content)


@then('it should push all matches to firebase')
def push_foreach_match(list_of_match):
    endpoint = Mock()
    instance = Push(endpoint)
    instance.matches(list_of_match)

    for m in list_of_match:
        endpoint.put.assert_any_call('/matches/', m['match_id'], m)


# -----


@scenario('push.feature', 'Pushing posts')
def test_pushing_posts():
    pass


@given('a post')
def a_post():
    return {
        'post_id': 'foo1',
        'published': '2015-03-10',
        'embed_url': 'http://blabla.com/video.foo1'
    }


@then('it should push the post to Firebase')
def push_post(a_post):
    endpoint = Mock()
    instance = Push(endpoint)
    instance.post(a_post)

    endpoint.put.assert_any_call('/posts/', a_post['post_id'], a_post)


# -----


@scenario('push.feature', 'Pushing player stats')
def test_pushing_player_stats():
    pass


@given('a list of player stats')
def player_stats():
    return {
        'date': '2015-04-27',
        'data': {
            'Schln': {
                'nickname': '1',
                'mmr': '1499'
            },
            'skepparn_': {
                'nickname': '2',
                'mmr': '1733'
            }
        }
    }


@then('it should push all stats to Firebase')
def push_player_stats(player_stats):
    endpoint = Mock()
    instance = Push(endpoint)
    instance.player_stats(player_stats)
    key = player_stats['date']

    endpoint.put.assert_any_call('/stats/', key, player_stats)
