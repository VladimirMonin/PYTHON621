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

em_3 = Employee.from_dict(employee_dict_3)

em_3_dict = em_3.to_dict()
em_3_dict["is_married"] = False

print(em_3.is_married)
