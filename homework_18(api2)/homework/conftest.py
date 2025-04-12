import pytest
import requests
from selene import browser
import allure
from utils import log_to_console


@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    browser.config.base_url = 'https://demowebshop.tricentis.com/'
    browser.config.type_by_js = True

    # browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    log_to_console()
    allure.attach(
        name='browser console logs',
        body=browser.get_js_logs(),
        attachment_type=allure.attachment_type.TEXT,
    )

    browser.quit()


# Фикстура для создания сессии API
@pytest.fixture
def api_session():
    session = requests.Session()
    yield session
    session.close()


# Фикстура для скриншота при падении теста
@pytest.fixture(autouse=True)
def make_screenshot_on_failure(request):
    yield
    if request.node.rep_call.failed:
        allure.attach(
            browser.take_screenshot(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )

# Хук для добавления информации о статусе теста в отчет
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)