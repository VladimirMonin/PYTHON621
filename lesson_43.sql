-- database: ./lesson_43_blog.db
-- PYTHON621. Занятие №43. Жизнь блога: JOIN, изменения, удаление, транзакции, индексы.
-- ПОДГОТОВКА: подключите отдельную УЧЕБНУЮ SQLite-базу lesson_43_blog.db.
-- Комментарий database — подсказка расширению редактора, не команда SQLite:
-- перед запуском обязательно проверьте выбранное соединение.
-- НЕ запускайте этот файл на blog.db прошлого занятия или своей домашней базе.
-- Файл можно повторять сверху вниз: начало удаляет таблицы блога и их данные.
-- Это удобно для опыта «сначала → действие → результат» с одинаковыми исходными данными.
-- ВНИМАНИЕ: сохранённые посты, категории, хэштеги и привязки будут УНИЧТОЖЕНЫ.
-- Здесь пересоздаём четыре учебные таблицы внутри файла базы, не удаляем сам файл.
-- Блок A (01–08) преподаватель выполняет заранее; на уроке начинаем с чтения.
-- Остальные запросы выполняем по одному, обсуждая результат до и после действия.
-- В редакторе отключите автоматическую обёртку всего файла в одну транзакцию:
-- BEGIN / COMMIT / ROLLBACK ниже должны управлять своими отдельными операциями.
-- Схема продолжает №42: categories, posts, hashtags, posts_hashtags.
-- Последнее имя взято из фактического lesson_42.sqlite3-query и blog.db.
-- В исходнике №42 было view_count INTEGER DEFAUL; здесь явное DEFAULT 0.
-- Оба столбца пары здесь NOT NULL; рабочая база прошлого занятия не меняется.
-- Это примеры урока, НЕ готовое решение ДЗ №43: данные и количества другие.

-- БЛОК A. Готовим знакомую структуру и данные, на которых видно обе стороны M:N.

-- 01. Пересоздаём учебную структуру, временно отключив проверку внешних ключей.
-- Только для полного учебного сброса: так зависимые таблицы не блокируют удаление.
-- В обычной работе проверку держим включённой, иначе можно получить «висячие» ссылки.
-- OFF не отключает PRIMARY KEY, UNIQUE и NOT NULL; речь только о FOREIGN KEY.
-- OFF/ON выполняем ВНЕ транзакции; внутри BEGIN переключение не сработает.
PRAGMA foreign_keys = OFF;
-- Проверяем: сейчас одна строка со значением 0.
PRAGMA foreign_keys;
-- Удаляем привязки. IF EXISTS разрешает самый первый запуск, когда таблиц ещё нет.
DROP TABLE IF EXISTS posts_hashtags;
-- Удаляем справочник хэштегов; его содержимое будет заполнено заново.
DROP TABLE IF EXISTS hashtags;
-- Удаляем посты. Вместе с таблицей исчезнут её данные и индексы.
DROP TABLE IF EXISTS posts;
-- Удаляем категории. Другие, не названные здесь таблицы не трогаем.
DROP TABLE IF EXISTS categories;
-- Сразу возвращаем проверку FK; все вставки и действия урока проходят с ON.
PRAGMA foreign_keys = ON;
-- Проверяем включение: ожидаем одну строку со значением 1.
PRAGMA foreign_keys;

-- 02. Создаём категории. id — идентификатор; slug — уникальный адрес категории.
-- INTEGER PRIMARY KEY в обычной SQLite-таблице использует ключ rowid.
-- AUTOINCREMENT для автоматической выдачи id не требуется.
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE
);

-- 03. Создаём посты. Используем поля прошлого урока, включая create_at.
-- RESTRICT не разрешит удалить категорию, пока на неё ссылаются посты.
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    category_id INTEGER REFERENCES categories(id) ON DELETE RESTRICT,
    create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    likes INTEGER DEFAULT 0,
    view_count INTEGER DEFAULT 0
);

-- 04. Создаём справочник хэштегов; названия и slug не должны повторяться.
CREATE TABLE hashtags (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL UNIQUE,
    slug TEXT NOT NULL UNIQUE
);

