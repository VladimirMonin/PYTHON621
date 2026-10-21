from gettext import install
import sqlite3
from pathlib import Path

from lesson_44_sample import SOURCE_DB

ROOT = Path(__file__).resolve().parent

print(ROOT)  # C:\PY\ПРИМЕРЫ КОДА\PYTHON621

SOURCE_DB = ROOT / "blog.db"
DEMO_DB = ROOT / "lesson_44_blog.db"

# 1. Подключение к файлу БД
connection = sqlite3.connect(SOURCE_DB)

# 2. С подключением мы можем создать объект cursor - та сущность которая будет выполнять наши запросы
cursor = connection.cursor()

# 3. С помощью cursor мы можем можем делать запросы в БД!
cursor.execute("SELECT * FROM POSTS")

# 4. После запроса мы можем получить данные
posts = cursor.fetchmany(2)

# 5. Распечатать данные
print(posts)

# 6. Закрыть соединение
connection.close()


# - `Connection` — соединение, транзакции, фабрика курсоров.
# - `Cursor` — выполнение запросов и чтение результата.
# - `execute()` — один запрос с параметрами; результат забирают `fetchone()` / `fetchmany()` / `fetchall()`.
# - Изменения без `commit()` теряются при закрытии соединения.
# - Всегда закрывайте `cursor` и `connection` (или используйте `with conn:` для транзакций и явный `close()` для соединения).


# 1. Подключение к файлу БД
connection = sqlite3.connect(SOURCE_DB)

"""
`sqlite3.Row` в Python — это специальный служебный объект. Если мы распечатаем результат работы `cursor.fetchall()`, мы получим на вид список, но в конце будут некие служебные объекты. Эта штука является служебным объектом, это не является списком или словарём.

Поэтому оно поддерживает обращение двумя способами: к результатам работы `sqlite3.Row` из `cursor.fetchall()` можно обращаться как по ключу, так и по индексу — то есть как будто бы это и список, и словарь одновременно.

Также можно получить названия столбцов, если мы обратимся к результату работы этого и вызовем метод `keys`, который в словаре по классике отдаёт нам названия ключей.

Эта штука поддерживает также конвертацию в словарь. То есть технически мы можем обойти циклом список `cursor.fetchall()` и конвертировать всё функцией `dict`.

"""

connection.row_factory = sqlite3.Row

cursor = connection.execute(
    "SELECT id, title, slug FROM posts"
)

# for post in cursor.fetchall():
#     print(post["id"])
#     print(post["title"])
#     print(post["slug"])


posts = [
    dict(post) for post in cursor.fetchall()
]

print(posts)

connection.close()

with sqlite3.connect(SOURCE_DB) as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.execute(
        "SELECT * FROM posts WHERE id = 1"
    )
    post = cursor.fetchone()

    if post:
        print("Пост по АЙДИ")
        print(dict(post))
    else:
        print("Пост не найден")


# user_input = input("Введите ID поста:")
# # 1
# # 1 OR 1=1
# # SELECT * FROM posts WHERE id = 1 OR 1=1

# with sqlite3.connect(SOURCE_DB) as connection:
#     connection.row_factory = sqlite3.Row
#     # cursor = connection.execute(
#     #     f"SELECT * FROM posts WHERE id = {user_input}"
#     # )

#     # Вариант устойчивый к SQL инъекциям
#     cursor = connection.execute(
#         "SELECT * FROM posts WHERE id = ?", (user_input,)
#     )
#     posts = cursor.fetchall()

#     if posts:
#         for post in posts:
#             print(dict(post))
#     else:
#         print("Пост не найден")

"""
При написании функций на Python с использованием библиотеки `sqlite3` у нас есть три способа взаимодействия с объектом соединения `connection`.

Способ номер один: создать его глобально, в функцию не передавать и внутри функции просто использовать эту переменную из глобальной области видимости.

Способ номер два: создавать внутри каждой функции свой собственный `connection`.

Способ номер три: передавать `connection` аргументом внутрь функции, а создавать его извне.

Хороший для тестирования способ — если вы собираетесь писать какие-то базовые тесты — чтобы ваша функция обязательно принимала объект соединения. Потому что вы можете сделать тесты с виртуальной базой в оперативной памяти, подключиться к ней, передать этот `connection` в вашу функцию и прогонять тесты.
"""

from typing import TypedDict, cast

class Post(TypedDict):
    id: int
    title: str
    slug: str
    content: str
    category_id: int | None
    likes: int
    view_count: int
    create_at: str


class PostDetail(TypedDict):
    id: int
    title: str
    category_id: int | None
    category_name: str | None
    create_at: str| None
    likes: int
    view_count: int
    tags: list[str]

def get_post_by_id(connection: sqlite3.Connection, post_id: int) -> Post | None:
    """
    Функция для получения поста по ID. Важно, должна использваться с connection.row_factory = sqlite3.Row
    """
    cursor = connection.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    )
    post = cursor.fetchone()

    if post:
        # Встроенная в Python функция `cast`, живущая в модуле `typing`, успокаивает аннотацию типов. Фактически здесь мы говорим, что берём ответственность на себя, утверждая, что эта штука точно соответствует нашему типу.
        return cast(Post, dict(post))
    else:
        return None


"""
Эту функцию можно использовать двумя способами: вы можете буквально создать переменную с экземпляром соединения и передать её в функцию; но, с другой стороны, вы можете использовать эту функцию в рамках контекстного менеджера через `with sqlite3.connect(...)`. И так, и так будет правильно — главное, чтобы соединение после использования функции закрывалось.
"""

with sqlite3.connect(SOURCE_DB) as conntion:
    connection.row_factory = sqlite3.Row

    post = get_post_by_id(connection, 1)
    if not post:
        print("Пост не обнаружен!")
    else:
        print("Заголовок:", post["title"])


def get_post_detail(
        connection: sqlite3.Connection,
        post_id: int
) -> PostDetail | None:
    cursor = connection.execute(
    """
    SELECT
        p.id,
        p.title,
        p.content,
        p.slug,
        p.category_id,
        p.create_at,
        p.likes,
        p.view_count,
        c.name AS category_name,
        GROUP_CONCAT(h.title, ', ') AS tags
    FROM posts AS p
    LEFT JOIN categories AS c
        ON c.id = p.category_id
    LEFT JOIN posts_hashtags AS ph
        ON ph.post_id = p.id
    LEFT JOIN hashtags AS h
        ON h.id = ph.hashtag_id
    WHERE p.id = ?
    GROUP BY p.id
    """, (post_id,)
    )

    row = cursor.fetchone()
    if row is None:
        return None

    post = dict(row)
    post["tags"] = post["tags"].split(", ") if post["tags"] else []

    return cast(PostDetail, post)

with sqlite3.connect(SOURCE_DB) as connection:
    connection.row_factory = sqlite3.Row

    post = get_post_detail(connection, 1)
    if post:
        print(post["title"])
        print(post["category_name"])
        print(post["tags"])

    
