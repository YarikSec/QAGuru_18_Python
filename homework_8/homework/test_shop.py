"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from pytest_check import check

from homework_8.homework.models import Product, Cart


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
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)
        assert product.check_quantity(999)
        assert not product.check_quantity(1001)
        # check(product.check_quantity(1000))
        # check(product.check_quantity(999))
        # check(not product.check_quantity(1001))


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1000)
        assert product.buy(0)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001)
        with pytest.raises(ValueError):
            assert product.buy(-1)
        # assert not product.buy(1001)
        # assert not product.buy(-1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product, product_two, cart):
        assert cart.add_product(product)

        with pytest.raises(ValueError):
            assert cart.add_product(product, -1)

        assert cart.add_product(product_two, 2)

    def test_remove_product(self, product, product_two, cart):
        cart.add_product(product)
        cart.add_product(product_two, 2)
        assert cart.remove_product(product)

        with pytest.raises(ValueError):
            assert cart.remove_product(product, 2)

        assert cart.remove_product(product, 1)

    def test_clear(self, product, cart):
        cart.add_product(product)
        assert cart.clear()

    def test_get_total_price(self, product, product_two, cart):
        cart.add_product(product)
        cart.add_product(product_two, 2)
        assert cart.get_total_price() == 4100

    def test_buy(self, product, product_two, cart):
        with pytest.raises(ValueError):
            assert cart.buy()

        cart.add_product(product)
        cart.add_product(product_two, 2)
        assert cart.buy()

        # Проверил, что корзина пустая
        assert not cart.products

        