import logging


def setup_logging() -> None:
    # В терминал отправляем INFO и выше
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # В файл отправляем DEBUG и выше
    file_handler = logging.FileHandler(
        filename="lesson_25.log",
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)

    # Общая настройка
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s | %(asctime)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            console_handler,
            file_handler,
        ],
    )