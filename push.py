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


    # =====================================================
    #  Private API
    # =====================================================
    def push_match(self, match):
        url = "/matches/{}".format(match['match_id'])
        print " - pushing match to " + url
        try:
            self.endpoint.post(url, match)
        except BaseException as err:
            print err
