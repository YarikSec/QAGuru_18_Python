class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if self.quantity >= quantity:
            return True
        else:
            print(f"\nНедостаточно товара '{self.name}' на складе")
            return False

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if not self.check_quantity(quantity):
            raise ValueError(f"Недостаточно товара '{self.name}' на складе")
        
        self.quantity -= quantity
        return True
        

        

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if buy_count < 0:
            raise ValueError("Количество товара не может быть отрицательным")
        if product in self.products:
            self.products[product] += buy_count
            return True
        else:
            self.products[product] = buy_count
            return True

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product not in self.products:
            raise ValueError("Товара нет в корзине")

        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        elif 0 < remove_count < self.products[product]:
            self.products[product] -= remove_count
            if self.products[product] == 0:
                del self.products[product]
        else:
            raise ValueError("Количество товара не может быть отрицательным")

    def clear(self):
        return self.products.clear()

    def get_total_price(self) -> float:
        return sum(product.price * count for product, count in self.products.items())

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        if not self.products:
            raise ValueError("Корзина пустая")

        not_available = [f"{product.name} (требуется: {count}, в наличии: {product.quantity})"
                for product, count in self.products.items()
                if not product.check_quantity(count)]
        if not_available:
            raise ValueError(f"Недостаточно товаров на складе:\n {'\n'.join(not_available)}")
        
     
        for product, count in self.products.items():
            product.buy(count)
            
        self.clear()
        return True