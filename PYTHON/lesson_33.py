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

    def __str__(self):
        return f"Сотрудник: {self.name}, Возраст: {self.age}, Должность: {self.position}, Зарплата: {self.salary}"

    def __repr__(self):
        """
        Писать его нет смысла - это делает @dataclass - выглядит это примерно так
        Это служебное представление объекта удобное для сериализации
        """
        return f"Employee(name='{self.name}', age={self.age}, position='{self.position}', salary={self.salary})"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def to_dict(self):
        return self.__dict__


employee_1 = Employee("Шарик", 2, "Пес", 1000.0)
employee_2 = Employee("Матроскин", 3, "Кот", 5000.0)

# Сбросить это в строку сериализация
employee_1_str = repr(employee_1)
print(employee_1_str)

# Обратно в объект десериализация
employee_1_back = eval(employee_1_str)


print(employee_1)
print(employee_2)


employee_dict_3 = {
    "name": "Дядя Фёдор",
    "age": 12,
    "position": "Мальчик",
    "salary": 15000.0,
}

employee_dict_4 = {"name": "Заяц", "age": 2, "position": "Фото-дичь", "salary": 0.0}

employee_3 = Employee.from_dict(employee_dict_3)
employee_4 = Employee.from_dict(employee_dict_4)

dict_4 = employee_4.to_dict()

print(dict_4)

# Список персонажей
list_of_employees = [employee_1, employee_2, employee_3, employee_4]

# Сбрасываю их в JSON файл
import json
FILE = "employees.json"

dicts_list_of_employees = [employee.to_dict() for employee in list_of_employees]


with open(FILE, "w", encoding="utf-8") as file:
    json.dump(dicts_list_of_employees, file, indent=4, ensure_ascii=False)


# А теперь обратно!

with open(FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

list_of_employees_from_json = [Employee.from_dict(employee_dict) for employee_dict in data]

print(list_of_employees_from_json)
[print(employee) for employee in list_of_employees_from_json]