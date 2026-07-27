import logging

logger = logging.getLogger(__name__)


def fun_foo():
    logger.info("Почему муж программист не купил хлеб? Потому что не залогировал это!")
    print("Функция отработала")
