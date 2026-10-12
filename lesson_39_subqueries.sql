-- PYTHON621. Занятие №39. Подзапросы.
-- База: db/marvel_normal.db от корня Teaching Hub, 16 376 персонажей.
-- Подключите эту базу в редакторе SQL и запускайте запросы по одному сверху вниз.
-- Все запросы только читают данные: таблицы и записи не изменяются.
-- Контрольные числа относятся к текущей учебной базе, а не к любой версии Marvel.
-- LIMIT 10 сокращает только показ списка, но не расчёт среднего и не список ключей.
-- AVG, MIN и MAX не учитывают NULL. Неизвестное значение не заменяем нулём.

-- 1. Посмотреть первые десять персонажей и поля, с которыми будем работать.
-- APPEARANCES — число появлений; Year — год первого появления.
-- Результат: 10 строк, по возрастанию id.
SELECT id, name, APPEARANCES, Year, align_id, eye_id, hair_id
FROM MarvelCharacters
ORDER BY id
LIMIT 10;

-- 2. Сравнить число всех персонажей с числом известных значений APPEARANCES.
-- COUNT(*) считает все строки, а COUNT(APPEARANCES) пропускает NULL.
-- Результат: 1 строка; total_characters = 16376, known_appearances = 15280.
SELECT COUNT(*) AS total_characters,
       COUNT(APPEARANCES) AS known_appearances
FROM MarvelCharacters;

-- 3. Получить среднее число появлений: это будущий порог для фильтрации.
-- Без GROUP BY агрегат даёт одну строку с одним значением.
-- Результат: 1 строка; average_appearances примерно 17.0334.
SELECT AVG(APPEARANCES) AS average_appearances
FROM MarvelCharacters;

-- 4. Вручную подставить среднее из запроса №3 и найти персонажей выше порога.
-- Это временный вариант: если данные изменятся, переписанное число устареет.
-- Результат: 10 строк с наибольшим числом появлений среди подходящих персонажей.
SELECT id, name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > 17.033376963350786
ORDER BY APPEARANCES DESC, id
LIMIT 10;

-- 5. Заменить переписанное число подзапросом: найти персонажей выше среднего.
-- Внутренний SELECT из №3 даёт один порог, внешний сравнивает с ним персонажей.
-- Среднее не округляем и не ограничиваем через LIMIT внутри подзапроса.
-- Результат: 10 строк; на текущих данных они совпадают с результатом №4.
SELECT id, name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > (
    SELECT AVG(APPEARANCES)
    FROM MarvelCharacters
)
ORDER BY APPEARANCES DESC, id
LIMIT 10;

-- 6. Посчитать всех персонажей выше среднего, а не только десять показанных.
-- Условие то же, что в №5; вместо списка выводим COUNT(*) без LIMIT.
-- Результат: 1 строка; above_average_count = 2034.
SELECT COUNT(*) AS above_average_count
FROM MarvelCharacters
WHERE APPEARANCES > (
    SELECT AVG(APPEARANCES)
    FROM MarvelCharacters
);

-- 7. Найти персонажей ниже среднего: меняем только знак сравнения из №5.
-- NULL не проходит сравнение. Сортируем от большего числа появлений к меньшему.
-- Результат: 10 строк для просмотра; без LIMIT подходящих персонажей 13246.
SELECT id, name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES < (
    SELECT AVG(APPEARANCES)
    FROM MarvelCharacters
)
ORDER BY APPEARANCES DESC, id
LIMIT 10;

-- 8. Отдельно узнать максимальное число появлений среди всех персонажей.
-- Получаем значение для следующего подзапроса, а не имя персонажа.
-- Результат: 1 строка; maximum_appearances = 4043.
SELECT MAX(APPEARANCES) AS maximum_appearances
FROM MarvelCharacters;

-- 9. Найти всех персонажей, чьё число появлений равно максимуму из №8.
-- Равенство с MAX сохраняет всех с одинаковым максимумом; LIMIT 1 здесь не нужен.
-- Результат: 1 строка на текущих данных — Spider-Man (Peter Parker), 4043.
SELECT id, name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES = (
    SELECT MAX(APPEARANCES)
    FROM MarvelCharacters
)
ORDER BY id;

-- 10. Отдельно узнать самый ранний известный год первого появления.
-- MIN(Year) возвращает год, а не список персонажей этого года.
-- Результат: 1 строка; earliest_year = 1939.
SELECT MIN(Year) AS earliest_year
FROM MarvelCharacters;

-- 11. Найти всех персонажей самого раннего года с помощью подзапроса из №10.
-- Не пишем 1939 вручную: нужный год определяется самой базой.
-- Результат: 69 строк; Year у каждого персонажа равен 1939.
SELECT id, name, Year
FROM MarvelCharacters
WHERE Year = (
    SELECT MIN(Year)
    FROM MarvelCharacters
)
ORDER BY id;

-- 12. Отдельно узнать самый поздний известный год первого появления в базе.
-- Результат: 1 строка; latest_year = 2013.
SELECT MAX(Year) AS latest_year
FROM MarvelCharacters;

-- 13. Найти всех персонажей самого позднего года: меняем MIN на MAX из №11.
-- Результат: 167 строк; Year у каждого персонажа равен 2013.
SELECT id, name, Year
FROM MarvelCharacters
WHERE Year = (
    SELECT MAX(Year)
    FROM MarvelCharacters
)
ORDER BY id;

-- 14. Узнать ключ стороны Good Characters в справочнике Alignment.
-- Для следующего IN нужен один столбец ключей, поэтому name здесь не выводим.
-- Результат: 1 строка; align_id = 2. Запоминать этот номер не требуется.
SELECT align_id
FROM Alignment
WHERE name = 'Good Characters';

