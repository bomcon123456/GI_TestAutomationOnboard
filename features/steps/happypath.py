from behave import *

use_step_matcher("re")


@given("Asker/ Expert signed up, Expert has been approved")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Asker/ Expert signed up, Expert has been approved')


@when("Asker post a quest then Expert bids and claims the question")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Asker post a quest then Expert bids and claims the question')


@then("Asker and Expert are in a chat session")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Asker and Expert are in a chat session')
