# Lesson 25

"""
2026-07-27 20:15:31 INFO Программа запущена
2026-07-27 20:15:32 WARNING Пользователь не указал email
2026-07-27 20:15:33 ERROR Не удалось подключиться к базе данных
"""

import logging
from utils import fun_foo, divide_foo

# 1. Общий корневой логгер
root_logger = logging.getLogger()

# 2. Указываю минимальный уровень сообщений
root_logger.setLevel(logging.DEBUG)

# 3. Описываем внешний вид сообщений
formatter = logging.Formatter(
    fmt="%(levelname)s | %(asctime)s | %(name)s | %(message)s"
)

# 4. Создаем обработчик для терминала
console_handler = logging.StreamHandler()

# 5. Передаем ему формат в котором он должен работать
console_handler.setFormatter(formatter)

#6. Подключаем обработкчик к общему логгеру
root_logger.addHandler(console_handler)

# 7. Создаем filehandler Для записи логов в файл
file_handler = logging.FileHandler(
    filename="lesson_25.log",
    mode="w",
    encoding="utf-8"

)

# 8. Указываем форматтер и подклчаем к логгеру
file_handler.setFormatter(formatter)
root_logger.addHandler(file_handler)



#9. Создаем логгер для модуля
logger = logging.getLogger(__name__)




logger.info("Программа запущена")
logger.debug("Кот чихнул!")

# Так как функция импортирована из utils.py имя логера __name__ тут будет utils
fun_foo()

a = int(input("Введите число а"))
b = int(input("Введите число b"))
divide_foo(a, b)