-- 15. Выбрать персонажей стороны Good Characters через IN с запросом из №14.
-- Сравниваем align_id с ключами из справочника, а не с текстом названия стороны.
-- Результат: 10 строк для просмотра; без LIMIT подходящих персонажей 4636.
SELECT id, name, APPEARANCES, align_id
FROM MarvelCharacters
WHERE align_id IN (
    SELECT align_id
    FROM Alignment
    WHERE name = 'Good Characters'
)
ORDER BY id
LIMIT 10;

-- 16. Узнать ключ Blue Eyes в справочнике EyeColor.
-- Сначала проверяем внутренний запрос отдельно: он возвращает только eye_id.
-- Результат: 1 строка; eye_id = 4.
SELECT eye_id
FROM EyeColor
WHERE color = 'Blue Eyes';

-- 17. Выбрать персонажей с Blue Eyes через IN с запросом из №16.
-- Меняем справочник и ключ, но используем тот же каркас, что в №15.
-- Результат: 10 строк для просмотра; без LIMIT подходящих персонажей 1962.
SELECT id, name, eye_id
FROM MarvelCharacters
WHERE eye_id IN (
    SELECT eye_id
    FROM EyeColor
    WHERE color = 'Blue Eyes'
)
ORDER BY id
LIMIT 10;

-- 18. Получить ключи сразу двух цветов волос: Black Hair и Brown Hair.
-- Один столбец может содержать несколько строк: именно такой список нужен IN.
-- Результат: 2 строки; hair_id = 3 и 7.
SELECT hair_id
FROM HairColor
WHERE color IN ('Black Hair', 'Brown Hair')
ORDER BY hair_id;

-- 19. Найти персонажей с Black Hair или Brown Hair по списку ключей из №18.
-- Внутренний SELECT возвращает два ключа, внешний IN подходит к любому из них.
-- Результат: 10 строк для просмотра; без LIMIT подходящих персонажей 6094.
SELECT id, name, hair_id
FROM MarvelCharacters
WHERE hair_id IN (
    SELECT hair_id
    FROM HairColor
    WHERE color IN ('Black Hair', 'Brown Hair')
)
ORDER BY id
LIMIT 10;

-- 20. Построить знакомую сводку: сколько персонажей у каждой известной стороны.
-- Исключаем неизвестную сторону до GROUP BY; одна строка результата — одна сторона.
-- Результат: 3 строки; для align_id 1, 2, 3 количества равны 6720, 4636, 2208.
SELECT align_id, COUNT(*) AS hero_count
FROM MarvelCharacters
WHERE align_id IS NOT NULL
GROUP BY align_id
ORDER BY align_id;

-- 21. Использовать сводку из №20 как таблицу и оставить стороны больше 3000.
-- report — имя результата подзапроса; hero_count снаружи уже обычный столбец.
-- Внутри сначала считаем группы, снаружи фильтруем уже посчитанные строки.
-- Результат: 2 строки; align_id 1 — 6720, align_id 2 — 4636.
SELECT report.align_id, report.hero_count
FROM (
    SELECT align_id, COUNT(*) AS hero_count
    FROM MarvelCharacters
    WHERE align_id IS NOT NULL
    GROUP BY align_id
) AS report
WHERE report.hero_count > 3000
ORDER BY report.hero_count DESC, report.align_id;

-- 22. Посчитать персонажей по известным hair_id — подготовить ещё одну сводку.
-- Пока выводим все группы, без отбора по их размеру.
-- Результат: 25 строк; каждая содержит hair_id и число персонажей с этим ключом.
SELECT hair_id, COUNT(*) AS hero_count
FROM MarvelCharacters
WHERE hair_id IS NOT NULL
GROUP BY hair_id
ORDER BY hair_id;

-- 23. Через подзапрос в FROM оставить из сводки №22 группы больше 1000.
-- Это тот же приём, что в №21: меняем только ключ группировки и порог.
-- Результат: 4 строки; количества 3755, 2339, 1582, 1176 для hair_id 3, 7, 4, 14.
SELECT report.hair_id, report.hero_count
FROM (
    SELECT hair_id, COUNT(*) AS hero_count
    FROM MarvelCharacters
    WHERE hair_id IS NOT NULL
    GROUP BY hair_id
) AS report
WHERE report.hero_count > 1000
ORDER BY report.hero_count DESC, report.hair_id;

-- 24. Посчитать среднее число появлений по сторонам и отобрать средние выше 20.
-- Внутри AVG считается отдельно для каждой известной стороны и пропускает NULL.
-- Снаружи фильтруем готовый average_appearances, а не отдельных персонажей.
-- Результат: 1 строка; align_id = 2, среднее примерно 34.9427.
SELECT report.align_id, report.average_appearances
FROM (
    SELECT align_id, AVG(APPEARANCES) AS average_appearances
    FROM MarvelCharacters
    WHERE align_id IS NOT NULL
    GROUP BY align_id
) AS report
WHERE report.average_appearances > 20
ORDER BY report.average_appearances DESC, report.align_id;

-- 25. Переписать №21 через один WITH: дать сводке имя alignment_report.
-- WITH и основной SELECT — один запрос; между ними точка с запятой не ставится.
-- Имя существует только внутри этого запроса: постоянная таблица не создаётся.
-- Это другое оформление тех же двух шагов, а не новый способ считать группы.
-- Результат: 2 строки, полностью совпадающие с №21.
WITH alignment_report AS (
    SELECT align_id, COUNT(*) AS hero_count
    FROM MarvelCharacters
    WHERE align_id IS NOT NULL
    GROUP BY align_id
)
SELECT align_id, hero_count
FROM alignment_report
WHERE hero_count > 3000
ORDER BY hero_count DESC, align_id;
