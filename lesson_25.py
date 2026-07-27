# Lesson 25

"""
2026-07-27 20:15:31 INFO Программа запущена
2026-07-27 20:15:32 WARNING Пользователь не указал email
2026-07-27 20:15:33 ERROR Не удалось подключиться к базе данных
"""

import logging

# Базовый вариант конфига для логгера
logging.basicConfig(level=logging.INFO)

# Создаем логгер. Тут можно задать его имя. Без этого это будет root
logger = logging.getLogger(__name__)

logger.info("Программа запущена")
logger.debug("Кот чихнул!")