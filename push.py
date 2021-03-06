def log(message):
    print "  [ push ]  ", message


class Push:
    # =====================================================
    #  Constructor
    # =====================================================
    def __init__(self, endpoint):
        self.endpoint = endpoint

    # =====================================================
    #  Public API
    # =====================================================
    def matches(self, list_of_match):
        for m in list_of_match:
            self.push_match(m)

    def post(self, post):
        self.push_post(post)

    def player_stats(self, stats):
        self.push_player_stats(stats)

    # =====================================================
    #  Private API
    # =====================================================
    def push_match(self, match):
        m_id = match['match_id']
        url = "/matches/"
        log("pushing %s%s" % (url, m_id))

        try:
            self.endpoint.put(url, m_id, match)
        except BaseException as err:
            print err

    def push_post(self, post):
        p_id = post['post_id']
        url = "/posts/"
        log("pushing %s%s" % (p_id, url))

        try:
            self.endpoint.put(url, p_id, post)
        except BaseException as err:
            print err

    def push_player_stats(self, entry):
        key = entry['date']
        url = "/stats/"

        log("pushing %s%s" % (url, key))

        try:
            self.endpoint.put(url, key, entry)
        except BaseException as err:
            print err
