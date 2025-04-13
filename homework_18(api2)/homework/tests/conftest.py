import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    # browser.config.base_url = 'https://demowebshop.tricentis.com/'
    # browser.config.type_by_js = True

    # browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()