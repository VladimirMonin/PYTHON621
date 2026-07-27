# Lesson 16 - Try - Except, практика с декораторами


# while True:
#     a = input("Введите число А: ")
#     b = input("Введите число B: ")

#     try:
#         int_a = int(a)
#         int_b = int(b)

#     except:
#         print("Ошибка! Введите числа, а не строки.")
#         continue


# while True:
#     a = input("Введите число А: ")
#     b = input("Введите число B: ")

#     try:
#         int_a = int(a)
#         int_b = int(b)

#     except Exception as e:
#         print(type(e)) # <class 'ValueError'>
#         print(e) # invalid literal for int() with base 10: 'dd'
#         print("Ошибка! Введите числа, а не строки.")
#         continue


# while True:
#     a = input("Введите число А: ")
#     b = input("Введите число B: ")

#     try:
#         int_a = int(a)
#         int_b = int(b)

#         result = int_a / int_b


#     except ValueError as e:
#         print(type(e)) # <class 'ValueError'>
#         print(e) # invalid literal for int() with base 10: 'dd'
#         print("Ошибка! Введите числа, а не строки.")
#         continue

#     except ZeroDivisionError as e:
#         print(type(e)) # <class 'ZeroDivisionError'>
#         print(e) #
#         print("Нельзя делить на ноль!")
#         continue

# raise - создает исключения в коде!
# raise ValueError("Вы что-то сделали не так!!!!!!!!")

"""
Проверку на принадлежность к определённому типу данных или же к родству с определённым классом — если говорить другими словами, можно узнать в Python двумя способами. Это функция `type` и функция `isinstance`.

type(obj) == str
isinstance(obj, str)

"""


def get_hello_message(name: str, age: int) -> str:
    """
    Функция возвращает приветственную строку!
    :param: name - Имя пользователя
    :param: age - Возраст пользователя
    :return: Приветственная строка с данными о пользователе.
    :ValueError: - Возникает если пользователь подал не те данные на вход или возраст вне диапазона
    """
    if not (isinstance(name, str) and isinstance(age, int)):
        raise ValueError(
            "Неверные данные. Имя должно быть строкой и возраст должен быть числом."
        )
    elif not (0 < int(age) < 120):
        raise ValueError("Неверный возраст. Число должно быть в диапазоне от 1 до 119.")

    return f"Привет {name}! Тебе {age} лет."


# while True:
#     try:
#         name = input("Введите имя: ")
#         age = int(input("Введите возраст: "))

#     except ValueError:
#         print("Пожаста, введите число в возраст!")
#         continue

#     try:
#         result = get_hello_message(name, age)
#         print(result)
#         continue

#     except ValueError as e:
#         print(e)


# Try Except Else Finally

"""
В Python блок `try` открывает возможность для попытки — действия, которое может привести к исключению. Исключение — это некий исключительный случай, который описан разработчиками самого языка или сторонними разработчиками (например, если вы используете какую-либо библиотеку).

Блок `else` является опциональным; в него мы попадаем только в том случае, если ни одно исключение не возникло.

Блок `finally` также присутствует и выполняется всегда, независимо от того, произошло ли исключение или нет. В этом блоке часто размещают код для логирования. Для других целей его использование мне кажется излишним.
"""

# while True:
#     try:
#         name = input("Введите имя: ")
#         age = int(input("Введите возраст: "))

#     except ValueError:
#         print("Пожалуйста, введите число в возраст!")
#         continue

#     else:
#         print("Похоже что конвертация возраста прошла без ошибок")

#     try:
#         result = get_hello_message(name, age)
#         print(result)


#     except ValueError as e:
#         print(e)

#     else:
#         print("Похоже ВСЯ работа прошла без ошибок")

#     finally:
#         print("А сюда мы попадём в любом случае")


"""
Модуль time.perf_counter — это высокоточный инструмент в Python для замера 
временных интервалов. Он использует часы с самой высокой доступной 
разрешающей способностью в системе, что делает его предпочтительным 
выбором для бенчмаркинга и оценки производительности кода.

Пример замера короткого диапазона:

    import time

    start = time.perf_counter()
    # Ваш код здесь
    end = time.perf_counter()

    duration = end - start
    print(f"Выполнено за {duration:.6f} секунд")

Для вывода результата без использования научной нотации (экспоненциального 
представления) используется форматированная строка (f-string) с 
пецификатором 'f'. Конструкция ':.6f' означает, что число будет выведено 
как десятичная дробь с фиксированной точкой (fixed-point) с точностью 
до 6 знаков после запятой, что предотвращает появление формата 'e-05'.
"""

from time import sleep, perf_counter
from typing import Callable, Any

start_time = perf_counter()
sleep(3)
finish_time = perf_counter()

duration = finish_time - start_time
print(duration)
print(round(duration, 6))


def timer_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        duration = end_time - start_time
        print(f"Функция {func.__name__} выполнена за {duration:.6f} секунд")
        return result

    return wrapper


@timer_decorator
def two_sec_sleep():
    sleep(2)
    return "Поспали 2 секунды"


@timer_decorator
def four_sec_sleep():
    sleep(4)
    return "Поспали 4 секунды"


two_sec_sleep()
four_sec_sleep()

"""
В Python декораторы с параметрами пишутся с использованием трёх функций: функция внутри функции внутри функции. 

Внешняя функция является приёмником параметров. Вторая функция является самим декоратором. Третья функция является враппером (обёрткой). Таким образом, у вас первая функция принимает параметры декоратора, вторая функция принимает декорируемую функцию, а третья функция — враппер — принимает на вход множественные аргументы и множественные ключевые аргументы `*args` и `**kwargs`.

Когда вы вешаете такой декоратор на вашу функцию, вы обязаны использовать скобки. Эти скобки запускают внешнюю функцию из трёх, которая принимает параметры декоратора. Даже если у этого декоратора есть параметры по умолчанию, которые вы не хотите переопределять, такие декораторы всё равно всегда запускаются через скобочки — просто иначе Python это не запустит. 

Если вы хотите переопределить какие-то из параметров этого декоратора, вы можете сделать это в формате keyword-аргументов.
"""

def timer_decorator2(rounded_param: int = 5):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            start_time = perf_counter()
            result = func(*args, **kwargs)
            end_time = perf_counter()
            duration = end_time - start_time
            final_time = round(duration, rounded_param)
            print(f"Функция {func.__name__} выполнена за {final_time} секунд")
            return result

        return wrapper

    return decorator


@timer_decorator2()
def two_sec_sleep2():
    sleep(2)
    return "Поспали 2 секунды"


@timer_decorator2(rounded_param=2)
def four_sec_sleep2():
    sleep(4)
    return "Поспали 4 секунды"

two_sec_sleep2()
four_sec_sleep2()