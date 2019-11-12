Feature: QueryChat ask flow
  As an user,
  After logging in at QueryChat and redirected to the homepage,
  I can ask question and receives answer from the expert.


  @fixture.full_setup
  Scenario: I/Expert log(s)b in by signing up
    Given I'm on Asker Home Page
    When I open Asker SignUp Modal
    And I enter email
    And I enter password
    And I enter confirm password
    And I press sign up
    Then Asker's Terms Conditions Modal should be presented
    When I press Next
    Then I should be redirected to Asker Home Page
    # Expert register
    When Expert is on Expert Home Page
    And Expert open Signup Dropdown
    And Expert enters email
    And Expert enters password
    And Expert enters confirm password
    And Expert click Sign Up button
    Then Expert's Terms Conditions Modal should be presented
    When Expert presses Next
    Then Expert should be redirected to Expert Onboard Page
    When Admin bypass that expert
    And Expert go to Expert Home Page
    And Expert press Start Working Button
    Then Expert should see the Expert Workspace Page
    # Start querying
    When I post a question
    And Expert claims the question
    Then I should see Problem Expert Intro Modal
    When I press GotIt button
    Then I should be in the same room with that expert