import helpers
import json
from transform import to_player, to_player_stats

player_fixture = json.loads(helpers.read_file('./fixtures/transform_to_player.json'))
stats_fixture = json.loads(helpers.read_file('./fixtures/transform_to_player_stats.json'))


class TestToPlayer:
    def assert_key(self, key, val):
        player = to_player(player_fixture)
        assert player[key] == val

    # copied attributes
    def test_copied_keys(self):
        player = to_player(player_fixture)
        keys = [
            'deaths',
            'herokills',
            'level',
            'hero_id',
            'nickname',
            'heroassists',
            'wards',
            'denies'
        ]

        for k in keys:
            assert player[k] == player_fixture[k]

    def test_apm(self):
        self.assert_key('apm', '111')

    def test_gpm(self):
        self.assert_key('gpm', '139')

    def test_xpm(self):
        self.assert_key('xpm', '152')

    def test_last_hits(self):
        self.assert_key('lasthits', '19')

    def test_delta_mmr(self):
        self.assert_key('delta_mmr', '-4.707')


class TestToPlayerStats:
    def assert_key(self, key, val):
        stats = to_player_stats(stats_fixture)
        assert stats[key] == val

    def test_nickname(self):
        self.assert_key('nickname', 'Schln')

    def test_mmr(self):
        self.assert_key('mmr', '1574.691')

    def test_games_played(self):
        self.assert_key('games_played', '1843')

    def test_wins(self):
        self.assert_key('wins', '914')

    def test_losses(self):
        self.assert_key('losses', '929')

    def test_disconnects(self):
        self.assert_key('disconnects', '6')

    def test_concedes(self):
        self.assert_key('concedes', '851')

    def test_concedevotes(self):
        self.assert_key('concedevotes', '174')

    def test_buybacks(self):
        self.assert_key('buybacks', '66')

    def test_wards(self):
        self.assert_key('wards', '8138')

    def test_consumables(self):
        self.assert_key('consumables', '11549')

    def test_actions(self):
        self.assert_key('actions', '9068281')

    def test_bloodlust(self):
        self.assert_key('bloodlust', '158')

    def test_doublekill(self):
        self.assert_key('doublekill', '523')

    def test_triplekill(self):
        self.assert_key('triplekill', '45')

    def test_quadkill(self):
        self.assert_key('quadkill', '3')

    def test_annihilation(self):
        self.assert_key('annihilation', '0')

    def test_annihilation(self):
        self.assert_key('annihilation', '0')

    def test_ks3(self):
        self.assert_key('ks3', '512')

    def test_ks4(self):
        self.assert_key('ks4', '237')

    def test_ks5(self):
        self.assert_key('ks5', '135')

    def test_ks6(self):
        self.assert_key('ks6', '68')

    def test_ks7(self):
        self.assert_key('ks7', '37')

    def test_ks8(self):
        self.assert_key('ks8', '21')

    def test_ks9(self):
        self.assert_key('ks9', '12')

    def test_ks10(self):
        self.assert_key('ks10', '9')

    def test_ks15(self):
        self.assert_key('ks15', '0')

    def test_seconds_dead(self):
        self.assert_key('seconds_dead', '439133')

    def test_seconds_played(self):
        self.assert_key('seconds_played', '4045284')

    def test_seconds_earning_exp(self):
        self.assert_key('seconds_earning_exp', '4040452')

    def test_kicked(self):
        self.assert_key('kicked', '0')

    def test_level(self):
        self.assert_key('level', '39')

    def test_deaths(self):
        self.assert_key('deaths', '10986')

    def test_herokills(self):
        self.assert_key('herokills', '6935')

    def test_heroassists(self):
        self.assert_key('heroassists', '18994')

    def test_smackdown(self):
        self.assert_key('smackdown', '0')

    def test_humiliation(self):
        self.assert_key('humiliation', '10')

    def test_nemesis(self):
        self.assert_key('nemesis', '5552')

    def test_retribution(self):
        self.assert_key('retribution', '171')
