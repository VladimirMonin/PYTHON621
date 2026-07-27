# Lesson 9 Dict в Python
# Словари в пайтон это записи в формате ключ:значение
# Ключем словаря могут быть любые неизменяемые типы данных (как и элементами множества - по той же причине, они хешируются)


# Плагины для Python в Visual Studio Code: Python, MyPy Type Checker, Pylance, Python Debugger, Python Environments. И плагин Ruff, который заменяет сейчас Black Formatter и Pylint одновременно. Этих плагинов достаточно для разработки на Python.

empty_dict = {}

# Проверяем ЧТО может стать ключем словаря. Не повторяйте.
# Это опасно для психики!

experemental_dict = {
    1: "Чебурек",
    "Пирожок": 2,
    ("биляш", "компот"): 3,
    True: "булочка",  # ПЕРЕОПРЕДЕЛИТ ЧЕБУРЕК
    None: "курение",
    3.14: "PI",
}

# True: "булочка",  ПЕРЕОПРЕДЕЛИТ ЧЕБУРЕК потому что при хешировании ключей True и 1 хешируются в ОДИНАКОВЫЙ ХЕШ

print(hash(1))
print(hash(True))
print(hash(0))
print(hash(False))
print(experemental_dict)


person = {
    "name": "Дункан",
    "last_name": "Макклауд",
    "age": 237,
    "hobbies": ["рубить головы", "искать других бессмертных", "жаловаться на субдьину"],
    "position": "Python senior developer",
}

# Старая запись была переопределена - а вот новый ключ (middle_name) был добавлен
person["name"] = "Дудункан"
person["middle_name"] = "Александрович"

print(person)

del person["middle_name"]

print(person)

# prettier print - pprint
from pprint import pprint

print("-" * 20)
pprint(person, sort_dicts=False)

# .get(key[, default]) — возвращает значение по ключу или default, самый часто используемый метод
# .keys() — возвращает объект с ключами словаря
# .values() — возвращает объект со значениями словаря
# .items() — возвращает пары (ключ, значение)
# .update([other]) — обновляет словарь данными из другого словаря или итератора
# .pop(key[, default]) — удаляет ключ и возвращает его значение
# .clear() — очищает словарь
# .copy() — возвращает копию словаря
# .setdefault(key[, default]) — возвращает значение или устанавливает default, если ключа нет
# .popitem() — удаляет и возвращает последнюю пару (ключ, значение)
# .fromkeys(seq[, value]) — создаёт словарь из последовательности ключей со значением value
# .__getitem__(key) — доступ по ключу через квадратные скобки (неявно)


# .get(key[, default]) — возвращает значение по ключу или default, самый часто используемый метод
person_name = person["name"]
# person_midle_name = person["middle_name"] KeyError: 'middle_name'
person_midle_name = person.get("middle_name")  # Мы тут получим либо данные либо None
person_midle_name = person.get("middle_name", "Отец неизвестен")

# .keys() — возвращает объект с ключами словаря
# .values() — возвращает объект со значениями словаря
# .items() — возвращает пары (ключ, значение)
print(person.keys())  # dict_keys(['name', 'last_name', 'age', 'hobbies', 'position'])
print(
    person.values()
)  #  dict_values(['Дудункан', 'Макклауд', 237, ['рубить головы', 'искать других бессмертных', 'жаловаться на субдьину'], 'Python senior developer'])
print(
    person.items()
)  # dict_items([('name', 'Дудункан'), ('last_name', 'Макклауд'), ('age', 237), ('hobbies', ['рубить головы', 'искать других бессмертных', 'жаловаться на субдьину']), ('position', 'Python senior developer')])
# Проверю тип данных
print(type(person.keys()))
print(type(person.values()))
print(type(person.items()))

# Печатаю это в списке
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))

# pop - возвращает данные по ключу и удалят запись
# popitem - возвращает ПОСЛЕДНЮЮ пару ключ и значение и удалет их из словаря

# update
pop_name = person.pop("name")
print(pop_name)

popitem = person.popitem()
print(popitem)

pprint(person)

# PRACTICE - ФИО через инпут

# first_name =
# last_name =
# middle_name =
# ....
# Получите словарь на принте
# Странный и не очень правильный (понятный, чистый вариант)
# person = {
#     "name": input("Введите имя:"),
#     "middle_name": input("Введите отчество:"),
#     "last_name": input("Введите фамилию:"),
# }
# print(person)

# print(
#     {
#         "name": input("Введите имя:"),
#         "middle_name": input("Введите отчество:"),
#         "last_name": input("Введите фамилию:"),
#     }
# )

# # Нормальный способ

# first_name = input("Введите имя:")
# middle_name = input("Введите отчество:")
# last_name = input("Введите фамилию:")

# person_dict = {
#     "name": first_name,
#     "middle_name": middle_name,
#     "last_name": last_name,
#     }


person = {
    "name": "Дункан",
    "last_name": "Макклауд",
    "age": 237,
    "hobbies": ["рубить головы", "искать других бессмертных", "жаловаться на субдьину"],
    "position": "Python senior developer",
}

# Простой проход циклом for по словарю дает обход ключей
for key in person:
    print(key)

# Это более явный способ обойти ключи словаря - учитывая то что этот метод есть ТОЛЬКО у словарей
for key in person.keys():
    print(key)

# Можно ли обойти значения без метода values()? ДА!
for key in person:
    print("Ключ:", key)
    print("Значение", person[key])

# НО! С values это делать куда удобнее
for value in person.values():
    print(value)


name, last_name = "Иван", "Иваныч"
name, last_name = ["Иван", "Иваныч"]
name, last_name, *_ = ["Иван", "Иваныч", "Иванов", 25]
print(_)
*_, last_name, age = ["Иван", "Иваныч", "Иванов", 25]

items_sample = [["ключ", "значение"], ["name", "Дункан"], ["age", 433]]

for item in items_sample:
    print(item)
    print(item[0], item[1])
    key, value = item
    print(key, value)


for key, value in person.items():
    print("ключ", key)
    print("значение", value)


cities = [
    {"name": "Москва", "population": 30_000_000, "region": "Московская область"},
    {
        "name": "Санкт-Петербург",
        "population": 10_000_000,
        "region": "Ленинградская область",
    },
]

for city in cities:
    print(city)
    print(city.get("name"))


# Файл cities_dataset.py должен лежать рядом и вы сможете из него импортировать переменную (так как будто она лежит в вашем коде) в самом том файле экспорт делать не надо как в JS
# from cities_dataset import cities
