"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from pytest_check import check

from homework_8.homework.models import Product, Cart

"""
) FAILED [ 22%]
Недостаточно товара 'book' на складе

test_shop.py:38 (TestProducts.test_product_buy)
self = <homework.test_shop.TestProducts object at 0x0000015B3A19B750>
product = <homework_8.homework.models.Product object at 0x0000015B3A19AFD0>

def test_product_buy(self, product):
# TODO напишите проверки на метод buy
assert product.buy(1000)
> assert product.buy(999)

====

Падают, увы, и другие тесты.

Хорошо бы чтобы я получил работу без ошибок.
"""


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def product_two():
    return Product("macbook", 2000, "This is a comp", 2000)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(1000)
        assert product.check_quantity(999)
        assert not product.check_quantity(1001)


    def test_product_buy(self, product):
        assert product.buy(1)
        assert product.buy(999)
        assert product.buy(0)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product, product_two, cart):
        assert cart.add_product(product, 1)
        cart.clear()

        with pytest.raises(ValueError):
            assert cart.add_product(product, -1)

        assert cart.add_product(product_two, 1999)

    def test_remove_product(self, product, product_two, cart):
        # Проверяю ошибку, если товара нет в корзине
        with pytest.raises(ValueError):
            assert cart.remove_product(product, 2)

        # Проверяю удаление продукта с remove_count < 0
        with pytest.raises(ValueError):
            assert cart.remove_product(product, -1)

        # Проверяю удаление продукта с remove_count = None
        cart.add_product(product)
        cart.remove_product(product)
        assert product not in cart.products

        # Проверяю удаление продукта с remove_count > quantity
        cart.add_product(product_two, 2)
        cart.remove_product(product_two, 3)
        assert product_two not in cart.products

        # Проверяю удаление продукта с "0 < remove_count < quantity"
        cart.add_product(product_two, 2)
        cart.remove_product(product_two, 1)
        assert cart.products[product_two] == 1

    def test_clear(self, product, cart):
        """
        Проверяю очистку корзины
        Добавляю продукт, очищаю корзину
        Проверяю, что корзина пустая
        """
        cart.add_product(product)
        cart.clear()
        assert not cart.products

    def test_get_total_price(self, product, product_two, cart):
        cart.add_product(product)
        cart.add_product(product_two, 2)
        assert cart.get_total_price() == 4100

    def test_buy(self, product, product_two, cart):
        with pytest.raises(ValueError):
            assert cart.buy()

        cart.add_product(product)
        cart.add_product(product_two, 2)
        assert cart.buy() is True

        # Проверил, что корзина пустая
        assert not cart.products
    

    def test_buy_insufficient_quantity(self, product, cart):
        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError) as ex_info:
            assert cart.buy()
        assert "Недостаточно товаров на складе" in str(ex_info.value)


        