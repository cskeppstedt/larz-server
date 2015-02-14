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
    expected = [{'winning_team': u'2', 'match_id': u'136020720', 'team2': [{'deaths': u'3', 'herokills': u'3', 'level': u'8', 'hero_id': u'43', 'nickname': u'DB_Killer', 'heroassists': u'8'}, {'deaths': u'2', 'herokills': u'0', 'level': u'13', 'hero_id': u'206', 'nickname': u'Thumping', 'heroassists': u'15'}, {'deaths': u'2', 'herokills': u'3', 'level': u'12', 'hero_id': u'163', 'nickname': u'One_of_Few', 'heroassists': u'8'}, {'deaths': u'1', 'herokills': u'13', 'level': u'14', 'hero_id': u'103', 'nickname': u'm0zak', 'heroassists': u'4'}, {'deaths': u'3', 'herokills': u'3', 'level': u'12', 'hero_id': u'210', 'nickname': u'Counsellor', 'heroassists': u'11'}], 'team1': [{'deaths': u'3', 'herokills': u'2', 'level': u'12', 'hero_id': u'165', 'nickname': u'deimi', 'heroassists': u'2'}, {'deaths': u'3', 'herokills': u'5', 'level': u'11', 'hero_id': u'102', 'nickname': u'Schln', 'heroassists': u'4'}, {'deaths': u'4', 'herokills': u'2', 'level': u'7', 'hero_id': u'169', 'nickname': u'skepparn_', 'heroassists': u'4'}, {'deaths': u'4', 'herokills': u'0', 'level': u'10', 'hero_id': u'201', 'nickname': u'dolanduck101', 'heroassists': u'3'}, {'deaths': u'8', 'herokills': u'2', 'level': u'9', 'hero_id': u'204', 'nickname': u'__I1I__', 'heroassists': u'6'}]}, {'winning_team': u'2', 'match_id': u'136021420', 'team2': [{'deaths': u'11', 'herokills': u'14', 'level': u'25', 'hero_id': u'115', 'nickname': u'Rackerkecy', 'heroassists': u'29'}, {'deaths': u'8', 'herokills': u'19', 'level': u'25', 'hero_id': u'196', 'nickname': u'EmmaGoldman', 'heroassists': u'30'}, {'deaths': u'12', 'herokills': u'5', 'level': u'25', 'hero_id': u'197', 'nickname': u'Giannis_13', 'heroassists': u'41'}, {'deaths': u'13', 'herokills': u'17', 'level': u'24', 'hero_id': u'38', 'nickname': u'RedVergil', 'heroassists': u'12'}, {'deaths': u'13', 'herokills': u'12', 'level': u'25', 'hero_id': u'39', 'nickname': u'tyrakheczy', 'heroassists': u'25'}], 'team1': [{'deaths': u'12', 'herokills': u'6', 'level': u'25', 'hero_id': u'27', 'nickname': u'Marv21', 'heroassists': u'24'}, {'deaths': u'10', 'herokills': u'21', 'level': u'25', 'hero_id': u'242', 'nickname': u'pyROMenniels', 'heroassists': u'13'}, {'deaths': u'14', 'herokills': u'7', 'level': u'21', 'hero_id': u'203', 'nickname': u'Schln', 'heroassists': u'23'}, {'deaths': u'12', 'herokills': u'14', 'level': u'25', 'hero_id': u'236', 'nickname': u'skepparn_', 'heroassists': u'24'}, {'deaths': u'19', 'herokills': u'9', 'level': u'23', 'hero_id': u'6', 'nickname': u'Nilo', 'heroassists': u'22'}]}, {'winning_team': u'2', 'match_id': u'136023435', 'team2': [{'deaths': u'5', 'herokills': u'10', 'level': u'23', 'hero_id': u'95', 'nickname': u'snushenke', 'heroassists': u'24'}, {'deaths': u'6', 'herokills': u'2', 'level': u'21', 'hero_id': u'168', 'nickname': u'Adelsmansman', 'heroassists': u'26'}, {'deaths': u'7', 'herokills': u'20', 'level': u'23', 'hero_id': u'216', 'nickname': u'Pacoloco', 'heroassists': u'13'}, {'deaths': u'10', 'herokills': u'9', 'level': u'19', 'hero_id': u'20', 'nickname': u'skepparn_', 'heroassists': u'16'}, {'deaths': u'11', 'herokills': u'7', 'level': u'20', 'hero_id': u'233', 'nickname': u'Kriticall', 'heroassists': u'20'}], 'team1': [{'deaths': u'7', 'herokills': u'6', 'level': u'17', 'hero_id': u'12', 'nickname': u'danionino', 'heroassists': u'21'}, {'deaths': u'9', 'herokills': u'11', 'level': u'21', 'hero_id': u'192', 'nickname': u'Unreal234', 'heroassists': u'15'}, {'deaths': u'8', 'herokills': u'5', 'level': u'19', 'hero_id': u'13', 'nickname': u'yelworC', 'heroassists': u'12'}, {'deaths': u'12', 'herokills': u'10', 'level': u'22', 'hero_id': u'42', 'nickname': u'tsalkat', 'heroassists': u'10'}, {'deaths': u'12', 'herokills': u'7', 'level': u'16', 'hero_id': u'110', 'nickname': u'TheGo0n', 'heroassists': u'11'}]}, {'winning_team': u'1', 'match_id': u'136026090', 'team2': [{'deaths': u'7', 'herokills': u'5', 'level': u'14', 'hero_id': u'205', 'nickname': u'DB_Killer', 'heroassists': u'6'}, {'deaths': u'6', 'herokills': u'8', 'level': u'18', 'hero_id': u'5', 'nickname': u'Zaludemocelo', 'heroassists': u'11'}, {'deaths': u'5', 'herokills': u'6', 'level': u'20', 'hero_id': u'236', 'nickname': u'Dr_Zlo_lolo', 'heroassists': u'9'}, {'deaths': u'5', 'herokills': u'2', 'level': u'14', 'hero_id': u'9', 'nickname': u'Kelghor', 'heroassists': u'9'}, {'deaths': u'6', 'herokills': u'3', 'level': u'14', 'hero_id': u'10', 'nickname': u'silvio_saint', 'heroassists': u'5'}], 'team1': [{'deaths': u'3', 'herokills': u'1', 'level': u'19', 'hero_id': u'31', 'nickname': u'Adelsmansman', 'heroassists': u'17'}, {'deaths': u'6', 'herokills': u'9', 'level': u'14', 'hero_id': u'27', 'nickname': u'Schln', 'heroassists': u'7'}, {'deaths': u'6', 'herokills': u'9', 'level': u'18', 'hero_id': u'212', 'nickname': u'Pacoloco', 'heroassists': u'9'}, {'deaths': u'6', 'herokills': u'2', 'level': u'16', 'hero_id': u'204', 'nickname': u'skepparn_', 'heroassists': u'13'}, {'deaths': u'3', 'herokills': u'8', 'level': u'20', 'hero_id': u'24', 'nickname': u'FunkyKareem', 'heroassists': u'7'}]}, {'winning_team': u'1', 'match_id': u'136028023', 'team2': [{'deaths': u'5', 'herokills': u'12', 'level': u'20', 'hero_id': u'44', 'nickname': u'ruse', 'heroassists': u'7'}, {'deaths': u'6', 'herokills': u'1', 'level': u'13', 'hero_id': u'205', 'nickname': u'krudtugle', 'heroassists': u'10'}, {'deaths': u'7', 'herokills': u'5', 'level': u'13', 'hero_id': u'10', 'nickname': u'elsvupper', 'heroassists': u'6'}, {'deaths': u'5', 'herokills': u'7', 'level': u'17', 'hero_id': u'226', 'nickname': u'supermcnasti', 'heroassists': u'10'}, {'deaths': u'7', 'herokills': u'8', 'level': u'16', 'hero_id': u'8', 'nickname': u'langefatmund', 'heroassists': u'14'}], 'team1': [{'deaths': u'8', 'herokills': u'1', 'level': u'16', 'hero_id': u'3', 'nickname': u'ThienLe', 'heroassists': u'13'}, {'deaths': u'5', 'herokills': u'9', 'level': u'18', 'hero_id': u'242', 'nickname': u'Adelsmansman', 'heroassists': u'12'}, {'deaths': u'7', 'herokills': u'7', 'level': u'14', 'hero_id': u'204', 'nickname': u'Schln', 'heroassists': u'10'}, {'deaths': u'10', 'herokills': u'5', 'level': u'14', 'hero_id': u'21', 'nickname': u'Pacoloco', 'heroassists': u'10'}, {'deaths': u'3', 'herokills': u'8', 'level': u'19', 'hero_id': u'236', 'nickname': u'skepparn_', 'heroassists': u'11'}]}, {'winning_team': u'2', 'match_id': u'136095625', 'team2': [{'deaths': u'8', 'herokills': u'12', 'level': u'22', 'hero_id': u'233', 'nickname': u'Schln', 'heroassists': u'20'}, {'deaths': u'6', 'herokills': u'11', 'level': u'19', 'hero_id': u'43', 'nickname': u'skepparn_', 'heroassists': u'23'}, {'deaths': u'6', 'herokills': u'5', 'level': u'20', 'hero_id': u'10', 'nickname': u'BeefN', 'heroassists': u'27'}, {'deaths': u'7', 'herokills': u'9', 'level': u'21', 'hero_id': u'22', 'nickname': u'Sexistenz', 'heroassists': u'23'}, {'deaths': u'6', 'herokills': u'11', 'level': u'21', 'hero_id': u'41', 'nickname': u'ltzMcFly', 'heroassists': u'12'}], 'team1': [{'deaths': u'7', 'herokills': u'10', 'level': u'23', 'hero_id': u'216', 'nickname': u'Sitting_Duck', 'heroassists': u'9'}, {'deaths': u'10', 'herokills': u'3', 'level': u'16', 'hero_id': u'8', 'nickname': u'AxEeLl', 'heroassists': u'14'}, {'deaths': u'6', 'herokills': u'3', 'level': u'15', 'hero_id': u'7', 'nickname': u'SnyggEric', 'heroassists': u'9'}, {'deaths': u'14', 'herokills': u'12', 'level': u'18', 'hero_id': u'240', 'nickname': u'Wizzard_cz', 'heroassists': u'8'}, {'deaths': u'11', 'herokills': u'4', 'level': u'15', 'hero_id': u'110', 'nickname': u'N1l3', 'heroassists': u'10'}]}, {'winning_team': u'2', 'match_id': u'136097421', 'team2': [{'deaths': u'10', 'herokills': u'4', 'level': u'13', 'hero_id': u'27', 'nickname': u'Schln', 'heroassists': u'15'}, {'deaths': u'3', 'herokills': u'12', 'level': u'22', 'hero_id': u'225', 'nickname': u'skepparn_', 'heroassists': u'9'}, {'deaths': u'3', 'herokills': u'5', 'level': u'17', 'hero_id': u'217', 'nickname': u'galaxy91620', 'heroassists': u'12'}, {'deaths': u'7', 'herokills': u'3', 'level': u'14', 'hero_id': u'3', 'nickname': u'IMURD', 'heroassists': u'14'}, {'deaths': u'9', 'herokills': u'9', 'level': u'18', 'hero_id': u'242', 'nickname': u'BlackMerlien', 'heroassists': u'16'}], 'team1': [{'deaths': u'8', 'herokills': u'8', 'level': u'18', 'hero_id': u'210', 'nickname': u'Bumsnickel', 'heroassists': u'7'}, {'deaths': u'7', 'herokills': u'2', 'level': u'15', 'hero_id': u'192', 'nickname': u'STAVMAN', 'heroassists': u'11'}, {'deaths': u'8', 'herokills': u'2', 'level': u'15', 'hero_id': u'185', 'nickname': u'SilverSh0t', 'heroassists': u'2'}, {'deaths': u'8', 'herokills': u'2', 'level': u'12', 'hero_id': u'168', 'nickname': u'Karpizl', 'heroassists': u'10'}, {'deaths': u'2', 'herokills': u'18', 'level': u'20', 'hero_id': u'16', 'nickname': u'_`DRACULA`_', 'heroassists': u'6'}]}, {'winning_team': u'1', 'match_id': u'136198877', 'team2': [{'deaths': u'5', 'herokills': u'6', 'level': u'13', 'hero_id': u'122', 'nickname': u'Birqe', 'heroassists': u'5'}, {'deaths': u'6', 'herokills': u'5', 'level': u'13', 'hero_id': u'95', 'nickname': u'Schln', 'heroassists': u'9'}, {'deaths': u'7', 'herokills': u'4', 'level': u'14', 'hero_id': u'96', 'nickname': u'Pacoloco', 'heroassists': u'4'}, {'deaths': u'7', 'herokills': u'4', 'level': u'13', 'hero_id': u'238', 'nickname': u'skepparn_', 'heroassists': u'11'}, {'deaths': u'9', 'herokills': u'4', 'level': u'14', 'hero_id': u'242', 'nickname': u'adrenalin161', 'heroassists': u'6'}], 'team1': [{'deaths': u'1', 'herokills': u'7', 'level': u'16', 'hero_id': u'108', 'nickname': u'Cypross', 'heroassists': u'10'}, {'deaths': u'3', 'herokills': u'9', 'level': u'18', 'hero_id': u'3', 'nickname': u'Zjuuu', 'heroassists': u'18'}, {'deaths': u'5', 'herokills': u'6', 'level': u'16', 'hero_id': u'114', 'nickname': u'martyshka', 'heroassists': u'14'}, {'deaths': u'2', 'herokills': u'12', 'level': u'17', 'hero_id': u'94', 'nickname': u'Toboter', 'heroassists': u'11'}, {'deaths': u'12', 'herokills': u'0', 'level': u'13', 'hero_id': u'9', 'nickname': u'Troliukas', 'heroassists': u'5'}]}, {'winning_team': u'1', 'match_id': u'136199362', 'team2': [{'deaths': u'6', 'herokills': u'7', 'level': u'12', 'hero_id': u'106', 'nickname': u'IMBALUCK_', 'heroassists': u'3'}, {'deaths': u'8', 'herokills': u'3', 'level': u'12', 'hero_id': u'233', 'nickname': u'Schln', 'heroassists': u'6'}, {'deaths': u'5', 'herokills': u'0', 'level': u'14', 'hero_id': u'240', 'nickname': u'Pacoloco', 'heroassists': u'5'}, {'deaths': u'7', 'herokills': u'1', 'level': u'11', 'hero_id': u'43', 'nickname': u'skepparn_', 'heroassists': u'6'}, {'deaths': u'7', 'herokills': u'3', 'level': u'12', 'hero_id': u'166', 'nickname': u'K`men', 'heroassists': u'4'}], 'team1': [{'deaths': u'4', 'herokills': u'3', 'level': u'14', 'hero_id': u'3', 'nickname': u'dizzlation', 'heroassists': u'13'}, {'deaths': u'2', 'herokills': u'3', 'level': u'13', 'hero_id': u'35', 'nickname': u'BregOo', 'heroassists': u'14'}, {'deaths': u'3', 'herokills': u'4', 'level': u'15', 'hero_id': u'121', 'nickname': u'_genetic_', 'heroassists': u'12'}, {'deaths': u'1', 'herokills': u'13', 'level': u'18', 'hero_id': u'34', 'nickname': u'D1NAMIT', 'heroassists': u'14'}, {'deaths': u'4', 'herokills': u'10', 'level': u'18', 'hero_id': u'206', 'nickname': u'masteR`J', 'heroassists': u'13'}]}, {'winning_team': u'1', 'match_id': u'136199918', 'team2': [{'deaths': u'6', 'herokills': u'7', 'level': u'21', 'hero_id': u'233', 'nickname': u'Schln', 'heroassists': u'17'}, {'deaths': u'8', 'herokills': u'12', 'level': u'23', 'hero_id': u'217', 'nickname': u'Pacoloco', 'heroassists': u'15'}, {'deaths': u'9', 'herokills': u'14', 'level': u'23', 'hero_id': u'197', 'nickname': u'skepparn_', 'heroassists': u'13'}, {'deaths': u'11', 'herokills': u'5', 'level': u'19', 'hero_id': u'210', 'nickname': u'samua', 'heroassists': u'18'}, {'deaths': u'7', 'herokills': u'9', 'level': u'18', 'hero_id': u'207', 'nickname': u'Singh2810', 'heroassists': u'10'}], 'team1': [{'deaths': u'8', 'herokills': u'10', 'level': u'24', 'hero_id': u'40', 'nickname': u'Th3On3', 'heroassists': u'17'}, {'deaths': u'3', 'herokills': u'6', 'level': u'22', 'hero_id': u'4', 'nickname': u'PeteAir', 'heroassists': u'18'}, {'deaths': u'13', 'herokills': u'13', 'level': u'22', 'hero_id': u'215', 'nickname': u'xhipmunk', 'heroassists': u'14'}, {'deaths': u'7', 'herokills': u'5', 'level': u'23', 'hero_id': u'34', 'nickname': u'xxtrash', 'heroassists': u'24'}, {'deaths': u'16', 'herokills': u'7', 'level': u'19', 'hero_id': u'230', 'nickname': u'XXCHOYXX', 'heroassists': u'17'}]}, {'winning_team': u'2', 'match_id': u'136200860', 'team2': [{'deaths': u'4', 'herokills': u'0', 'level': u'14', 'hero_id': u'21', 'nickname': u'RBreaker', 'heroassists': u'9'}, {'deaths': u'3', 'herokills': u'5', 'level': u'15', 'hero_id': u'206', 'nickname': u'Schln', 'heroassists': u'9'}, {'deaths': u'3', 'herokills': u'5', 'level': u'17', 'hero_id': u'43', 'nickname': u'Pacoloco', 'heroassists': u'10'}, {'deaths': u'5', 'herokills': u'9', 'level': u'16', 'hero_id': u'225', 'nickname': u'skepparn_', 'heroassists': u'4'}, {'deaths': u'7', 'herokills': u'3', 'level': u'15', 'hero_id': u'167', 'nickname': u'vissen90', 'heroassists': u'3'}], 'team1': [{'deaths': u'3', 'herokills': u'4', 'level': u'16', 'hero_id': u'109', 'nickname': u'Gustl', 'heroassists': u'13'}, {'deaths': u'3', 'herokills': u'10', 'level': u'19', 'hero_id': u'104', 'nickname': u'arverage', 'heroassists': u'8'}, {'deaths': u'8', 'herokills': u'1', 'level': u'13', 'hero_id': u'89', 'nickname': u'Bunny`Slayer', 'heroassists': u'9'}, {'deaths': u'5', 'herokills': u'5', 'level': u'14', 'hero_id': u'187', 'nickname': u'elko14', 'heroassists': u'6'}, {'deaths': u'3', 'herokills': u'1', 'level': u'14', 'hero_id': u'4', 'nickname': u'TuSpaccu', 'heroassists': u'9'}]}]
    assert result == expected

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