-- 05. Создаём связь M:N, сохраняя составной PK из №42, без отдельного id.
-- Уникальна ПАРА: один post_id может повторяться с разными hashtag_id и наоборот.
-- При удалении поста/хэштега CASCADE удаляет его привязки, не другой основной объект.
CREATE TABLE posts_hashtags (
    post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    hashtag_id INTEGER NOT NULL REFERENCES hashtags(id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, hashtag_id)
);

-- 06. Добавляем три категории. В пустой базе они получат id 1, 2, 3.
INSERT INTO categories (name, slug)
VALUES ('Python', 'python'),
       ('Базы данных', 'databases'),
       ('Инструменты', 'tools');

-- 07. Добавляем пять постов и пять хэштегов. id и дата создания выдаются сами.
INSERT INTO posts (title, content, slug, category_id)
VALUES ('Первый запуск Python', 'Запускаем небольшую программу.', 'first-python', 1),
       ('Git для Python-проекта', 'Сохраняем изменения программы.', 'python-git', 1),
       ('Знакомство с SQLite', 'Храним данные в связанных таблицах.', 'sqlite-start', 2),
       ('SQL из Python', 'Соединяем программу и базу данных.', 'python-sql', 2),
       ('Пост без хэштегов', 'Эта запись пока не размечена.', 'no-hashtags', 3);
-- Идентификаторы хэштегов в этой пустой базе: 1–5.
INSERT INTO hashtags (title, slug)
VALUES ('Python', 'python'),
       ('SQLite', 'sqlite'),
       ('Git', 'git'),
       ('Обучение', 'learning'),
       ('Новости', 'news');

-- 08. Назначаем восемь пар. Python общий для постов 1, 2, 4; SQLite — для 1, 3.
-- Пост 5 без хэштегов, хэштег 5 не используется: это намеренные учебные случаи.
INSERT INTO posts_hashtags (post_id, hashtag_id)
VALUES (1, 1), (1, 2),
       (2, 1), (2, 3),
       (3, 2), (3, 4),
       (4, 1), (4, 4);
-- Контроль подготовки: 3 категории, 5 постов, 5 хэштегов, 8 привязок.
SELECT (SELECT COUNT(*) FROM categories) AS categories_count,
       (SELECT COUNT(*) FROM posts) AS posts_count,
       (SELECT COUNT(*) FROM hashtags) AS hashtags_count,
       (SELECT COUNT(*) FROM posts_hashtags) AS links_count;

-- БЛОК B. Читаем один и тот же блог с разных сторон.

-- 09. Читаем посты с названиями категорий: пять строк, по одной на пост.
SELECT p.id, p.title, c.name AS category, p.create_at, p.likes, p.view_count
FROM posts AS p
JOIN categories AS c ON c.id = p.category_id
ORDER BY p.id;

-- 10. Собираем три таблицы через JOIN: восемь строк, по одной на привязку.
-- Повторение заголовка поста не ошибка: у него несколько хэштегов.
SELECT p.id AS post_id, p.title AS post_title, h.title AS hashtag
FROM posts AS p
JOIN posts_hashtags AS ph ON ph.post_id = p.id
JOIN hashtags AS h ON h.id = ph.hashtag_id
ORDER BY p.id, h.id;

-- 11. Находим все посты хэштега Python: три строки, посты 1, 2, 4.
-- Теперь есть общие хэштеги, чего не хватило в конце №42.
SELECT h.title AS hashtag, p.id, p.title
FROM hashtags AS h
JOIN posts_hashtags AS ph ON ph.hashtag_id = h.id
JOIN posts AS p ON p.id = ph.post_id
WHERE h.slug = 'python'
ORDER BY p.id;

-- 12. Узнаём хэштеги одного поста: у поста 1 две строки.
SELECT p.title AS post_title, h.title AS hashtag
FROM posts AS p
JOIN posts_hashtags AS ph ON ph.post_id = p.id
JOIN hashtags AS h ON h.id = ph.hashtag_id
WHERE p.id = 1
ORDER BY h.id;

-- 13. Меняем INNER JOIN на LEFT JOIN: девять строк, включая пост 5 с NULL.
-- Два LEFT JOIN сохраняют посты без привязок; последующий INNER JOIN их потерял бы.
SELECT p.id, p.title, h.title AS hashtag
FROM posts AS p
LEFT JOIN posts_hashtags AS ph ON ph.post_id = p.id
LEFT JOIN hashtags AS h ON h.id = ph.hashtag_id
ORDER BY p.id, h.id;

