import requests
import allure
from allure_commons._allure import step
import pytest
from selene import have, browser
from utils import log_request, log_response


"""
1. Написать несколько тестов на demoshop на добавление 
товаров в корзину через API с проверкой корзины через UI.

2. Автоматизировать у себя в коде логирование в allure

3. Задача со *: реализовать логирование реквеста в аллюр 
и в консоль https://demowebshop.tricentis.com/
"""

@allure.epic("demowebshop")
@allure.feature("Корзина")
@allure.story("Добавление товаров в корзину")
def test_add_to_cart():
    # Given
    """
    Добавить товар в корзину через API
    """
    with allure.step('add to cart'):
        url = 'https://demowebshop.tricentis.com/addproducttocart/details/38/1'
        log_request(url, 'POST')
        result = requests.post(url)
        log_response(result)


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

@allure.epic("demowebshop")
@allure.feature("Корзина")
@allure.story("Добавление нескольких товаров в корзину")
def test_add_multiple_items_to_cart():
    # Given
    """
    Добавить несколько товаров в корзину через API
    """
    with allure.step('add multiple items to cart'):
        # Добавляем первый товар
        url1 = 'https://demowebshop.tricentis.com/addproducttocart/details/38/1'
        log_request(url1, 'POST')
        result1 = requests.post(url1)
        log_response(result1)
        
        # Добавляем второй товар
        url2 = 'https://demowebshop.tricentis.com/addproducttocart/details/43/1'
        log_request(url2, 'POST')
        result2 = requests.post(url2)
        log_response(result2)

    # When
    with allure.step('open browser'):
        browser.open('')

    # Then
    """
    Проверить что в корзине 2 товара
    """
    with allure.step('check cart'):
        browser.element('[class="cart-qty"]').should(have.text('2'))