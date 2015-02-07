from pytest_bdd import scenario, given, when, then
from poll import Poll

@scenario('poll.feature', 'Polling matches')
def test_polling_matches():
    pass

@given('a list of userid')
def list_of_userid():
    return ['1','2','3']

@then('it should pull matches for each userid')
def pull_foreach_userid(list_of_userid):
    pass

@then('it should pull stats for the 10 latest, unique matches')
def pull_matches(list_of_userid):
    pass

@then('it should return the matches')
def no_duplicate_matches(list_of_userid):
    pass

