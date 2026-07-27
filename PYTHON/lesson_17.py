# Lesson 17
very_big_collection = range(1_000_000_000_000)
# print(very_big_collection)
print(type(very_big_collection))

"""
`range` является итерируемым объектом, но не является при этом итератором. Однако же мы можем это сделать, обвернув `range` в функцию `iter()`.
"""

iteraror = iter(very_big_collection)
print(type(iteraror))  # <class 'iterator'>

# print(next(iteraror))
# print(next(iteraror))
# print(next(iteraror))

# [print(i) for i in very_big_collection]

"""
Разница между итераторами и генераторами. Генератор — это частный случай итератора. Любой генератор будет являться итератором, но не любой итератор является генератором. В чем разница?

Генератор — это итератор, который создается специальным синтаксисом Python с помощью функции с ключевым словом `yield` или же с помощью генеративного выражения (того самого однострочника в круглых скобках).

Генератор как фабрика, которая печатает страницы книги, допустим, по одной на лету, отдает их тебе и сразу же о них забывает. Итератор — это объект, который помнит свое состояние и умеет сделать шаг вперед.

Получается, что любой генератор является итератором, но не любой итератор является генератором.

Итератор - низкий уровень - ручная настройка. 
1. Возвращает сам себя __iter__
2. Выдает следующий элемент и пададает с StopIteration

Генератор - выскокий уровень, это синтаксис пайтон позволяющй сделать итератор в пару строк кода. 
Никакого ООП, классов и __iter__ __next__
"""

from typing import Generator


def countdown_generator(start: int) -> Generator:
    while start > 0:
        yield start
        start -= 1


countdown_3 = countdown_generator(3)
print(next(countdown_3))  # 3
print(next(countdown_3))  # 2
print(next(countdown_3))  # 1
# print(next(countdown_3)) # StopIteration

from cities import cities_list
from pprint import pprint

r_city = filter(lambda city: city["name"].lower().startswith("р"), cities_list)
pprint(next(r_city))
pprint(next(r_city))
pprint(next(r_city))
pprint(next(r_city))


def cities_name_filter(search_str: str) -> Geneartor:
    for city in cities_list:
        if search_str.lower() in city["name"].lower():
            yield city


gorsk_filter = cities_name_filter("горск")

pprint(next(gorsk_filter))
pprint(next(gorsk_filter))


###################
import sys

list_comp = [x**2 for x in range(1_000_000)]
print(sys.getsizeof(list_comp))  # Около 8.4 мб!

gen_expr = (x * 2 for x in range(1_000_000))
print(sys.getsizeof(gen_expr))  # 208 байт!!!


# Typehints для генераторов
"""

Во-первых, вы не сможете просто так взять и аннотировать тип генератора. Эту штуку нужно импортировать из модуля `typing` — то есть сделать явный импорт.

Аннотация типа генератора внутри квадратных скобок дает три позиции. Первая позиция — это какой тип данных генератор отдаст наружу. Вторая позиция — какой тип данных генератор принимает вовнутрь. Здесь такой интересный момент, что он может принимать вовнутрь параметр при обращении к нему.

То есть, когда он уже будет работать, мы можем подавать туда какие-то значения. И третья позиция — какой тип данных генератор возвращает в самом конце.

То есть технически у него может быть еще что-то вроде `return`.
"""

"""
Generator[ЧТО ОТДАЕТ, ЧТО ПОЛУЧАЕТ ВО ВРЕМЯ РАБОТЫ, ЧТО ВОЗВРАЩАЕТ В КОНЦЕ]
"""


# В 95% случаев мы используем Generator[int, None None]
def simple_gen() -> Generator[int, None, None]:
    yield 1
    yield 2
    yield 3


# Второй параметр - как подать данные в Generator


def accumulator() -> Generator[int, int, None]:
    total = 0
    while True:
        # yield отдает текущий total, но может принять значение извне через .send() в переменную value
        value = yield total
        if value is not None:
            total += value


acc = accumulator()
next(acc)  # Получим 0
print(acc.send(10))  # Стал 10 вернет 10
print(acc.send(5))  # Стал 15 вернет 15
print(acc.send(-1))

