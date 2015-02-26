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
        m_id = match['match_id']
        url  = "/matches/"
        print " - pushing match {} to {}".format(m_id, url)
        
        try:
            self.endpoint.put(url, m_id, match)
        except BaseException as err:
            print err
