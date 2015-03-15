import sys
from firebase import firebase
from poll import Poll
from push import Push
import vars


def log(message):
    print "  [ main ]  ", message


def main():
    log('fetching stats for %d users' % len(vars.USERS))

    tokens  = Poll().match_tokens(vars.USERS)
    if len(tokens) == 0:
        log('no tokens, exiting')
        return

    matches = Poll().matches(tokens)
    if len(matches) == 0:
        log('no matches, exiting')
        return

    log("recieved %d match tokens" % len(matches))
    
    auth     = firebase.FirebaseAuthentication(vars.SECRET, vars.EMAIL)
    endpoint = firebase.FirebaseApplication(vars.FB_URL)
    endpoint.authentication = auth

    Push(endpoint).matches(matches)
    log("pushed %d matches to firebase" % len(matches))


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


if __name__ == "__main__":
    main()
