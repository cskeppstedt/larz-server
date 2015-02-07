Feature: Poll
    A way to poll statistics from the HoN API

Scenario: Polling matches
    Given a list of userid
    Then it should pull matches for each userid
    And it should pull stats for the 10 latest, unique matches
    And it should return the matches
