Feature: QueryChat ask flow
  As an user,
  After logging in at QueryChat and redirected to the homepage,
  I can ask question and receives answer from the expert.


  @fixture.full_setup
  Scenario: I register and ask a question on QueryChat.
    Given I'm on AskerHomePage
    When I open AskerSignUpModal
    And I enter email
    And I enter password
    And I enter confirm password
    And I press sign up
    Then Asker's TermsConditionsModal should be presented
    When I press Next
    Then I should be redirected to AskerHomePage
    # Expert register
    When Expert is on ExpertHomePage
    And Expert open SignupDropdown
    And Expert enters email
    And Expert enters password
    And Expert enters confirm password
    And Expert click Sign Up button
    Then Expert's TermsConditionsModal should be presented
    When Expert presses Next
    Then Expert should be redirected to ExpertOnboardPage
    When Admin bypass that expert
    And Expert go to ExpertHomePage
    And Expert press Start Working Button
    Then Expert should see the ExpertWorkspacePage
    # Start querying
    When I post a question
    And Expert claims the question
    Then I should see ProblemExpertIntroModal
    When I press GotIt button
    Then I should be in the same room with that expert