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

