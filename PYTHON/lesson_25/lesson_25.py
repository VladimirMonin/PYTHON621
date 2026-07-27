# Lesson 25

"""
2026-07-27 20:15:31 INFO Программа запущена
2026-07-27 20:15:32 WARNING Пользователь не указал email
2026-07-27 20:15:33 ERROR Не удалось подключиться к базе данных
"""

import logging
from utils import fun_foo, divide_foo


# Обработчик терминала
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)


# Обработчик файла
file_handler = logging.FileHandler(
    filename="lesson_25.log",
    encoding="utf-8",
)
file_handler.setLevel(logging.DEBUG)


# Общая настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s | %(asctime)s | %(name)s | %(message)s",
    handlers=[
        console_handler,
        file_handler,
    ],
)


logger = logging.getLogger(__name__)


logger.info("Программа запущена")
logger.debug("Кот чихнул!")

# Так как функция импортирована из utils.py имя логера __name__ тут будет utils
fun_foo()

a = int(input("Введите число а"))
b = int(input("Введите число b"))
divide_foo(a, b)
