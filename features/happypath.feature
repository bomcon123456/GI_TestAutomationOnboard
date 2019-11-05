Feature: Implement happy path for QueryChat ask flow

  Scenario: Asker and Expert Sign up then match each other
    Given Asker/ Expert signed up, Expert has been approved
    When Asker post a quest then Expert bids and claims the question
    Then Asker and Expert are in a chat session