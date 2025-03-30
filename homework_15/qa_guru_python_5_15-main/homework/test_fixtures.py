"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[('1920', '1080'), ('1024', '768')], ids=lambda x: f'{x[0]}x{x[1]}')
def browser_desktop(request):
    width, height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=[('400', '800'), ('375', '667')], ids=lambda x: f'{x[0]}x{x[1]}')
def browser_mobile(request):
    width, height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


def test_github_desktop(browser_desktop):
    browser.open('')
    browser.all('button').element_by(have.text('Sign up')).click()


def test_github_mobile(browser_mobile):
    browser.open('')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
