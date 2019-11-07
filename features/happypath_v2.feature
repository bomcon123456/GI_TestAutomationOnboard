Feature: Implement happy path for QueryChat ask flow

  @asker_sign_up
  Scenario: Asker log in by signing up
    Given Asker accesses to the sign up modal
    When Asker inserts her/his email
    And Askert inserts her/his password
    And Asker completes the sign up process
    Then Asker will be redirected to homepage signed in

  @expert_sign_up
  Scenario: Expert log in by signing up
    Given Expert accesses to the sign up dropdown
    When Expert inserts her/his email
    And Expert inserts her/his password
    And Expert completes the sign up process
    Then Expert will be redirected to homepage signed in

  @happy_path_flow
  Scenario: Asker and Expert Sign up then match each other
    # will use execute_steps() to run all of the @asker_sign_up steps
    Given Asker Logged in by signing up
    # will use execute_steps() to run all of the @expert_sign_up steps
    And Expert Logged in by signing up
    And Expert started working
    When Asker posts a question
    And Expert claims that question
    Then Asker and Expert will be in a chat session