import sys
from firebase import firebase
from poll import Poll
from push import Push
import vars


def log(funcName, message):
    print "  [ %s ]  %s" % (funcName, message)


def matches():
    log('matches', 'fetching stats for %d users' % len(vars.USERS))

    tokens  = Poll().match_tokens(vars.USERS)
    if len(tokens) == 0:
        log('matches', 'no tokens, exiting')
        return

    matches = Poll().matches(tokens)
    if len(matches) == 0:
        log('matches', 'no matches, exiting')
        return

    log('matches', "recieved %d match tokens" % len(matches))
    
    auth     = firebase.FirebaseAuthentication(vars.SECRET, vars.EMAIL)
    endpoint = firebase.FirebaseApplication(vars.FB_URL)
    endpoint.authentication = auth

    Push(endpoint).matches(matches)
    log('matches', "pushed %d matches to firebase" % len(matches))

def players():
    log('players', 'wassup')


def publish():
    auth     = firebase.FirebaseAuthentication(vars.SECRET, vars.EMAIL)
    endpoint = firebase.FirebaseApplication(vars.FB_URL)
    endpoint.authentication = auth

    post = {
        'embed_url': 'https://www.youtube.com/embed/UVsIGAEnK_4',
        'post_id': '2',
        'published': '2015-03-14 19:10'
    }

    Push(endpoint).post(post)


def main(argv):
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: %s <matches|players>" % (argv[0],))
        return 1

    arg = argv[1].strip().lower()

    if arg == 'players':
        players()
        return 0
    elif arg == 'matches':
        matches()
        return 0
    else:
        sys.stderr.write("Invalid argument %s; valid arguments: matches, players" % (arg,))
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
