import requests
import allure
from allure_commons._allure import step
import pytest
import selene
from selene import have, browser


"""
1. Написать несколько тестов на demoshop на добавление товаров в корзину через API с проверкой корзины через UI.

2. Автоматизировать у себя в коде логирование в allure

3. Задача со *: реализовать логирование реквеста в аллюр и в консоль https://demowebshop.tricentis.com/

4) Если хочешь, чтобы в логах был красивый читаемый текст вместо абракадабры, то нужно заменить в методе log_to_console строчку
в HTTP Response Body:
{result.text}
на
{json.dumps(json.loads(result.text), indent=4, ensure_ascii=False) if result.text else "None"}
"""

@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    browser.config.base_url = 'https://demowebshop.tricentis.com/'
    browser.config.type_by_js = True

    yield

    browser.quit()



@allure.epic("demowebshop")
@allure.feature("Корзина")
@allure.story("Добавление товаров в корзину")
def test_add_to_cart():
    # Given
    """
    Добавить товар в корзину через API
    """
    with allure.step('add to cart'):
        result = requests.post('https://demowebshop.tricentis.com/addproducttocart/details/38/1')
        print(result.status_code)

    # When
    with allure.step('open browser'):
        browser.open('')

    # Then
    """
    Проверить что в корзине 1 товар
    Проверить что товар в корзине добавлен
    """
    with allure.step('check cart'):
        browser.element('[class="cart-qty"]').should(have.text('1'))