-- 14. Собираем хэштеги в одной строке поста: пять строк.
-- Считаем ph.hashtag_id, не COUNT(*): у поста 5 результат 0, не 1.
-- GROUP_CONCAT без отдельного порядка не обещает фиксированный порядок названий.
SELECT p.id, p.title, COUNT(ph.hashtag_id) AS hashtag_count,
       GROUP_CONCAT(h.title, ', ') AS hashtags
FROM posts AS p
LEFT JOIN posts_hashtags AS ph ON ph.post_id = p.id
LEFT JOIN hashtags AS h ON h.id = ph.hashtag_id
GROUP BY p.id, p.title
ORDER BY p.id;

-- БЛОК C. Добавляем и изменяем данные, затем отдельно снимаем привязку.

-- 15. Создаём новый пост и новый хэштег. Будут пост 6 и хэштег 6.
INSERT INTO posts (title, content, slug, category_id)
VALUES ('Ветки Git', 'Пробуем независимые изменения.', 'git-branches', 3);
-- Проверяем автоматический id новой записи, а не угадываем его в существующей базе.
SELECT id, title, category_id, create_at FROM posts WHERE slug = 'git-branches';
-- Добавляем новый хэштег пока без единой привязки.
INSERT INTO hashtags (title, slug) VALUES ('Практика', 'practice');
-- Проверяем ключ нового хэштега.
SELECT id, title FROM hashtags WHERE slug = 'practice';

-- 16. Привязываем к новому посту Git и Практику. Теперь десять пар.
-- Подзапросы получают ключи по уникальным slug: это уже знакомый приём.
INSERT INTO posts_hashtags (post_id, hashtag_id)
VALUES ((SELECT id FROM posts WHERE slug = 'git-branches'),
        (SELECT id FROM hashtags WHERE slug = 'git')),
       ((SELECT id FROM posts WHERE slug = 'git-branches'),
        (SELECT id FROM hashtags WHERE slug = 'practice'));
-- Проверяем два хэштега нового поста.
SELECT p.id, p.title, h.title AS hashtag
FROM posts AS p
JOIN posts_hashtags AS ph ON ph.post_id = p.id
JOIN hashtags AS h ON h.id = ph.hashtag_id
WHERE p.slug = 'git-branches'
ORDER BY h.id;

-- 17. Редактируем текст одного поста: SELECT до, UPDATE с WHERE, SELECT после.
SELECT id, title, content, create_at FROM posts WHERE id = 3;
-- Дата создания не меняется сама при редактировании текста.
UPDATE posts SET content = 'Проверяем внешние ключи и читаем связанные данные.' WHERE id = 3;
-- Только текст поста 3 должен отличаться от предыдущей выборки.
SELECT id, title, content, create_at FROM posts WHERE id = 3;

-- 18. Переносим новый пост в категорию «Базы данных»: меняем только ссылку.
SELECT p.id, p.title, c.name AS category
FROM posts AS p JOIN categories AS c ON c.id = p.category_id
WHERE p.slug = 'git-branches';
-- category_id становится 2, но сама категория и другие посты не переименовываются.
UPDATE posts
SET category_id = (SELECT id FROM categories WHERE slug = 'databases')
WHERE slug = 'git-branches';
-- Проверяем название новой категории через JOIN.
SELECT p.id, p.title, c.name AS category
FROM posts AS p JOIN categories AS c ON c.id = p.category_id
WHERE p.slug = 'git-branches';

-- 19. Переименовываем общий хэштег. Привязки не меняются; обновлена одна строка.
SELECT id, title, slug FROM hashtags WHERE id = 1;
-- slug оставляем прежним, меняем отображаемое название.
UPDATE hashtags SET title = 'Python: практика' WHERE id = 1;
-- Три поста сразу показывают новое название без обновления каждого поста.
SELECT p.id, p.title, h.title AS hashtag
FROM posts AS p
JOIN posts_hashtags AS ph ON ph.post_id = p.id
JOIN hashtags AS h ON h.id = ph.hashtag_id
WHERE h.id = 1
ORDER BY p.id;

