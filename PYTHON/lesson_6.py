# УРОК 6. СПИСКИ В PYTHON

# МЕТОДЫ СПИСКОВ В PYTHON
# len() - возвращает количество элементов в списке.
# if in [list] - проверяет, есть ли элемент в списке.
# count() - возвращает количество вхождений элемента в список.
# append() - добавляет элемент в конец списка.
# insert() - вставляет элемент на определенную позицию в списке.
# remove() - удаляет первое вхождение элемента из списка.
# pop() - удаляет элемент по индексу и возвращает его.
# clear() - удаляет все элементы из списка.
# sort() - сортирует список.
# reverse() - переворачивает порядок элементов в списке.

ai_guru_list = [
    "Сэм Альтман",
    "Илон Маск",
    "Андрей Карпаты",
    "Грег Брокман",
    "Илья Суцкевер",
]

print(len(ai_guru_list))  # Выводит 5

ai_guru_list.append("Семёныч")  # Добавляет "Семёныч" в конец списка

if "Семёныч" in ai_guru_list:
    print("Семёныч есть в списке!")
else:
    print("Семёныча нет в списке!")  # Выводит "Семёныча нет в списке!"


# Два варианта удалить Семёныча из этого списка!
# Посчитать всех Семёнычей, в списке. Найти индекс, и удалить по индкусу.
# Вариант 2. Просто сделать remove() столько раз, сколько Семёнычей в списке.

count_semenych = ai_guru_list.count("Семёныч")
print(f"Семёнычей в списке: {count_semenych}")  # Выводит количество Семёнычей в списке

semenych_index = ai_guru_list.index("Семёныч")
print(f"Индекс Семёныча: {semenych_index}")  # Выводит индекс первого вхождения Семёныча

removied_semenych = ai_guru_list.pop(
    semenych_index
)  # Удаляет Семёныча по индексу и возвращает его

# Вариант 2. Удалить Семёныча remove
#  # Удаляет первое вхождение "Семёныч" из списка
print(ai_guru_list)  # Выводит обновленный список без Семёныча


ai_opinion_leaders = [
    "Сэм Альтман",
    "Андрей Карпати",
    "Илья Суцкевер",
    "Дарио Амодеи",
    "Илон Маск",
    "Демис Хассабис",
    "Джеффри Хинтон",
    "Ян Лекун",
    "Йошуа Бенжио",
    "Эндрю Ын",
    "Франсуа Шолле",
    "Лекс Фридман",
    "Андрей Бурков",
    "Сатя Наделла",
    "Мустафа Сулейман",
    "Дженсен Хуанг",
    "Мира Мурати",
    "Грег Брокман",
    "Ноам Шазир",
    "Эйдан Гомес",
]

# Сортировка списка по алфавиту
ai_opinion_leaders.sort()  # Сортирует список по алфавиту
print(ai_opinion_leaders)  # Выводит отсортированный список лидеров мнений в области ИИ

# Добыть рандомного человека из этого списка!
from random import choice

random_leader = choice(
    ai_opinion_leaders
)  # Выбирает случайного лидера мнений из списка
print(
    f"Случайный лидер мнений в области ИИ: {random_leader}"
)  # Выводит имя случайного лидера мнений в области ИИ

# FOR
for leader in ai_opinion_leaders:
    print(leader)
    print(f"Длина имени: {len(leader)}")


[print(name) for name in ai_opinion_leaders]

# PRACTICE - Приведем имена к snake_case

snake_case_names = []

for name in ai_opinion_leaders:
    snake_case_name = name.lower().replace(" ", "_")
    snake_case_names.append(snake_case_name)

print(snake_case_names)

# Вариант в одну строку
snake_case_names = [name.lower().replace(" ", "_") for name in ai_opinion_leaders]


# PRACTICE - Приведем имена к UpperCamelCase
# Сэм Альтман -> CэмАльтман
# сем альтман -> СемАльтман
# Вам нужно применить метод capitalize() (или title)))) а потом заменить пробелы на ничего.

upper_camel_case_names = [name.title().replace(" ", "") for name in ai_opinion_leaders]
print(upper_camel_case_names)


# count = 0
# while True:
#     print(f"Купи слона, прошу в {count} раз!")
#     # count = count + 1
#     count += 1


count = 0
while count < 5:
    print(f"Купи слона, прошу в {count} раз!")
    # count = count + 1
    count += 1


products = ["яблоко", "банан", "апельсин"]

while products:
    product = products.pop()
    print(f"Продано: {product}")
