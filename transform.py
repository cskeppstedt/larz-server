def to_player(multimatch_data):
    d = multimatch_data
    
    def n(key):
        return int(d[key])

    def f(key):
        return float(d[key])

    def rate(key):
        r = f(key) / f('secs')
        return str(int(60 * r))

    def apm():
        return rate('actions')

    def gpm():
        return rate('gold')

    def xpm():
        return rate('exp')

    def wards():
        return d['wards']

    def lasthits():
        return str(n('teamcreepkills') + n('neutralcreepkills'))

    def mmr_delta():
        return d['amm_team_rating']
    
    keys = [
        'denies',
        'deaths',
        'herokills',
        'level',
        'hero_id',
        'nickname', 
        'heroassists',
        'wards'
    ]

    player = { k: d[k] for k in keys }

    player['apm']      = apm()
    player['gpm']      = gpm()
    player['xpm']      = xpm()
    player['lasthits'] = lasthits()

    player['delta_mmr'] = d['amm_team_rating']

    return player

