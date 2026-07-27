# Lesson 13 - Функциональное программирование Ч2

import numbers
from unittest import result


def hello_user2(name, age):
    print(f"Привет, {name}! Тебе {age} лет.")


# Проверка позиционности аргументов
hello_user2("Алиса", 30)  # Привет, Алиса! Тебе 30 лет.
hello_user2(30, "Алиса")  # Привет, 30! Тебе Алиса лет.
hello_user2(age=30, name="Алиса")  # Привет, Алиса! Тебе 30 лет.

dict_params = {"name": "Алиса", "age": 30}
hello_user2(**dict_params)  # Привет, Алиса! Тебе 30 лет.

# Еще один пример распаковки
new_params = {"last_name": "Селезнева", **dict_params}
new_params = {"last_name": "Селезнева"}
new_params.update(dict_params)

favorite_dishes = ["Пицца", "Суши", "Борщ"]
print(*favorite_dishes)  # Пицца Суши Борщ
print(favorite_dishes[0], favorite_dishes[1], favorite_dishes[2])  # Пицца Суши Борщ
[print(dish + "\n") for dish in favorite_dishes]  # Пицца \n Суши \n Борщ


# Функции высшего порядка на примере создания кухонного комбайна с несколькими насадками.


# Функция - берет на вход картошку и чистит ее и отдает почищенную картошку
def potato_peeler(potato: str) -> str:
    return f"Почищенная {potato}"


# Функция берет морковку и отдает корейскую морковку
def carrot_shredder(carrot: str) -> str:
    return f"Корейская {carrot}"


# Как происходит приравнивание и присваивание имени функции в переменную? Важно функцию не вызывать: когда мы это делаем без скобок, у нас происходит создание ссылки на имя функции. Поэтому эта переменная становится вызываемым объектом и может вызываться, так как на самом деле она вызывает `print`.
банан = print
банан("Принт из банана!!!!!!!!!")

# Функция - комбайн берет на вход насадку и коллекцию овощей и отдает результат работы насадки на каждом из овощей

from typing import Callable


def food_processor(
    attachment: Callable[[str], str], vegetables: list[str]
) -> list[str]:
    result = []
    for vegetable in vegetables:
        result.append(attachment(vegetable))
    return result


# Картошка
potatoes = ["Картошка 1", "Картошка 2", "Картошка 3"]
result = food_processor(potato_peeler, potatoes)
print(
    result
)  # ['Почищенная Картошка 1', 'Почищенная Картошка 2', 'Почищенная Картошка 3']

# Функции высшего порядка в Python - map, filter, reduce, sorted, max, min, any, all и т.д. - это функции, которые принимают на вход другие функции и/или возвращают функции.

# result = map(potato_peeler, potatoes)
# print(result)  # <map object at 0x0000021B8C8F3A30>

result = list(map(potato_peeler, potatoes))
print(
    result
)  # ['Почищенная Картошка 1', 'Почищенная Картошка 2', 'Почищенная Картошка 3']

# Анонимные функции - lambda функции.
# lambda аргументы: выражение

# say_hello : Callable[...], str] и ... - это аннотация типа для функции, которая принимает на вход аргументы и возвращает строку.
def say_hello(name):
    return f"Привет, {name}!"
print(say_hello("Алиса"))  # Привет, Алиса!

potatoes = ["Картошка 1", "Картошка 2", "Картошка 3"]
result = list(map(lambda potato: f"Почищенная {potato}", potatoes))

# Проще, понятнее и короче
result = [f"Почищенная {potato}" for potato in potatoes]

# ФИЛЬТР - функция, которая принимает на вход функцию и коллекцию и возвращает коллекцию, состоящую из элементов, для которых функция возвращает True.

potatoes = [
    "Картошка 1",
    "Картошка 2",
    "Картошка 3",
    "Картошка 4 гнилая",
    "Картошка 5",
    "Картошка 6 гнилая",
]


def is_good_potato(potato: str) -> bool:
    return "гнилая" not in potato


good_potatoes = list(filter(is_good_potato, potatoes))
good_potatoes = list(filter(lambda potato: "гнилая" not in potato, potatoes))

# any, all - функции, которые принимают на вход коллекцию и возвращают True, если хотя бы один элемент коллекции (для any) или все элементы коллекции (для all) являются истинными.

all_true_list = [True, True, True]
any_true_list = [False, False, True]
false_list = [False, False, False]

print(all(all_true_list))  # True
print(all(any_true_list))  # False
print(all(false_list))  # False
print(any(all_true_list))  # True

# max, min - функции, которые принимают на вход коллекцию и возвращают максимальный или минимальный элемент коллекции соответственно. Поддерживают key - аргумент, который позволяет указать функцию, которая будет применяться к каждому элементу коллекции для сравнения.

ages = [25, 30, 35, 40]
print(max(ages))  # 40
print(min(ages))  # 25

employees = [
    {"name": "Алиса", "age": 30},
    {"name": "Петр", "age": 25},
    {"name": "Николай", "age": 35},
]

oldest_employee = max(employees, key=lambda employee: employee["age"])
print(oldest_employee)  # {'name': 'Николай', 'age': 35}
youngest_employee = min(employees, key=lambda employee: employee["age"])
print(youngest_employee)  # {'name': 'Петр', 'age': 25}

# sort - метод списков сортирует список на месте
# sorted - функция, которая возвращает новый отсортированный список и поддерживает key - аргумент, который позволяет указать функцию, которая будет применяться к каждому элементу коллекции для сравнения.

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)
print(numbers)  # [1, 2, 5, 5, 6, 9]

names = ["Анна", "Борис", "Андрей", "Дарья", "Елена", "Вадим", "Венер"]
names.sort()
print(names)  # ['Андрей', 'Анна', 'Борис', 'Вадим', 'Венер', 'Дарья', 'Елена']

names.sort(key=lambda name: name[-1], reverse=True)
print(names)

# Sorted - функция, которая возвращает новую сортированную коллекцию и поддерживает key - аргумент, который позволяет указать функцию, которая будет применяться к каждому элементу коллекции для сравнения.

sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

some_dict = {3: "Три", 1: "Один", 2: "Два"}
sorted_dict = dict(sorted(some_dict.items(), key=lambda item: item[0]))
