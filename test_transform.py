import helpers
import json
from transform import to_player

fixture = json.loads(helpers.read_file('./fixtures/transform_to_player.json'))


class TestToPlayer:
    def assert_key(self, key, val):
        player = to_player(fixture)
        assert player[key] == val

    # copied attributes
    def test_copied_keys(self):
        player = to_player(fixture)
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
            assert player[k] == fixture[k]

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
