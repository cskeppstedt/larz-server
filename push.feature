Feature: Push
    A way to push transformed match statistics to Firebase 

Scenario: Pushing matches
    Given a list of matches
    Then it should push all matches to firebase

Scenario: Pushing posts
    Given a post
    Then it should push the post to Firebase
