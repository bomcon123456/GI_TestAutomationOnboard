Feature: QueryChat ask flow
  As an user,
  After logging in at QueryChat and redirected to the homepage,
  I can ask question and receives answer from the expert.


  Scenario: As a new user, I want to ask a question on Querychat.
    Given I logs in by signing up
    And Expert logs in by signing up
    And Expert starts working
    When I posts a question
    And Expert claims that question
    Then I should see that the expert and I are in the same room