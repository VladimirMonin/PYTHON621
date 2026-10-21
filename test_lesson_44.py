import sqlite3
from pathlib import Path
from contextlib import closing
import pytest

from lesson_44 import get_post_detail

ROOT = Path(__file__).resolve().parent
TEST_SQL = ROOT / "test_blog.sql"

@pytest.fixture
def db_connection():
    with closing(sqlite3.connect(":memory:")) as connection:
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")

        sql = TEST_SQL.read_text(encoding='utf-8')
        connection.executescript(sql)
        yield connection


def test_get_post_detail(db_connection):
    post = get_post_detail(db_connection, 1)

    assert post is not None
    assert post["id"] == 1
    assert post["title"] == "Первый запуск Python"