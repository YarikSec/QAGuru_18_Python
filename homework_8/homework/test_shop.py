"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework_8.homework.models import Product, Cart

@pytest.fixture
def product_book():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def product_macbook():
    return Product("macbook", 2000, "This is a comp", 2000)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product_book):
        assert product_book.check_quantity(1000)
        assert product_book.check_quantity(999)

    def test_product_check_quantity_more_than_available(self, product_book):
        assert not product_book.check_quantity(1001)


    def test_product_buy(self, product_book):
        assert product_book.buy(1)
        assert product_book.buy(999)
        assert product_book.buy(0)

    def test_product_buy_more_than_available(self, product_book):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product_book.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product_book, product_macbook, cart):
        assert cart.add_product(product_book, 1)
        cart.clear()

        assert cart.add_product(product_macbook, 1999)

    def test_error_add_product_negative_quantity(self, product_book, cart):
        with pytest.raises(ValueError):
            assert cart.add_product(product_book, -1)

    """
    Тесты на удаления продуктов из корзины
    """
    def test_error_remove_product_not_in_cart(self, product_book, product_macbook, cart):
        """
        Проверяю ошибку, если товара нет в корзине
        """
        with pytest.raises(ValueError):
            assert cart.remove_product(product_book, 1), cart.remove_product(product_macbook, 2)

    def test_error_remove_product_negative_quantity(self, product_book, cart):
        """
        Проверяю ошибку, если remove_count < 0
        """
        with pytest.raises(ValueError):
            assert cart.remove_product(product_book, -1)

    def test_remove_product_count_none(self, product_book, cart):
        """
        Проверяю удаление продукта с remove_count = None
        """
        cart.add_product(product_book)
        cart.remove_product(product_book)
        assert product_book not in cart.products

    def test_remove_product_count_more_than_quantity(self, product_macbook, cart):
        """
        Проверяю удаление продукта с remove_count > quantity
        """
        cart.add_product(product_macbook, 2)
        cart.remove_product(product_macbook, 3)
        assert product_macbook not in cart.products

    def test_remove_product_count_in_quantity(self, product_macbook, cart):
        """
        Проверяю удаление продукта с "0 < remove_count < quantity"
        """
        cart.add_product(product_macbook, 2)
        cart.remove_product(product_macbook, 1)
        assert cart.products[product_macbook] == 1


    def test_clear(self, product_book, cart):
        """
        Проверяю очистку корзины
        Добавляю продукт, очищаю корзину
        Проверяю, что корзина пустая
        """
        cart.add_product(product_book)
        cart.clear()
        assert not cart.products

    def test_get_total_price(self, product_book, product_macbook, cart):
        cart.add_product(product_book)
        cart.add_product(product_macbook, 2)
        assert cart.get_total_price() == 4100

    def test_buy(self, product_book, product_macbook, cart):
        cart.add_product(product_book)
        cart.add_product(product_macbook, 2)
        assert cart.buy() is True

        # Проверил, что корзина пустая
        assert not cart.products

    def test_buy_empty_cart(self, cart):
        with pytest.raises(ValueError) as ex_info:
            assert cart.buy()
        assert "Корзина пустая" in str(ex_info.value)
    

    def test_buy_insufficient_quantity(self, product_book, product_macbook, cart):
        cart.add_product(product_book, product_book.quantity + 1)
        cart.add_product(product_macbook, product_macbook.quantity + 1)
        with pytest.raises(ValueError) as ex_info:
            assert cart.buy()
        assert "Недостаточно товаров на складе" in str(ex_info.value)


        