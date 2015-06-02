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


def to_player_stats(stats_data):
    d = stats_data

    def copy():
        return lambda key: d[key]

    def rename(fromKey):
        return lambda key: d[fromKey]

    mapping = {
        'actions':             rename('rnk_actions'),
        'annihilation':        rename('rnk_annihilation'),
        'bloodlust':           rename('rnk_bloodlust'),
        'buybacks':            rename('rnk_buybacks'),
        'concedes':            rename('rnk_concedes'),
        'concedevotes':        rename('rnk_concedevotes'),
        'consumables':         rename('rnk_consumables'),
        'deaths':              rename('rnk_deaths'),
        'disconnects':         rename('rnk_discos'),
        'doublekill':          rename('rnk_doublekill'),
        'games_played':        rename('rnk_games_played'),
        'heroassists':         rename('rnk_heroassists'),
        'herokills':           rename('rnk_herokills'),
        'humiliation':         rename('rnk_humiliation'),
        'kicked':              rename('rnk_kicked'),
        'ks10':                rename('rnk_ks10'),
        'ks15':                rename('rnk_ks15'),
        'ks3':                 rename('rnk_ks3'),
        'ks4':                 rename('rnk_ks4'),
        'ks5':                 rename('rnk_ks5'),
        'ks6':                 rename('rnk_ks6'),
        'ks7':                 rename('rnk_ks7'),
        'ks8':                 rename('rnk_ks8'),
        'ks9':                 rename('rnk_ks9'),
        'level':               rename('rnk_level'),
        'losses':              rename('rnk_losses'),
        'mmr':                 rename('rnk_amm_team_rating'),
        'nemesis':             rename('rnk_nemesis'),
        'nickname':            copy(),
        'quadkill':            rename('rnk_quadkill'),
        'retribution':         rename('rnk_retribution'),
        'seconds_dead':        rename('rnk_secs_dead'),
        'seconds_earning_exp': rename('rnk_time_earning_exp'),
        'seconds_played':      rename('rnk_secs'),
        'smackdown':           rename('rnk_smackdown'),
        'triplekill':          rename('rnk_triplekill'),
        'wards':               rename('rnk_wards'),
        'wins':                rename('rnk_wins')
    }

    return {k: mapping[k](k) for k in mapping.iterkeys()}
