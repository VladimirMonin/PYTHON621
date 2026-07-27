import logging

logger = logging.getLogger(__name__)


def fun_foo():
    logger.info("Почему муж программист не купил хлеб? Потому что не залогировал это!")
    print("Функция отработала")


def divide_foo(a: int, b: int) -> float|None:
    # Вариант ленивого форматирования
    # logger.info("Начинается деление %s на %s", a, b)
    logger.info(f"Начинается деление {a} на {b}")

    try:
        result = a / b
        logger.info(f"Результат деления: {result}")
        return result
    except ZeroDivisionError as e:
        logger.exception("Ошибка деления на ноль")
        return None

