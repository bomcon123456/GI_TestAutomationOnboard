Test Automation Training exercise
=================================

Objective
---------
Implement __happy path__ for QueryChat ask flow

Requirements
------------
- Make sure all tests run on __DEV__ environment:
```
- Asker:  https://asker-query.got-it.io/
- Explainer: https://expert-query.got-it.io/
- Admin: https://admin-query.got-it.io/
```
- Write clean code and follow Python code formats and conventions
- Use explicit waits and CSS selectors for locators
- Create one class to store all configurations and constants
- One main test runner class (eg. https://selenium-python.readthedocs.io/getting-started.html#using-selenium-to-write-tests)
- Other than that, feel free to build your own project structure

Implementation phases
---------------------

#### Preprare Expert 
- Sign up a new Expert account and set up the account ready to work (ie. Able to go to Workspace and wait for a question to be routed)
- Use admin api to bypass the onboarding process for that expert
- Make sure Expert is navigated to Home page

#### Preprare asker
- Sign up a new asker
- Use the free session to post a question and wait to be routed to an Expert

#### Connect Asker and Expert
- Expert clicks Start Working to go to Workspace
- Asker posts a question
- Expert bids and claims the questions
- Assert both asker and expert are in a chat session