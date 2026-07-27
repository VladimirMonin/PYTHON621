# Lesson 12 - Функциональное программирование

# Функция - это объект первого класса, который может быть присвоен переменной, передан в качестве аргумента другой функции и возвращен из функции.

# Если проще, это блок кода, сгруппированный одной логической еденицей, который сделан с целью переиспользования. Функция может принимать аргументы и возвращать результат.

# SRP - Single Responsibility Principle (Принцип единственной ответственности) - это концепция в программировании, которая гласит, что каждый модуль или класс должен иметь только одну причину для изменения. Это означает, что каждый модуль или класс должен быть ответственным за выполнение одной конкретной задачи или функции.

# DRY - Don't Repeat Yourself (Не повторяй себя) - это принцип программирования, который гласит, что каждый фрагмент знаний должен иметь единственное, недвусмысленное и авторитетное представление в системе. Это означает, что код должен быть написан таким образом, чтобы избежать дублирования и повторения.

# Нейминг - глагол + прилогательное (или существительное) - это рекомендация по именованию функций, которая помогает сделать код более читаемым и понятным. Глагол указывает на действие, которое выполняет функция, а прилагательное или существительное описывает объект, над которым выполняется действие.


def func1():
    print("Hello, World!")


def func2(name):
    print(f"Hello, {name}!")


func1()
func2("Алиса")
# func2("Алиса", "Селезнёва") # TypeError: func2() takes 1 positional argument but 2 were given


def get_hello_msg(name, last_name):
    return f"Hello, {name} {last_name}!"


_ = func2("Алиса")
print(_)
print(print("Hello, World!"))  # None


def is_palindrome(word):
    """
    Проверяет слово на палиндромность.
    :param word: Слово для проверки
    :return: True если слово палиндром, иначе False
    """
    raw_word = word.lower().replace(" ", "")
    return raw_word == raw_word[::-1]


print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("Дед"))

user_word = input("Введите слово для проверки на палиндромность: ")
if is_palindrome(user_word):
    print(f"Слово '{user_word}' является палиндромом!")
else:
    print(f"Слово '{user_word}' не является палиндромом.")


def hello_user(name="Гость"):
    print(f"Привет, {name}!")


hello_user()
hello_user("Алиса")


def hello_user2(name, age):
    print(f"Привет, {name}! Тебе {age} лет.")


# Проверка позиционности аргументов
hello_user2("Алиса", 30)  # Привет, Алиса! Тебе 30 лет.
hello_user2(30, "Алиса")  # Привет, 30! Тебе Алиса лет.
hello_user2(age=30, name="Алиса")  # Привет, Алиса! Тебе 30 лет.

dict_params = {"name": "Алиса", "age": 30}
hello_user2(**dict_params)  # Привет, Алиса! Тебе 30 лет.


# def hello_user3(age=30, name):
#     print(f"Привет, {name}! Тебе {age} лет.")

# Это тупиковая ветвь развития.

# Проблема в том, что оба аргумента являются позиционными, и аргумент, имеющий значение по умолчанию, не перестает от этого быть позиционным. Поэтому эта функция в любом случае будет требовать два аргумента на вход.
# hello_user3(30)


def hello_user4(name, age):
    print(f"Привет, {name}! Тебе {age} лет.")


# KW - аргументы. Возможность передать аргумнты по их имени. В любом порядке
hello_user4(age=30, name="Алиса")  # Привет, Алиса! Тебе 30 лет.

dict_params = {"name": "Алиса", "age": 30}

hello_user4(**dict_params)  # Привет, Алиса! Тебе 30 лет.
dict_params = {"name": "Боб", "age": 30, "address": "Тисовая улица, 10"}
# hello_user4(**dict_params)
# hello_user4(age=dict_params["age"], name=dict_params["name"]) # Привет, Алиса! Тебе 30 лет.

# arguments - аргументы
# *args - множественные позиционные аргументы
# **kwargs - множественные именованные аргументы


def hello_many_users(*names):
    print(type(names))  # <class 'tuple'>
    print(len(names))
    [print(name) for name in names]


hello_many_users("Алиса")
hello_many_users("Алиса", "Петр", "Николай")

names_list = ["Алиса", "Петр", "Николай"]
hello_many_users(*names_list)

# PRACTICE - попробуйте написать функцию которая будет принимать *words, и возвращать словарь, где ключ - слово, а значение, результат проверки на палиндромность
# 1. Пустой новый словарь
result_dict = {}
# 2. Цикл по words
# 3. Проверка на палиндромность
# 4. Запись в словарь слова и результата проверки
# result_dict[word] = результат проверки
# 5. Возврат словаря


def multiple_palindrome_check(*words):
    result_dict = {}
    for word in words:
        raw_word = word.lower().replace(" ", "")
        result_dict[word] = raw_word == raw_word[::-1]

    return result_dict


def multiple_palindrome_check2(*words):
    return {
        word: (word.lower().replace(" ", "") == word.lower().replace(" ", "")[::-1])
        for word in words
    }


def func5(**kwargs):
    print(type(kwargs))
    print(kwargs)


func5(favorite_dish="Пельмешки", age=30)


def func6(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)


func6("Алиса", "Петр", favorite_dish="Пельмешки", age=30)

from tabulate import tabulate

group: list[list] = [
    ["Имя", "Возраст", "Любимое блюдо"],
    ["Алиса", 30, "Пельмешки"],
    ["Петр", 25, "Борщ"],
    ["Николай", 35, "Солянка"],
]


def print_table(data: list[list], style: str = "grid") -> None:
    """Выводит таблицу в консоль с помощью библиотеки tabulate.
    :param data: Двумерный список, где первый элемент - это заголовки столбцов, а остальные - строки таблицы.
    :param style: Стиль оформления таблицы (по умолчанию "grid").
    """
    print(tabulate(data, headers="firstrow", tablefmt=style))


print_table(group, style=22)
