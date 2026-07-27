# Lesson 15
"""
Области видимости - декоратор
"""

# Глобальная облатсь
a = 5


def foo1():
    # Лолькальная область
    a = 2
    print(a)


def foo2():
    a = 3
    print(a)


def foo3():
    a = 1

    def inner():
        nonlocal a
        a = 4
        print(a)

    inner()


foo1()
foo2()
foo3()

чебурек = print
чебурек("Чебуречный принт!")

чебурек(id(чебурек))
чебурек(id(print))
# 2248673527264
# 2248673527264

from ast import Call
from typing import Callable


def counter(start: int) -> Callable:
    start_num = start

    def inner():
        nonlocal start_num
        start_num += 1
        return start_num

    return inner


my_counter = counter(5)
print(my_counter())  # 6
print(my_counter())  # 7

my_films = ["Матрица", "Человек Паук", "Железный человек", "Человек муравей"]
search_str = "человек"
search_str2 = "век"


def search_with_memory(collection: list) -> Callable:
    collection_memory = []
    search_str_memory = ""
    result_in_memory = []

    def filter_func(search_str: str):
        nonlocal collection_memory, search_str_memory, result_in_memory
        if collection == collection_memory and search_str == search_str_memory:
            print("Отработал кеш")
            return result_in_memory

        print("Кеш не сработал - происходят реальыне вычисления")
        collection_memory = collection.copy()
        search_str_memory = search_str
        result_in_memory = [
            item for item in collection if search_str.lower() in item.lower()
        ]
        return result_in_memory

    return filter_func


test1 = search_with_memory(my_films)
print(test1(search_str))  # ['Человек Паук', 'Человек муравей']
print(test1(search_str))  # ['Человек Паук', 'Человек муравей']
print(test1(search_str2))  # ['Человек Паук', 'Человек муравей']


def decorator1(func: Callable):
    def wrapper():
        print("До вызова функции")
        result = func()
        print("После вызова функции")
        return result

    return wrapper


def test_func():
    return "Привет из тестовой функции"


result_test = decorator1(test_func)
print(result_test())


"""
Это олдскульный вариант декорирования — так, как если бы у нас не было «собачки». Значок `@` является синтаксическим сахаром Python, но если бы его не существовало, нам бы приходилось делать это вручную, и это было бы очень неудобно.

Я буквально вызываю декоратор и помещаю туда ссылку на свою же функцию. После чего я вызываю то, что создал, и таким образом пропускаю результат работы своей функции через функцию-декоратор. 

Поэтому на принте мы видим: «принт до вызова функции», затем выполняется сама функция, потом происходит «принт после вызова функции», и только после этого наружу попадает результат работы моей декорированной функции, который выводится внешним принтом на 110-й строке.
"""

"""
Синтаксис «@» (название функции декоратора) прямо над другой функцией означает, что Python будет всегда автоматически пропускать нашу функцию `test_func` через декоратор.

Нам не нужно будет писать тот код, который мы писали выше, чтобы получить этот же эффект.
"""


@decorator1
def test_func2():
    return "Привет из тестовой функции 2"


@decorator1
def test_func3():
    return "Привет из тестовой функции 3"


print(test_func2())
print(test_func3())


@decorator1
def test_func4(name: str):
    return f"Привет {name} из функции 4"


# TypeError: decorator1.<locals>.wrapper() takes 0 positional arguments but 1 was given
# test_func4("Анна")


def decorator2(func: Callable):
    def wrapper(name):
        print("До вызова функции")
        result = func(name)
        print("После вызова функции")
        return result

    return wrapper


@decorator2
def test_func5(name: str):
    return f"Привет {name} из функции 5"


test_func5("Aнна")


def decorator3(func: Callable):
    def wrapper(*args, **kwargs):
        print("До вызова функции")
        result = func(*args, **kwargs)
        print("После вызова функции")
        return result

    return wrapper


def decorator4(func: Callable):
    def wrapper(*args, **kwargs):
        print("Декоратор 4! ДО")
        result = func(*args, **kwargs)
        print("Декоратор 4! ПОСЛЕ")
        return result

    return wrapper


@decorator3
def test_func6(name, last_name):
    print(f"Привет {name} {last_name} из функции 6")


@decorator3
def test_func7(name, last_name, age=18):
    print(f"Привет {name} {last_name} из функции 7 тебе {age} лет")


test_func6("Филлип", "Киркоров")
test_func6(last_name="Киркоров", name="Филлип")
test_func7(last_name="Киркоров", name="Филлип", age=20)


@decorator3
@decorator4
def test_func8(name):
    print(f"Привет {name} из функции 7")


test_func8("Олег")


def r_block_decorator(func: Callable):
    def wrapper(word):
        if "р" in word.lower():
            raise ValueError("содержит букву 'р'.")

        else:
            return func(word)

    return wrapper


@r_block_decorator
def get_uppercase_word(word):
    return word.upper()


# print(get_uppercase_word("Привет"))
print(get_uppercase_word("Пока"))


def decorator66(letter: str = "р"):
    def r_block_decorator(func: Callable):
        def wrapper(word):
            if letter in word.lower():
                raise ValueError("содержит недопустимую букву", letter)

            else:
                return func(word)

        return wrapper

    return r_block_decorator


@decorator66(letter="р")
def get_uppercase_word2(word):
    return word.upper()


print(get_uppercase_word2("Привет"))
print(get_uppercase_word2("Пока"))
