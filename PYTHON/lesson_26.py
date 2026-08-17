"""
Урок 26, `pytest`: ключевое слово `assert`, параметризация и фикстуры в `pytest`.\

assert - утверждение, которое проверяет истинность или ложность выражения. Если условие истинно, тест пройден, если ложно, тест провален.

"""

a = 5
b = 5

try:
    assert a == b
    print("Утверждение прошло")
except AssertionError:
    print("Утверждение не прошло")


def divide_foo(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя")

    if isinstance(a, int) and isinstance(b, int):
        return a / b
    else:
        raise ValueError("Введены не числа")


# Базовая проверка 
try:
    assert divide_foo(10, 2) == 5.0
    print("Тест прошел")

except AssertionError:
    print("Тест провалился")


try:
    divide_foo(10, 0)
except ZeroDivisionError:
    print("Тест НА НОЛЬ прошел")
else:
    print("Тест НА НОЛЬ провален")
