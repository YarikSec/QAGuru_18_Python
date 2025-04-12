import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    browser.config.base_url = 'https://demowebshop.tricentis.com/'
    browser.config.type_by_js = True

    yield

    browser.quit()