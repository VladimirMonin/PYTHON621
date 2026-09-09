"""
Lesson 34: Python Dataclasses, Pydantic, Pydanticsettings
"""

from dataclasses import dataclass, field, asdict

# uv add pydantic
from pydantic import BaseModel, Field, ValidationError, field_validator

# Создадим свой AgeEmployeeException


class AgeEmployeeException(Exception):
    pass


class Employee(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=0, le=120)
    skills: list[str] = Field(min_length=3, max_length=20)
    position: str = Field(min_length=3, max_length=20)
    salary: float = Field(ge=0)

    @field_validator("name", mode="before")
    @classmethod
    def validate_name(cls, value: str) -> str:
        return value.strip()


employee_dict_1 = {
    "name": "                              Шарик                                       ",
    "age": 2,
    "position": "Пес",
    "salary": 1000.0,
    "skills": ["жаловаться", "фотографировать", "покупать кеды на Озон"],
}

employee_dict_2 = {
    "name": "Матроскин",
    "age": 119,
    "position": "Кот",
    "salary": 5000.0,
    "skills": [
        "манипулировать Шариком",
        "пить молоко",
        "Безудержный парашютный спорт до потери всех своих девяти жизней",
    ],
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


em_1 = Employee(**employee_dict_1)
print(em_1.name)
