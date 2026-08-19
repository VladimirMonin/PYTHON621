"""
Занятие №28: Анатомия класса и связи между объектами
- Методы экземпляра
- Методы класса
- Аттрибуты экземпляра
- Аттрибуты класса
"""

"""Заказ = Словарь
Данные между функцями передаются
через словари

create_order()
add_item()
calculate_total()"""

class Order:
    available_regions = ["Шир", "Лихолесье", "Мордор"]

    def __init__(self, customer_name: str, region: str):
        self.customer_name = customer_name
        self.items: list = []
        self.total: int = 0
        self.region = region

    def add_item(self, position: str, amount: int):
        self.items.append({"position": position, "amount": amount})
        self.total += amount

    def set_region(self, region: str):
        if region in self.available_regions:
            self.region = region
        else:
            raise ValueError("Недопустимый регион")


    @classmethod
    def set_available_regions(cls, regions: list):
        cls.available_regions = regions

    @staticmethod
    def validate_phone(phone: str) -> bool:
        return len(phone) == 10 and phone.isdigit()


order_1 = Order("Фёдор Сумкин", "Шир")
Order.set_available_regions(["Шир", "Лихолесье", "Мордор", "Южное Бутово"])
order_1.set_region("Южное Бутово")
order_1.add_item("Чехол для кольца всевластия", 1)
order_1.add_item("Удобные тапочки", 1)

print("Имя клиента:", order_1.customer_name)
print("Товары:", order_1.items)
print("Общая стоимость:", order_1.total)
print("Регион:", order_1.region)

print(order_1.validate_phone("1234567890"))
print(Order.validate_phone("1234567890"))