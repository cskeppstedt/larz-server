import time


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

def to_player_stats(data):
    def mmr():
        return data['rnk_amm_team_rating']

    def games_played():
        return data['rnk_games_played']

    def wins():
        return data['rnk_wins']

    def losses():
        return data['rnk_losses']

    def disconnects():
        return data['rnk_discos']

    def concedes():
        return data['rnk_concedes']

    def concedevotes():
        return data['rnk_concedevotes']

    def buybacks():
        return data['rnk_buybacks']

    def wards():
        return data['rnk_wards']
    
    def bloodlust():
        return data['rnk_bloodlust']
    
    def doublekill():
        return data['rnk_doublekill']
    
    def triplekill():
        return data['rnk_triplekill']
    
    def quadkill():
        return data['rnk_quadkill']
    
    def annihilation():
        return data['rnk_annihilation']
    
    def ks3():
        return data['rnk_ks3']
    
    def ks4():
        return data['rnk_ks4']
    
    def ks5():
        return data['rnk_ks5']
    
    def ks6():
        return data['rnk_ks6']
    
    def ks7():
        return data['rnk_ks7']
    
    def ks8():
        return data['rnk_ks8']
    
    def ks9():
        return data['rnk_ks9']
    
    def ks10():
        return data['rnk_ks10']
    
    def ks15():
        return data['rnk_ks15']

    def seconds_played():
        return data['rnk_secs']

    return { 
        'date': time.strftime("%Y-%m-%d"),
        'data': {
            'nickname': data['nickname'],
            'mmr': mmr(),
            'games_played': games_played(),
            'wins': wins(),
            'losses': losses(),
            'concedes': concedes(),
            'concedevotes': concedevotes(),
            'buybacks': buybacks(),
            'wards': wards(),
            'bloodlust': bloodlust(),
            'doublekill': doublekill(),
            'triplekill': triplekill(),
            'quadkill': quadkill(),
            'annihilation': annihilation(),
            'ks3': ks3(),
            'ks4': ks4(),
            'ks5': ks5(),
            'ks6': ks6(),
            'ks7': ks7(),
            'ks8': ks8(),
            'ks9': ks9(),
            'ks10': ks10(),
            'ks15': ks15(),
            'seconds_played': seconds_played(),
            'disconnects': disconnects(),
        }
    }

