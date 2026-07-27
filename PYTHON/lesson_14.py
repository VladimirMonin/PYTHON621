# Lesson 14 - аннотации типов и Typing
# age:int - число
# name:str - строка
# float - дробное число
# dict, list, typle, set
# list[str] - список строк
# dict[str, int|str] - словарь где ключи строки а значения или строки или числа
# int|None - либо целое число либо None

# from typing import Callable, Optional

# Optional[int] - Может быть число а может быть None
# Callable[[int, str], int] - функция которая принимает два аргумента и возвращает число

favorite_numbers = [1, 2, 3, 4, 5]


def get_random_number(*collection: int) -> int:
    set_collection = set(collection)
    return set_collection.pop()


rundom_number = get_random_number(*favorite_numbers)


def get_user_message() -> str:
    return input("Введите что-то: ")


def get_final_msg(param: str = "string") -> str | tuple[str | int]:
    result = get_user_message()
    if param == "string":
        return result
    elif param == "tuple":
        return (result,)
    return ""


result = get_final_msg()

if type(result) is tuple:
    print(result)
    for item in result:
        print(item + " ")
elif type(result) is str:
    print(result.lower())


# PRACTICE
"""
Попробуйте установить MyPy с помощью uv.addMyPy  После чего наберите код, попробуйте вызвать проверку MyPy и название вашего файла
"""

"""
Флаги майпай
--strict - все строгие проверки разом, самый мощный вариант
--ignore-missing-imports - игнорирует отсутствующие аннотации в импортируемом файле
"""

"""
uv tool — это механизм для установки изолированных консольных приложений (инструментов), которые не являются частью какого-то одного проекта.

uv tool install ruff - устанавлиет изолированный инструмен ruff
uv tool install mypy

ruff check . Прогоняет линтер по всем .py файлам в текущей папке. Покажет ошибки, но ничего не исправит.
ruff check . --fix То же самое, но автоисправляет всё, что может (неиспользуемые импорты, лишние пробелы, etc.).
ruff check . --fix --unsafe-fixes Исправляет даже потенциально опасные штуки (меняет логику кода — аккуратнее с этим).
ruff format .
"""

a = 5  # Коммент
b = 4
c = 3


def foo1():
    return 1


def foo2():
    print("ddd")


############################## ОБЛАСТИ ВИДИМОСТИ
"""
- Built-in scope - встроенная область видимости - встроенные в пайтон инструменты (print и т.п.)
- Global scope - глобальная область видимости - весь наш файл - все что вокруг нас
- Local scope - локальная область видимости - внутри функции
- Non Local scope - НЕ локальная область видимости - функнция вложенная в другую (только в этом случае это уместно)
"""

a = 5 # Глобальная область видимости

def foo():
    a = 10 # Локальная область видимости
    print(a)

print(a) # 5
foo() # 10
print(a) # 5

def foo3():
    # Если внутри функции нет а - мы ищем ее снаружи
    print(a)
    

# print = "Чебурек"
# print("ЧТО ТО") # 'str' object is not callable

def foo4():
    def inner():
        print("Привет из inner")
    inner()

def foo5():
    def inner():
        print("Привет из inner")
    return inner

banana = print
banana("Банановый принт!")

result_5 = foo5()
result_5()
result_5()

"""
global - используется внутри функции, и позволяет перезаписать ГЛОБАЛЬНЫЕ переменные. НЕ РЕКОМЕНДУЮТ ИСПОЛЬЗОВАТЬ
nonlocal - ТО ЖЕ САМОЕ, НО для ПЕРЕОПРЕДЕЛЕНИЯ ИЗ ВЛОЖЕННОЙ функции что-то во ВНЕШНЕЙ функции.
"""

b = 10

def foo6():
    global b # Разрешине на перезапись ГЛОБАЛЬНО
    b = 20

print(b)
foo6()
print(b)


a = 3
def foo7():
    a = 5
    print(a, "foo7 до вызова inner")
    def inner():
        # nonlocal a - ВАЖНАЯ СТРОКА
        a = 10
        print("inner a", a)
    inner()
    print(a, "foo7 после вызова inner")


def counter(start: int = 0):
    # statr живет ТУТ и это local scope 
    def inner():
        nonlocal start
        start += 1
        return start
    
    return inner

counter_1 = counter()
counter_2 = counter(5)

print(counter_1()) # 1
print(counter_1()) # 2
print(counter_2()) # 6

