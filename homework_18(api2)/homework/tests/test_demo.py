import allure
from allure_commons._allure import step
from api import api
from ui import cart


@allure.epic("demowebshop")
@allure.feature("Корзина")
@allure.story("Добавление товаров в корзину")
def test_add_product_to_cart():
    # Given
    """
    Добавить товар в корзину через API
    """
    with allure.step('Add product to cart'):
        result = api.add_product_to_cart(product_id=31, quantity=1)

    with allure.step('Get cookie'):
        cookie = api.get_cookies(result)

    # When
    with allure.step('Set cookie and open cart'):
        cart.set_cookie_and_open_cart(cookies=cookie)

    # Then
    """
    Проверить что товар в корзине добавлен
    """
    with allure.step('Check success adding to cart'):
        cart.cart_should_product(product='14.1-inch Laptop')


@allure.epic("demowebshop")
@allure.feature("Корзина")
@allure.story("Добавление нескольких штук товара в корзину")
def test_add_multiple_product_to_cart():
    # Given
    """
    Добавить несколько товаров в корзину через API
    """
    with allure.step('Add multiple products to cart'):
        result = api.add_product_to_cart(product_id=31, quantity=3)

    with allure.step('Get cookie'):
        cookie = api.get_cookies(result)

    # When
    with allure.step('Set cookie and open cart'):
        cart.set_cookie_and_open_cart(cookies=cookie)

    # Then
    """
    Проверяем что в корзине несколько товаров
    """
    with allure.step('Check success adding multiple products to cart'):
        cart.cart_should_product_with_quantity(product='14.1-inch Laptop', quantity=3)


@allure.epic("demowebshop")
@allure.feature("Корзина")
@allure.story("Проверка что корзина пустая при добавлении товара с нулевым количеством")
def test_add_product_to_cart_with_null_quantity():
    # Given
    """
    Добавить товар в корзину через API
    """
    with allure.step('Add product to cart with null quantity'):
        result = api.add_product_to_cart(product_id=31, quantity=0)

    with allure.step('Get cookie'):
        cookie = api.get_cookies(result)

    # When
    with allure.step('Set cookie and open cart'):
        cart.set_cookie_and_open_cart(cookies=cookie)

    # Then
    """
    Проверяем что в корзине нет товаров
    """
    with allure.step('Check empty cart'):
        cart.cart_should_be_empty()


@allure.epic("demowebshop")
@allure.feature("Корзина")
@allure.story("Добавление нескольких наименований товаров в корзину")
def test_add_multiple_product_to_cart_with_different_names():
    # Given
    """
    Добавить несколько товаров в корзину через API
    """
    with allure.step('Add multiple products to cart with different names'):
        result = api.add_product_to_cart(product_id=31, quantity=1)


    with allure.step('Get cookie'):
        cookie = api.get_cookies(result)

    with allure.step('Add second product to cart with different names'):
        api.add_product_with_cookies(cookies=cookie, product_id=43, quantity=1)

    # When
    with allure.step('Set cookie and open cart'):
        cart.set_cookie_and_open_cart(cookies=cookie)

    # Then
    """
    Проверяем что в корзине несколько товаров
    """
    with allure.step('Check success adding multiple products to cart'):
        cart.cart_should_multiple_products(product1='14.1-inch Laptop', product2='Smartphone')