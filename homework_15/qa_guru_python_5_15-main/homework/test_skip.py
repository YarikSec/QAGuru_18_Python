"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture(
    params=[
        # Десктоп
        {'width': 1920, 'height': 1080, 'env': 'desktop'},
        {'width': 1366, 'height': 768, 'env': 'desktop'},
        # Мобильные
        {'width': 480, 'height': 800, 'env': 'mobile'},
        {'width': 375, 'height': 812, 'env': 'mobile'}
    ]
)
def browser_setup(request):
    params = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = params['width']
    browser.config.window_height = params['height']
    
    yield params
    
    browser.quit()


def test_github_desktop(browser_setup):
    if browser_setup['env'] == 'mobile':
        pytest.skip('Десктопный тест пропущен, т.к. соотношение сторон мобильное')

    browser.open('')
    browser.all('button').element_by(have.text('Sign up')).click()


def test_github_mobile(browser_setup):
    if browser_setup['env'] == 'desktop':
        pytest.skip('Мобильный тест пропущен, т.к. разрешение окна десктопное')

    browser.open('')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
