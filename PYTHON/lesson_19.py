# Lesson 19 CSV - Запись и чтение
import csv

"""
Модуль CSV в Python предназначен для обработки данных в табличном формате с расширением .csv. Он предоставляет удобные инструменты для чтения и записи документов, позволяя работать со структурированными данными без сторонних библиотек.

Для операций чтения используется класс csv.reader, который преобразует строки файла в списки. Если данные имеют заголовки, удобнее использовать csv.DictReader, который преобразует каждую строку в словарь, где ключами выступают названия столбцов из первой строки файла.

Запись данных осуществляется аналогичными методами: csv.writer для записи списков списков и csv.DictWriter для записи списков словарей. В случае с DictWriter необходимо предварительно определить полевые заголовки через параметр fieldnames.

При работе с нестандартными форматами файлов (например Майкрософт Ексель)))) ) можно настраивать параметры парсинга. Делиметр (delimiter) определяет символ, разделяющий значения в строке, по умолчанию это запятая. Параметр lineterminator задает строку, завершающую запись в файле, что позволяет корректно обрабатывать переносы строк в разных операционных системах.

Важной настройкой является кодировка (encoding). Поскольку файлы часто хранят данные в UTF-8 или CP1251, при открытии файла через встроенную функцию open() необходимо обязательно указывать параметр encoding, чтобы избежать ошибок при чтении специальных символов или русского алфавита.

Для Excel можно использовать bom-utf8
"""

participants = [
    ["first_name", "middle_name", "last_name"],
    ["Владимир", "Александрович", "Монин"],
    ["Роман", "Борисович", "Володченков"],
    ["Евгений", "Владимирович", "Черкасов"],
    ["Елена", "Алексеевна", "Путилина"],
    ["Вадим", "Юрьевич", "Забугин"],
    ["Венер", "Марселевич", "Сагидуллин"],
    ["Елена", "Викторовна", "Вересова"],
]

participants_dicts = [
    {
        "first_name": "Владимир",
        "middle_name": "Александрович",
        "last_name": "Монин",
    },
    {
        "first_name": "Роман",
        "middle_name": "Борисович",
        "last_name": "Володченков",
    },
    {
        "first_name": "Евгений",
        "middle_name": "Владимирович",
        "last_name": "Черкасов",
    },
    {
        "first_name": "Елена",
        "middle_name": "Алексеевна",
        "last_name": "Путилина",
    },
    {
        "first_name": "Вадим",
        "middle_name": "Юрьевич",
        "last_name": "Забугин",
    },
    {
        "first_name": "Венер",
        "middle_name": "Марселевич",
        "last_name": "Сагидуллин",
    },
    {
        "first_name": "Елена",
        "middle_name": "Викторовна",
        "last_name": "Вересова",
    },
]

# Запись данных в файл через csv.writer (пишем список списков)
# utf-8-sig - она же BOM UTF-8 - костыль для офиса Microsoft. Либо ее надо использовать либо windows-1251 иначе ексель не сможет номрально открыть файл
# with open("participants.csv", "w", newline="", encoding="utf-8-sig") as file:
#     writer = csv.writer(file, delimiter=";")
#     for row in participants:
#         writer.writerow(row)


# # Дозапишем данные  Монаков Денис Вячеславович
# add_data = ["Денис", "Вячеславоич", "Монаков"]


# # У объекта writer есть 2 метода. Один позволяет писать список списков (сразу много) а другой только одну строку - просто список
# with open("participants.csv", "a", newline="", encoding="utf-8-sig") as file:
#     writer = csv.writer(file, delimiter=";")
#     writer.writerow(add_data)

# # uv add tabulate

from tabulate import tabulate
# # Чтение данных из файла через csv.reader (читаем список файлов)
# with open("participants.csv", "r", newline="", encoding="utf-8-sig") as file:
#     reader = csv.reader(file, delimiter=";")
#     result = [row for row in reader]
#     print(tabulate(result, tablefmt="grid"))


"""
А теперь на очереди dictWriter. Вместо списка списков мы будем записывать словари.
"""

with open("participants_dicts.csv", "w", newline="", encoding="utf-8-sig") as file:
    headers = participants_dicts[0].keys()
    writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")
    writer.writeheader()  # Записываем заголовки
    for participant in participants_dicts:
        writer.writerow(participant)


add_dict_data = {
    "first_name": "Денис",
    "middle_name": "Вячеславоич",
    "last_name": "Монаков",
}

# Дописать данные в CSV

with open("participants_dicts.csv", "a", newline="", encoding="utf-8-sig") as file:
    headers = participants_dicts[0].keys()
    writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")
    # writer.writeheader()  # Записываем заголовки
    writer.writerow(add_dict_data)


tabulate_headers = {
    "first_name": "Имя",
    "middle_name": "Отчество",
    "last_name": "Фамилия",
}

# Открываем на чтение и печатаем tabulate
with open("participants_dicts.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=";")
    result = [row for row in reader]
    print(tabulate(result, tablefmt="grid", headers=tabulate_headers))