-- 20. Меняем не название хэштега, а одну привязку: у поста 6 Практика → SQLite.
SELECT post_id, hashtag_id FROM posts_hashtags WHERE post_id = 6 ORDER BY hashtag_id;
-- Условие содержит ОБА ключа пары. Пары (6, 2) пока нет: конфликт PK не возникнет.
UPDATE posts_hashtags SET hashtag_id = 2 WHERE post_id = 6 AND hashtag_id = 6;
-- Две пары остаются: (6, 2), (6, 3); сам хэштег Практика существует.
SELECT post_id, hashtag_id FROM posts_hashtags WHERE post_id = 6 ORDER BY hashtag_id;

-- 21. Снимаем Git только с поста 6. Удаляем пару, не пост и не хэштег.
SELECT post_id, hashtag_id FROM posts_hashtags WHERE post_id = 6 AND hashtag_id = 3;
-- После удаления останется девять привязок; у поста 6 только SQLite.
DELETE FROM posts_hashtags WHERE post_id = 6 AND hashtag_id = 3;
-- Удалённая пара: ноль строк.
SELECT post_id, hashtag_id FROM posts_hashtags WHERE post_id = 6 AND hashtag_id = 3;
-- Пост и хэштег Git: по одной сохранённой строке.
SELECT id, title FROM posts WHERE id = 6;
-- Git по-прежнему нужен другому посту.
SELECT id, title FROM hashtags WHERE id = 3;

-- БЛОК D. Удаляем основной объект и проверяем направление каскада.

-- 22. Удаляем пост 4. Сначала читаем пост и его две привязки.
SELECT id, title FROM posts WHERE id = 4;
-- Две зависимые строки; Python и Обучение используются и другими постами.
SELECT post_id, hashtag_id FROM posts_hashtags WHERE post_id = 4;
-- CASCADE находится в FK дочерней таблицы, поэтому удалит только привязки поста.
DELETE FROM posts WHERE id = 4;
-- Оба следующих SELECT вернут ноль строк.
SELECT id, title FROM posts WHERE id = 4;
-- Проверяем отсутствие осиротевших привязок удалённого поста.
SELECT post_id, hashtag_id FROM posts_hashtags WHERE post_id = 4;
-- Общие хэштеги сохранились: две строки.
SELECT id, title FROM hashtags WHERE id IN (1, 4) ORDER BY id;
-- Контроль: 5 постов, 6 хэштегов, 7 привязок, 3 категории.
SELECT (SELECT COUNT(*) FROM posts) AS posts_count,
       (SELECT COUNT(*) FROM hashtags) AS hashtags_count,
       (SELECT COUNT(*) FROM posts_hashtags) AS links_count,
       (SELECT COUNT(*) FROM categories) AS categories_count;

-- Отдельный намеренно ошибочный эксперимент — НЕ часть общего запуска.
-- В выделенном запросе можно выполнить DELETE FROM categories WHERE id = 2;
-- Ожидаем FOREIGN KEY constraint failed: в категории остались посты.
-- Ошибка одного оператора не означает автоматический откат всей открытой транзакции.

-- БЛОК E. Первый осознанный откат и фиксация нескольких связанных действий.

-- 23. Запоминаем значения до транзакции: «Первый запуск Python» и «Python: практика».
SELECT id, title FROM posts WHERE id = 1;
-- Это две разные таблицы, которые изменим вместе.
SELECT id, title FROM hashtags WHERE id = 1;
-- Начинаем транзакцию; проверка FK уже включена в 01.
BEGIN;
-- Временная правка поста, которую не хотим оставлять.
UPDATE posts SET title = 'ВРЕМЕННЫЙ ЗАГОЛОВОК' WHERE id = 1;
-- Временная правка хэштега в той же транзакции.
UPDATE hashtags SET title = 'ВРЕМЕННЫЙ ХЭШТЕГ' WHERE id = 1;
-- В своём соединении видим ещё не зафиксированные изменения.
SELECT p.title AS post_title, h.title AS hashtag
FROM posts AS p
JOIN posts_hashtags AS ph ON ph.post_id = p.id
JOIN hashtags AS h ON h.id = ph.hashtag_id
WHERE p.id = 1 AND h.id = 1;
-- Отменяем ОБЕ правки, а не только последний UPDATE.
ROLLBACK;
-- Исходные названия снова видны: это проверка результата, не просто команда отката.
SELECT p.title AS post_title, h.title AS hashtag
FROM posts AS p
JOIN posts_hashtags AS ph ON ph.post_id = p.id
JOIN hashtags AS h ON h.id = ph.hashtag_id
WHERE p.id = 1 AND h.id = 1;

