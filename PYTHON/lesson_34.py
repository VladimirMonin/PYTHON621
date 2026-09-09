"""
Lesson 34: Python Dataclasses, Pydantic, Pydanticsettings

gt - больше чем
lt - меньше чем
ge - больше или равно
le - меньше или равно
min_lenth - минимальная длина
max_lenth - максимальная длина
pattern= - соответствме регулярке
EmailStr - проверка на emeil
HttpUrl - ссылка в интернете
AnyUrl - более мягкий вариант
IPvAnyAddress
PaymentCardNumber
date
time
datetime


uv add pydantic-extra-types
from pydantic_extra_types.phone_numbers import PhoneNumber
PhoneNumber("89001234567")

uv add "pydantic[email,timezone]" "pydantic-extra-types[all]" pydantic-settings
"""

from dataclasses import dataclass, field, asdict

# uv add pydantic
from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    field_validator,
    EmailStr,
    HttpUrl,
)
from pydantic_extra_types.phone_numbers import PhoneNumber
# Создадим свой AgeEmployeeException


class AgeEmployeeException(Exception):
    pass


class Employee(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    skills: list[str] = Field(min_length=3, max_length=20)
    position: str = Field(min_length=3, max_length=20)
    salary: float = Field(ge=0)

    # Новые поля
    email: EmailStr
    phone: PhoneNumber
    portfolio: HttpUrl | None = None

    @field_validator("name", mode="before")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()

        if not 3 < len(value) < 20:
            raise ValueError("Имя должно быть от 3 до 20 символов")

        return value


employee_dict_1 = {
    "name": "Шарик",
    "age": 2,
    "position": "Пес",
    "salary": 1000.0,
    "skills": ["жаловаться", "фотографировать", "покупать кеды на Озон"],
    "email": "sharik@example.com",
    "phone": "+77011234567",
    "portfolio": "https://sharik.example.com",
}

employee_dict_2 = {
    "name": "Матроскин",
    "age": 119,
    "position": "Кот",
    "salary": 5000.0,
    "skills": [
        "манипулировать Шариком",
        "пить молоко",
        "парашютный спорт",
    ],
    "email": "matroskin@@prostokvashino",
    "phone": "кот позвонит сам",
    "portfolio": "трактор",
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


# Создаем Шарика
em_1 = Employee(**employee_dict_1)
print(em_1)

# Dump -> JSON + Dict
em_1_json = em_1.model_dump_json(indent=4)
print(type(em_1_json))
print(em_1_json)

em_1_to_dict = em_1.model_dump()
print(type(em_1_to_dict))
print(em_1_to_dict)

# Десериализация DICT -> Employee
# Вариант 1. Классика
em_1 = Employee(**em_1_to_dict)
# Вариант 2. Более наглядный
em_1 = Employee.model_validate(em_1_to_dict)

# Десериализация JSON -> Employee
em_1 = Employee.model_validate_json(em_1_json)
