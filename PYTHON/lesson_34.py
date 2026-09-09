"""
Lesson 34: Python Dataclasses, Pydantic, Pydanticsettings
"""

from dataclasses import dataclass, field, asdict
# uv add pydantic
from pydantic import BaseModel, Field, ValidationError

# Создадим свой AgeEmployeeException

class AgeEmployeeException(Exception):
    pass


class Employee(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    skills: list[str]
    position: str
    salary: float

employee_dict_1 = {
    "name": "Шарик",
    "age": 2,
    "position": "Пес",
    "salary": 1000.0,
    "skills": ["жаловаться", "фотографировать", "покупать кеды на Озон"],
}

employee_dict_2 = {
    "name": "Матроскин",
    "age": 500,
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

# Пытаюсь создать Матроскина которому 200 лет

try:
    em_2 = Employee(**employee_dict_2)
except ValidationError as ex:
    for error in ex.errors():
        print(error)

