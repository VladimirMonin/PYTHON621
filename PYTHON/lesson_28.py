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
        return f"{self.name} - {self.price} руб., {self.quantity} шт. Общая стоимость: {self.total_price} руб."



item_1 = Item("Чебурек", 100, "Выпечка", 5)
item_2 = Item("Котлета", 50, "Мясные блюда", 2)
print(item_1)
print(item_2)

data_item_3 = {"name": "Пюре", "price": 40, "category": "Гарнир", "quantity": 1}
# item_3 = Item(name=data_item_3["name"], price=data_item_3["price"], category=data_item_3["category"], quantity=data_item_3["quantity"])

item_3 = Item(**data_item_3)
print(item_3)

