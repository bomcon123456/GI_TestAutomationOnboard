from behave.fixture import fixture, use_fixture, use_fixture_by_tag

from utils.drivers import DriverWrapper


@fixture
def asker_setup(context):
    asker = DriverWrapper(url='https://asker-query.got-it.io/')
    context.asker = asker
    yield context.asker
    context.asker.driver.quit()


@fixture
def expert_setup(context):
    expert = DriverWrapper(url='https://expert-query.got-it.io/')
    context.expert = expert
    yield context.expert
    context.expert.driver.quit()


@fixture
def admin_setup(context):
    admin = DriverWrapper(url='https://admin-query.got-it.io/')
    context.admin = admin
    yield context.admin


@fixture
def query_asker_expert_admin_setup(context):
    asker_fixture = use_fixture(asker_setup, context)
    expert_fixture = use_fixture(expert_setup, context)
    admin_fixture = use_fixture(admin_setup, context)
    return [asker_fixture, expert_fixture, admin_fixture]


fixture_registry = {
    "fixture.full_setup": query_asker_expert_admin_setup,
    "fixture.asker": asker_setup,
    "fixture.expert": expert_setup,
    "fixture.admin": admin_setup,
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)
