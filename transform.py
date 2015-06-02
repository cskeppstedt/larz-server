def to_player(multimatch_data):
    d = multimatch_data

    def copy():
        return lambda key: d[key]

    def rename(fromKey):
        return lambda key: d[fromKey]

    def n(key):
        return int(d[key])

    def f(key):
        return float(d[key])

    def rate(key):
        return lambda _: str(int(60 * f(key) / f('secs')))

    def lasthits():
        return lambda _: str(n('teamcreepkills') + n('neutralcreepkills'))

    mapping = {
        'apm':         rate('actions'),
        'deaths':      copy(),
        'delta_mmr':   rename('amm_team_rating'),
        'denies':      copy(),
        'gpm':         rate('gold'),
        'hero_id':     copy(),
        'heroassists': copy(),
        'herokills':   copy(),
        'lasthits':    lasthits(),
        'level':       copy(),
        'nickname':    copy(),
        'wards':       copy(),
        'xpm':         rate('exp')
    }

    return {k: mapping[k](k) for k in mapping.iterkeys()}


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

    def consumables():
        return data['rnk_consumables']

    def actions():
        return data['rnk_actions']

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

    def seconds_dead():
        return data['rnk_secs_dead']

    def seconds_played():
        return data['rnk_secs']

    def seconds_earning_exp():
        return data['rnk_time_earning_exp']

    def kicked():
        return data['rnk_kicked']

    def level():
        return data['rnk_level']

    def deaths():
        return data['rnk_deaths']

    def herokills():
        return data['rnk_herokills']

    def heroassists():
        return data['rnk_heroassists']

    def smackdown():
        return data['rnk_smackdown']

    def humiliation():
        return data['rnk_humiliation']

    def nemesis():
        return data['rnk_nemesis']

    def retribution():
        return data['rnk_retribution']

    return {
        'nickname': data['nickname'],
        'mmr': mmr(),
        'games_played': games_played(),
        'wins': wins(),
        'losses': losses(),
        'concedes': concedes(),
        'concedevotes': concedevotes(),
        'buybacks': buybacks(),
        'wards': wards(),
        'consumables': consumables(),
        'actions': actions(),
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
        'seconds_dead': seconds_dead(),
        'seconds_earning_exp': seconds_earning_exp(),
        'disconnects': disconnects(),
        'kicked': kicked(),
        'level': level(),
        'deaths': deaths(),
        'herokills': herokills(),
        'heroassists': heroassists(),
        'smackdown': smackdown(),
        'humiliation': humiliation(),
        'nemesis': nemesis(),
        'retribution': retribution(),
    }