"""
Внутри, «под капотом» Python, просто вызов функции `next()` является `send(None)`. Поэтому, если в этом конкретном случае я пытаюсь сделать `next()`, это будет означать, что я передаю `None`, на что Python падает с ошибкой: я не могу складывать `None` с числами.

Поэтому мы будем падать с ошибкой при попытке сделать `next()` именно на 111-й строке, где происходит операция сложения. Однако же, если я хочу просто потихонечку начать разряжать этот аккумулятор, я могу сделать `send(-1)` и фактически буду уменьшать это число, разряжая аккумулятор.
"""


def simple_gen2() -> Generator[int, None, str]:
    yield 1
    yield 2
    yield 3
    return "Парам-парам-пам!"


for i in simple_gen2():
    print(i)

sg2 = simple_gen2()

try:
    print(next(sg2))
    print(next(sg2))
    print(next(sg2))
    print(next(sg2))
except StopIteration as e:
    print(e)


proverbs = [
    "Ум хорошо, а два лучше.",
    "Ум — горячая штука.",
    "Ум всё голова.",
    "Умом Россию не понять.",
    "Ум бережет, а глупость губит.",
    "Ум в голову приходит.",
    "Ум от ума не горит.",
    "Умом нагружен, а волосы развеваются.",
    "Умом обдумал, а ногами пошел.",
    "Ум — сокровище, не пропадет без него и копье на ветру.",
    "Ум — грех, а бес — мера.",
    "Ум есть богатство.",
    "Ум роднит народы.",
    "Ум краток, да забот — бездна.",
    "Ум не камень, взял и положил.",
    "Ум не велит, а наставляет.",
    "Ум с мерой, а глупость без меры.",
    "Ум — сокол, глаз его — телескоп.",
    "Ум — не конская морда, не разобьешь.",
    "Ум — семь пядей во лбу.",
    "Ум — не барсук, в нору не залезет.",
    "Ум в голове, а не на ветру.",
    "Ум греет душу, а глупость терпение.",
    "Ум служит человеку, а глупость — хозяином.",
    "Ум мил, да безумству хозяин.",
    "Ум в труде, да наслаждение в праздности.",
    "Ум глаза исправляет.",
    "Ум человека не обманешь.",
    "Ум на подобии огня — без сна не останешься.",
    "Ум к уму приходит.",
    "Ум с пользой тратит время.",
    "Ум желание творит.",
    "Ум общего дела дело.",
    "Ум — друг, а воля — враг.",
    "Ум — бесценное сокровище.",
    "Ум тонок, да разум невелик.",
    "Ум — враг бедности.",
    "Ум — теремок, да не на прокол.",
    "Ум силен, да не камень.",
    "Ум рассудит, что сердце не посоветует.",
    "Ум — подкова, а топор — ось.",
    "Ум легче камня, да весомей золота.",
    "Ум не вешать на гроздья.",
    "Ум — не мешок, на плечи не вешай.",
    "Ум — лучшая победа.",
    "Ум — в суде велик, а в деле своем мал.",
    "Ум голове краса.",
    "Ум — сокровище, а глупость — нищета.",
    "Ум человека — огонь, а глаза — масло.",
    "Ум — путь, а дорога — конец.",
    "Ум стоит денег.",
    "Ум от смеха бьет в ладоши.",
    "Ум — коза, к барскому плечу привыкает.",
    "Ум — лезвие, а лень — ржавчина.",
    "Ум на вершине — мир в руках.",
]
variants = [
    "кот",
    "шеф",
    "мозг",
    "лес",
    "фолк",
    "код",
    "рот",
    "мёд",
    "лук",
    "год",
    "час",
    "друг",
    "жена",
    "муж",
    "айфон",
    "работа",
]

from random import choice


def proverb_gen_1() -> Generator[str, None, int]:
    iter_count = 0
    proverbs_limit = len(proverbs) * len(variants)
    used_variants = []

    while len(used_variants) < proverbs_limit:
        iter_count += 1
        print(f"Попытка №{iter_count}")
        proverb = choice(proverbs)
        variant = choice(variants)
        new_proverb = proverb.replace("Ум", variant)

        if new_proverb not in used_variants:
            used_variants.append(new_proverb)
            yield new_proverb

    return iter_count


def proverb_gen_2() -> Generator[str, None, int]:
    iter_count = 0
    
    for var in set(variants):
        for proverb in set(proverbs):
            new_proverb = proverb.replace("Ум", var)
            iter_count += 1
            yield new_proverb
    
    return iter_count

pg1 = proverb_gen_1()
pg2 = proverb_gen_2()
for i in range(5):
    print(next(pg1))

for i in range(5):
    print(next(pg2))