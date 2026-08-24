"""
Занятие №28: Анатомия класса и связи между объектами
- Методы экземпляра
- Методы класса
- Аттрибуты экземпляра
- Аттрибуты класса
"""


class Item:
    """
    Класс представляющий товарную позицию в корзине
    """

    def __init__(self, name: str, price: float, category: str, quantity: int):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        self.total_price: float = self.price * self.quantity

    def __str__(self):
        return f"{self.name} - {self.price} руб., {self.quantity} шт. Общая стоимость: {self.total_price} руб.\n"


class Order:
    def __init__(self, *items: Item):
        self.items = list(items)

    def total_price(self):
        return sum(item.total_price for item in self.items)

    def add_item(self, item: Item):
        self.items.append(item)

    def __str__(self):
        return f"Ваш заказ:\n{', '.join(str(item) for item in self.items)}\nОбщая стоимость: {self.total_price()} руб."






item_1 = Item("Чебурек", 100, "Выпечка", 5)
item_2 = Item("Котлета", 50, "Мясные блюда", 2)

data_item_3 = {"name": "Пюре", "price": 40, "category": "Гарнир", "quantity": 1}
# item_3 = Item(name=data_item_3["name"], price=data_item_3["price"], category=data_item_3["category"], quantity=data_item_3["quantity"])

item_3 = Item(**data_item_3)

order = Order(item_1, item_2, item_3)
print(order)


# Агрегация - когда один объект содержит другой объект как его атрибут
# Композиция - когда один объект содержит другой объект как его составляющую

class Wheel:
    """
    Класс колесо
    """
    def __init__(self, size: int):
        self.size = size


class Car:
    """
    Класс машина
    """
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.wheels = [Wheel(size=18) for _ in range(4)]



##########################


class Cofnig:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.baseURL
        self.api_key
        self.model
        self.image
        self.load_config()

    def load_config(self):
        with open(self.file_path, "r", encoding="utf8") as file:
            config = json.load(file)
            self.baseURL = config["baseURL"]
            self.api_key = config["api_key"]
            self.model = config["model"]
            self.image = config["image"]


class OpenAIRequest:
    def __init__(self, config: Cofnig, message: str):
        self.config = config
        self.message = message
        self.client = OpenAI(
            base_url=self.config.baseURL,
            api_key=self.config.api_key,
        )


