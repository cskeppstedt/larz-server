import os
default_value = 'not_set'

EMAIL        = os.getenv('LARZSERVER_EMAIL', default_value)
SECRET       = os.getenv('LARZSERVER_FIREBASE_SECRET', default_value)
FB_URL       = os.getenv('LARZSERVER_FIREBASE_URL', 'http://{}'.format(default_value))
API_BASE_URL = os.getenv('LARZSERVER_API_URL', 'http://{}'.format(default_value))
API_TOKEN    = os.getenv('LARZSERVER_API_TOKEN', default_value)
USERS        = [
    'skepparn_',
    'Pacoloco',
    'Adelsmansman',
    'Schln',
    'zwex',
    'khoosan'
]
