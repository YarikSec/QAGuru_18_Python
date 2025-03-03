from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com')

    s('.search-input-container').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example')
    s('#query-builder-test').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.link_text('Привет от 27го потока QA.GURU!!!')).should(be.visible)
