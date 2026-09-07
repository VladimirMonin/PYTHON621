"""
Lesson 33: Python Dataclasses
"""

from dataclasses import dataclass, field


@dataclass
class Employee:
    name: str
    age: int
    skills: list = field(default_factory=list)
    position: str = "Безработный"
    salary: float = 0.0

    def __str__(self):
        return f"Сотрудник: {self.name}, Возраст: {self.age}, Должность: {self.position}, Зарплата: {self.salary}\nSkills: {self.skills}"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def to_dict(self):
        return self.__dict__


employee_dict_1 = {
    "name": "Шарик",
    "age": 2,
    "position": "Пес",
    "salary": 1000.0,
    "skills": ["жаловаться", "фотографировать", "покупать кеды на Озон"],
}

employee_dict_2 = {
    "name": "Матроскин",
    "age": 3,
    "position": "Кот",
    "salary": 5000.0,
    "skills": ["манипулировать Шариком", "пить молоко"],
}


employee_dict_3 = {
    "name": "Дядя Фёдор",
    "age": 12,
    "position": "Мальчик",
    "salary": 15000.0,
    "skills": ["сбегать от родителей", "неправильно есть бутерброды"],
}

employee_dict_4 = {
    "name": "Заяц",
    "age": 2,
    "position": "Фото-дичь",
    "salary": 0.0,
    "skills": ["позировать на фото", "убегать"],
}


employee_1 = Employee.from_dict(employee_dict_1)

print(employee_1)

employee_2 = Employee.from_dict(employee_dict_2)
print(employee_2)
print(employee_1)


employee_dict_5 = {"name": "Печкин", "age": 45}

employee_5 = Employee(**employee_dict_5)
print(employee_5)

employee_5.skills.append("Езда на велосипеде")
print(employee_5)

# А теперь пример с обычным классом и общим списком на всех вместе)


class BaseEmployee:
    def __init__(
        self,
        name: str,
        age: int,
        position: str = "Безработный",
        salary: float = 0.0,
        skills: list = [],
    ):
        self.name = name
        self.age = age
        self.position = position
        self.salary = 0.0
        self.skills = skills


be_1 = BaseEmployee(
    "Шарик",
    2,
    "Пес",
    1000.0,
    ["жаловаться", "фотографировать", "покупать кеды на Озон"],
)
be_2 = BaseEmployee(
    "Матроскин", 3, "Кот", 5000.0, ["манипулировать Шариком", "пить молоко"]
)

print(be_2.skills)
print(be_1.skills)

be_3 = BaseEmployee("Печкин", 50)
be_4 = BaseEmployee("Заяц", 2)

be_3.skills.append("Потирать усы")

print(be_4.skills)


# Правильно это можно сделать так!
# class BaseEmployee:
#     def __init__(
#         self,
#         name: str,
#         age: int,
#         position: str = "Безработный",
#         salary: float = 0.0,
#         skills: list | None = None,
#     ):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary
#         self.skills = [] if skills is None else skills