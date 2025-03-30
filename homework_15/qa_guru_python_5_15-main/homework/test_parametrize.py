"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture
def browser_config(request):
    config = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = config['width']
    browser.config.window_height = config['height']
        
    yield
    
    browser.quit()


@pytest.mark.parametrize('browser_config', [
    {'width': 1920, 'height': 1080, 'env': 'desktop'}
], indirect=True)
def test_github_desktop(browser_config):
    browser.open('')
    browser.all('button').element_by(have.text('Sign up')).click()


@pytest.mark.parametrize('browser_config', [
    {'width': 480, 'height': 800, 'env': 'mobile'}
], indirect=True)
def test_github_mobile(browser_config):
    browser.open('')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
