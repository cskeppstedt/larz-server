import sys
from firebase import firebase
from poll import Poll
from push import Push
import vars


def main():
    print "Polling matches for {} users".format(len(vars.USERS))
    matches = Poll().matches(vars.USERS)
    print "Recieved data for {} matches".format(len(matches))

    auth     = firebase.FirebaseAuthentication(vars.SECRET, vars.EMAIL)
    endpoint = firebase.FirebaseApplication(vars.FB_URL)
    endpoint.authentication = auth

    Push(endpoint).matches(matches)
    print "Pushed {} matches to firebase".format(len(matches))


if __name__ == "__main__":
    main()