-- 24. Создаём пост и две привязки как одну операцию. Успех фиксируем COMMIT.
BEGIN;
-- Для нового поста id вычислит база, ссылки ниже получим по его уникальному slug.
INSERT INTO posts (title, content, slug, category_id)
VALUES ('Одна операция блога', 'Пост и его хэштеги сохраняем вместе.', 'atomic-post', 3);
-- Назначаем два уже существующих хэштега.
INSERT INTO posts_hashtags (post_id, hashtag_id)
VALUES ((SELECT id FROM posts WHERE slug = 'atomic-post'), 1),
       ((SELECT id FROM posts WHERE slug = 'atomic-post'), 3);
-- Фиксируем пост и привязки. После COMMIT обычный ROLLBACK их уже не отменит.
COMMIT;
-- Контроль фиксации: 6 постов и 9 привязок.
SELECT (SELECT COUNT(*) FROM posts) AS posts_count,
       (SELECT COUNT(*) FROM posts_hashtags) AS links_count;
-- Новый пост действительно имеет два хэштега: две строки.
SELECT p.id, p.title, h.title AS hashtag
FROM posts AS p
JOIN posts_hashtags AS ph ON ph.post_id = p.id
JOIN hashtags AS h ON h.id = ph.hashtag_id
WHERE p.slug = 'atomic-post'
ORDER BY h.id;

-- 25. Для сравнения показываем ручной порядок удаления: сначала дочерние строки.
-- Даже при настроенном CASCADE такой порядок допустим; без CASCADE он необходим.
BEGIN;
-- Сначала снимаем две привязки только у временного поста из 24.
DELETE FROM posts_hashtags WHERE post_id = (SELECT id FROM posts WHERE slug = 'atomic-post');
-- Сам пост пока существует, но строк JOIN с хэштегами больше нет.
SELECT id, title FROM posts WHERE slug = 'atomic-post';
-- Затем удаляем родительскую запись; общие справочники не трогаем.
DELETE FROM posts WHERE slug = 'atomic-post';
-- Сохраняем весь порядок удаления вместе.
COMMIT;
-- Временного поста нет; итог снова 5 постов и 7 привязок.
SELECT id, title FROM posts WHERE slug = 'atomic-post';
-- foreign_key_check должен вернуть НОЛЬ строк, не число 0.
PRAGMA foreign_key_check;

-- ПАУЗА ДЛЯ САМОСТОЯТЕЛЬНОЙ ПРАКТИКИ: используйте другие slug и свои записи.
-- Прочитать → добавить пост/пару → изменить → снять пару → проверить сохранность.
-- Сравнить COMMIT и ROLLBACK. Не повторять готовую домашку целиком.
-- Если добавляете свои строки сюда, контрольные числа следующих примеров изменятся.

-- БЛОК F. В КОНЦЕ УРОКА: идентификатор, уникальность и индекс — разные роли.

-- id — значение, по которому узнаём запись; имя столбца id само ничего не гарантирует.
-- PRIMARY KEY задаёт ключ записи; UNIQUE запрещает дубликаты выбранных значений.
-- INDEX — отдельная структура поиска; обычный индекс НЕ запрещает повторения.
-- В SQLite UNIQUE допускает несколько NULL, поэтому обязательное поле имеет NOT NULL.
-- INTEGER PRIMARY KEY использует rowid; отдельного автоиндекса для него обычно нет.
-- UNIQUE(slug), UNIQUE(title) и составной PK обычно обеспечиваются автоиндексами.

