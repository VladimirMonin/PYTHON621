# Lesson 25

"""
2026-07-27 20:15:31 INFO Программа запущена
2026-07-27 20:15:32 WARNING Пользователь не указал email
2026-07-27 20:15:33 ERROR Не удалось подключиться к базе данных
"""

import logging
from utils import fun_foo

# Базовый вариант конфига для логгера

"""
%(levelname)s	Уровень лога
%(asctime)s	Дата и время
%(name)s	Имя логгера
%(message)s	Текст сообщения
INFO | 2026-07-27 21:16:44,962 | __main__ | Программа запущена


filename - имя файла лога
filemode - w - перезапись, a - дозапись
"""
logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s | %(asctime)s | %(name)s | %(message)s",
                    filename="lesson_25.log",
                    encoding="utf-8",
                    filemode="w"
                    )

# Создаем логгер. Тут можно задать его имя. Без этого это будет root
logger = logging.getLogger(__name__)

logger.info("Программа запущена")
logger.debug("Кот чихнул!")

# Так как функция импортирована из utils.py имя логера __name__ тут будет utils
fun_foo()