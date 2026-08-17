"""
Урок 27. Объектно-ориентированное программирование на Python. Классы, объекты, `self` и инициализатор `__init__`.
"""

"""
Классы в Python называются через UpperCamelCase. Это означает: никаких пробелов, никаких нижних подчёркиваний. Каждое новое слово начинается с заглавной буквы.

Принцип нейминга тот же, что и в переменных: это существительные, прилагательные, хотя в целом иногда допускаются и глаголы. Двух, трёх, максимум четырёх слов будет достаточно для названия класса.
"""


class Car: ...


car1 = Car()
car2 = Car()


print(type(car1))
print(type(car2))

# <class '__main__.Car'>

car1.name = "Лада"
car2.name = "Мерседес"

print(car1.name)
print(car2.name)


class Car2:
    name: str = "Лада баклажан"
    year: int = 2020
    model: str = "Лада"


car3 = Car2()
car4 = Car2()

print(car3.name)
print(car3.year)

car4.model = "Мерседес"
print(car4.model)


class Car3:
    def __init__(self, name: str, year: int, model: str):
        print(self)
        print(id(self))
        self.name = name
        self.year = year
        self.model = model


new_car = Car3("Лада", 1995, "Калина")
new_car2 = Car3("M3", 1995, "BMW")

""""<__main__.Car3 object at 0x00000215A6808EC0>
2292011011776
<__main__.Car3 object at 0x00000215A680CF50>
2292011028304"""


class Dog:
    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color

    def voice(self):
        print(f"Гав! Говорит {self.name}")


dog1 = Dog("Чипсик", 5, "серый")
dog2 = Dog("Стрипс", 3, "белый")

dog1.voice()
dog2.voice()


class Cat:
    def __init__(apple, name: str, age: int):
        apple.name = name
        apple.age = age

    def voice(apple):
        print(apple.name, "Мяу!")


cat1 = Cat("Рокки", 2)
cat1.voice()

TEXT_DOC = "./lesson_27.txt"


class TextDocument:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> list[str]|None:
        """
        Читает документ и возвращает список строк
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            try:
                raw_data = file.readlines()
                return [line.strip() for line in raw_data]
            except FileNotFoundError:
                return None


    def write(self, *lines: str) -> None:
        """
        Пишет в документ
        """
        with open(self.file_path, "a", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")

    def append(self, *lines: str) -> None:
        """
        Дозапишет в документ
        """
        with open(self.file_path, "a", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")


txt_doc = TextDocument(TEXT_DOC)
txt_doc.write("Hello, world!", "This is a test.")
txt_doc.append("Another line.", "And another one.")
print(txt_doc.read())

import json

class ConfigData:
    def __init__(self, config_file_path: str):
        self.config_file_path = config_file_path
        self.config_data: dict = {}
        self.load_config()

    def load_config(self):
        with open(self.config_file_path, "r", encoding="utf-8") as file:
            self.config_data = json.load(file)


config_path = "./config.json"

config_data = ConfigData(config_path)
print(config_data.config_data)


