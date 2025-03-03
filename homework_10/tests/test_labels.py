import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Проверяем текст Issue')
    allure.dynamic.link('https://github.com', name='Testing')
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s('.search-input-container').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с названием"):
        s(by.link_text('Привет от 27го потока QA.GURU!!!')).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "YAQA")
@allure.feature("Задачи в репозитории")
@allure.story("Проверяем текст Issue")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s('.search-input-container').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с названием"):
        s(by.link_text('Привет от 27го потока QA.GURU!!!')).should(be.visible)
