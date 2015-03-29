def to_player(multimatch_data):
    keys = ['deaths', 'herokills', 'level', 'hero_id', 'nickname', 'heroassists']
    player = { k: data[k] for k in keys }
    return player
