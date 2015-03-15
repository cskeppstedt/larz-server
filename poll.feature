Feature: Poll
    A way to poll statistics from the HoN API

Scenario: Polling match tokens
    Given a list of userid
    Then it should pull matches for each userid
    And it should return the match tokens

Scenario: Polling matches
    Given a list of match tokens
    Then it should pull the matches
    And it should return the match data
