class Push:
    # =====================================================
    #  Constructor
    # =====================================================
    def __init__(self, endpoint):
        self.endpoint = endpoint


    # =====================================================
    #  Public API
    # =====================================================
    def push_matches(self, list_of_match):
        for m in list_of_match:
            self.push_match(m) 


    # =====================================================
    #  Private API
    # =====================================================
    def push_match(self, match):
        url = "/matches/{}".format(match['match_id'])
        self.endpoint.post(url, match)
