"""
Lesson 33: Python Dataclasses
"""

from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int
    position: str
    salary: float


employee_1 = Employee("Шарик", 2, "Пес", 1000.0)
employee_2 = Employee("Матроскин", 3, "Кот", 5000.0)

# Сбросить это в строку сериализация
employee_1_str = str(employee_1)
print(employee_1_str)

# Обратно в объект десериализация
employee_1_back = eval(employee_1_str)



print(employee_1)
print(employee_2)

