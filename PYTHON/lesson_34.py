"""
Lesson 34: Python Dataclasses, Pydantic, Pydanticsettings
"""

from dataclasses import dataclass, field, asdict


# Создадим свой AgeEmployeeException

class AgeEmployeeException(Exception):
    pass


@dataclass
class Employee:
    name: str
    age: int
    skills: list = field(default_factory=list)
    position: str = "Безработный"
    salary: float = 0.0

    # post иницилизатор - фича датаклассов
    def __post_init__(self):
        print(f"Мы запустили постинициализатор!")
        self.age = self.__age_validator(self.age)


    def __str__(self):
        return f"Сотрудник: {self.name}, Возраст: {self.age}, Должность: {self.position}, Зарплата: {self.salary}\nSkills: {self.skills}"

    def __age_validator(self, age: int) -> int:
        if not isinstance(age, int):
           raise AgeEmployeeException("Возраст должен быть целым числом")
        if 0 < age < 120:
            return age
        raise AgeEmployeeException("Возраст должен быть от 1 до 119")



    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def to_dict(self):
        return asdict(self)


employee_dict_1 = {
    "name": "Шарик",
    "age": 2,
    "position": "Пес",
    "salary": 1000.0,
    "skills": ["жаловаться", "фотографировать", "покупать кеды на Озон"],
}

employee_dict_2 = {
    "name": "Матроскин",
    "age": 200,
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
except AgeEmployeeException as ex:
    print(ex)
    print("Кажется что-то с возрастом!")