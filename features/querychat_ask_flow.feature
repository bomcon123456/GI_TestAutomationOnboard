Feature: QueryChat ask flow
  As an user,
  After logging in at QueryChat and redirected to the homepage,
  I can ask question and receives answer from the expert.


  Scenario: I register and ask a question on QueryChat.
    Given I'm on AskerHomePage
    When I open AskerSignUpModal
    And I enter email
    And I enter password
    And I enter confirm password
    And I press sign up
    Then TermsConditionsModal should be presented
    When I press Next
    Then I should be redirected to AskerHomePage
    # Expert register
    When Expert is on ExpertHomePage
    And Expert presses login button
    Then A dropdown should show up
    When Expert presses Signup
    Then The dropdown should show sign up form
    When Expert enters email
    And Expert enters password
    And Expert enters confirm password
    And Expert click Sign Up button
    Then TermsConditionsModal should be presented
    When Expert presses Next
    Then Expert should be redirected to ExpertOnboardPage
    When Admin bypass that expert
    And Expert go to ExpertHomePage
    And Expert press Start Working Button
    Then Expert should see the ExpertWorkspacePage
    # Start querying
    When I posts a question
    Then Expert should see that question
    When Expert claims the question
    Then I should be in the same room with that expert