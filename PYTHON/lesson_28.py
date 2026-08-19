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
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items: list = []
        self.total: int = 0

    def add_item(self, position: str, amount: int):
        self.items.append({"position": position, "amount": amount})
        self.total += amount

    @staticmethod
    def validate_phone(phone: str) -> bool:
        return len(phone) == 10 and phone.isdigit()


order_1 = Order("Фёдор Сумкин")
order_1.add_item("Чехол для кольца всевластия", 1)
order_1.add_item("Удобные тапочки", 1)

print("Имя клиента:", order_1.customer_name)
print("Товары:", order_1.items)
print("Общая стоимость:", order_1.total)

print(order_1.validate_phone("1234567890"))
print(Order.validate_phone("1234567890"))