-- 26. Смотрим уже существующие индексы. sql = NULL у автоматически созданных.
SELECT name, tbl_name, sql
FROM sqlite_schema
WHERE type = 'index' AND tbl_name IN ('posts', 'hashtags', 'posts_hashtags')
ORDER BY tbl_name, name;
-- У posts_hashtags уже есть индекс составного PK (post_id, hashtag_id).
PRAGMA index_list(posts_hashtags);
-- Например, id=1 ищется по INTEGER PRIMARY KEY, а не по имени столбца «id».
EXPLAIN QUERY PLAN SELECT id, title FROM posts WHERE id = 1;

-- 27. Составной PK помогает искать по его первому столбцу post_id.
-- Обычно план покажет SEARCH ... USING COVERING INDEX ... (post_id=?).
-- Отдельный индекс только на post_id в этой схеме сейчас не нужен.
EXPLAIN QUERY PLAN
SELECT hashtag_id FROM posts_hashtags WHERE post_id = 1;

-- 28. Смотрим обратный JOIN ДО отдельного индекса по hashtag_id.
-- Обычно видим SCAN ph: перебор таблицы-связи; посты ищутся по INTEGER PRIMARY KEY.
-- Точное оформление EXPLAIN зависит от SQLite, это не замер секунд.
EXPLAIN QUERY PLAN
SELECT p.id, p.title
FROM posts_hashtags AS ph
JOIN posts AS p ON p.id = ph.post_id
WHERE ph.hashtag_id = 2;
-- Сохраняем смысловой результат для сравнения: посты 1, 3, 6 (три строки).
SELECT p.id, p.title
FROM posts_hashtags AS ph
JOIN posts AS p ON p.id = ph.post_id
WHERE ph.hashtag_id = 2
ORDER BY p.id;

-- 29. Создаём ОБЫЧНЫЙ индекс для обратного поиска от хэштега к постам.
-- Повторение hashtag_id допустимо и нужно для M:N. UNIQUE здесь было бы ошибкой.
-- FOREIGN KEY сам такой индекс дочернего столбца автоматически не создаёт.
CREATE INDEX idx_posts_hashtags_hashtag_id ON posts_hashtags (hashtag_id);
-- После создания обычно SEARCH ph USING INDEX ... (hashtag_id=?), вместо SCAN ph.
EXPLAIN QUERY PLAN
SELECT p.id, p.title
FROM posts_hashtags AS ph
JOIN posts AS p ON p.id = ph.post_id
WHERE ph.hashtag_id = 2;
-- Данные и ответ не изменились: те же три поста 1, 3, 6.
SELECT p.id, p.title
FROM posts_hashtags AS ph
JOIN posts AS p ON p.id = ph.post_id
WHERE ph.hashtag_id = 2
ORDER BY p.id;

-- 30. Проверяем итог и формулируем вывод без обещания «JOIN всегда быстрее».
-- Индекс помогает находить строки в WHERE и ON; использование выбирает SQLite.
-- На маленьком блоге разница секунд может быть незаметной; план — нагляднее.
-- Индексы занимают место и обновляются при записи: индексировать всё подряд не надо.
-- Уникальность пары уже обеспечена PK. Ещё один UNIQUE на ту же пару не нужен.
-- Отдельный id + UNIQUE(post_id, hashtag_id) — допустимая другая схема, не миграция здесь.
SELECT (SELECT COUNT(*) FROM categories) AS categories_count,
       (SELECT COUNT(*) FROM posts) AS posts_count,
       (SELECT COUNT(*) FROM hashtags) AS hashtags_count,
       (SELECT COUNT(*) FROM posts_hashtags) AS links_count;
-- Итог: 3 категории, 5 постов, 6 хэштегов, 7 привязок; ни одной нарушенной ссылки.
PRAGMA foreign_key_check;

-- Необязательные ошибки для ОТДЕЛЬНОГО выделенного запуска, не общего сценария:
-- INSERT INTO posts_hashtags (post_id, hashtag_id) VALUES (1, 1);
-- Ожидаем UNIQUE constraint failed: эта пара уже есть, даже без отдельного id.
-- INSERT INTO posts_hashtags (post_id, hashtag_id) VALUES (999, 1);
-- Ожидаем FOREIGN KEY constraint failed: такого поста нет.
-- Если ошибку выполняли внутри BEGIN, явный ROLLBACK — решение об отмене всей операции.
