# Lesson 8 - Множества
# Множества - это неупорядоченные коллекции уникальных элементов которые хранятся в виде хеш-таблицы. Важно что элементы множества должны быть неизменяемыми (хешируемыми) - строки, числа, bool, кортежи. Множества поддерживают операции объединения, пересечения, разности и симметрической разности.

# Создание пустого множества
empty_set = set()  # ВАЖНО! Нельзя создать множество с помощью фигурных скобок {}, так как это будет словарь, а не множество.

suhi1 = "филадельфия"
print(hash(suhi1))  # Получение хеш-значения строки
# -3935584557020997658
# 7697187882776257118

count = 0
while True:
    print(hash(suhi1))
    count += 1
    if count >= 5:
        break
# -5644304149665032741 - пять раз подряд. Потому что хеш считается один раз на запуск пайтон кода.

# Создание множества (сета)
my_sushi = {"филадельфия", "калифорния", "темпура", "роллы с угрем"}

# Все четыре будут ОДИНАКОВЫМИ. По этой же причине
# Пайтон хеширует строки на страте ОДИН РАЗ, потом мы видим порядок на экране в соответсвтии с адресами в хеш-таблице.
print(my_sushi)
print(my_sushi)
print(my_sushi)
print(my_sushi)

# МЕТОДЫ СЕТОВ
# add - добавить в сет
# remove - удалить
# discard - удалить 2
# pop - добыть и удалить случайный элемент
######### Операции с сетами (пересечение, разница, симметричная разница, объединение)

my_sushi = {"филадельфия", "калифорния", "темпура", "роллы с угрем"}

for suhi in my_sushi:
    print(suhi)

# print(my_sushi[0]) # TypeError: 'set' object is not subscriptable потому что тут нет индексов!

if "филадельфия" in my_sushi:
    print(True, "филадельфия")

my_sushi.add("яки-маки")  # 123
my_sushi.add("яки-маки")  # 123

print(my_sushi)

# discard - не дает ошибку ЕСЛИ нет элемента в сете
# remove - дает ошибку ЕСЛИ нет элемента в сете - удобно когда ВАМ важно ТОЧНО знать что его там не было до удаления
# pop - удалит рандомный элемент (и положит вам его в коллекцию)
# my_sushi.remove("темпура с угрем") # KeyError: 'темпура с угрем'

poped_roll = my_sushi.pop()
print(my_sushi)
print(poped_roll)

product_list = ["молоко", "хлеб", "Молоко", "кефир", "МОЛОКО"]

lower_product_list = [product.lower() for product in product_list]

clear_product_list = list(set(lower_product_list))
print(clear_product_list)

my_book = {
    "Гарри Поттер и Кубок Огня",
    "Убить пересмешника",
    "Цикл: Я робот",
    "Цикл: Ночной Дозор",
    "Властелин Колец",
}
partner_book = {
    "Убить пересмешника",
    "Цикл: Я робот",
    "Мастер и Маргарита",
    "Преступление и наказание",
    "Анна Каренина",
}

# union - | Берём всё из обоих множеств, дубли убираются.
union_collection = my_book | partner_book

# intersection & ОБЩИЙ УНИКАЛЬНЫЙ СПИСОК
intersection_collection = my_book & partner_book

# difference - ТО ЧТО ЧИТАЛ Я НО НЕ ЧИТАЛА ЖЕНА
difference_collection = my_book - partner_book

# symmetric_difference ^ симметричная разница - ВСЕ вместе, за вычетом ПЕРЕСЕЧЕНИЯ
symmetric_difference = my_book ^ partner_book

collections_1 = {"Чёрная", "Глубокая", "Невероятная", "Питерская", "Чёкнутая", "Ночная"}

collection_2 = {"Песня", "Косуха", "Бутылка", "Кошка", "Лампа"}

full_names_set = set()

for word1 in collections_1:
    for word2 in collection_2:
        new_name = f"{word1} {word2}".capitalize()
        full_names_set.add(new_name)

print(full_names_set)
