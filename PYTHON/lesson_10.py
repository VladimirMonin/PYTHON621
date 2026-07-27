# Урок №10

from marvel import movies, movie_titles, movie_descriptions
from pprint import pprint
# from marvel import * - импорт всех переменных из модуля marvel.py - плохо, вы не знаете что импортировано

print(f"Количество фильмов: {len(movie_titles)}")

# List Comprehension - списковые выражения

# 1 - Просто перебор исходника
movies_titles_1 = [movie for movie in movie_titles]

# 2 - Замена "паук" на биляш
movies_title_2 = [movie.replace("паук", "бeляш") for movie in movie_titles]

# 3 - Фильтрация всех "человеков"
movies_title_3 = [movie for movie in movies_title_2 if "человек" in movie.lower()]
print(movies_title_3)

# Пробуем обход словаря. Поищем в значениях
search_str = input("Введите поисковую фразу").lower()
result = {}

for key, value in movie_descriptions.items():
    if search_str in value.lower() or search_str in key.lower():
        result[key] = value

pprint(result)

# Сделаем ключи нижним регистром + замена пробелов и уберем :
result = {}

for title, description in movie_descriptions.items():
    new_title = title.replace(" ", "_").replace(":", "").lower()
    result[new_title] = description

pprint(result, sort_dicts=False)

# Dict comprehension - словарные выражения

# 1. Просто перебор исходника
new_movie_descriptions = {
    title: description for title, description in movie_descriptions.items()
}

# 2. Реплейс в ключе пробел на _
new_movie_descriptions = {
    title.replace(" ", "_"): description
    for title, description in movie_descriptions.items()
}

# 3. Поиск
search_str = input("Введите поисковую фразу").lower()
new_movie_descriptions = {
    title: description
    for title, description in movie_descriptions.items()
    if search_str in title.lower()
}

# 4. Попробуйте сделать такой же фильтр по вхождению ИЛИ в заголовок ИЛИ в описание
#####

# СПИСОК СЛОВАРЕЙ movies
# Просто перебор исходника
new_movies = [movie for movie in movies]

# Заменить None в budget_million_usd и box_office_worldwide_million_usd на 0
clear_movies = [
    {
        "key": movie["key"],
        "order": movie["order"],
        "title": movie["title"],
        "year": movie["year"],
        "release_date": movie["release_date"],
        "release_region": movie["release_region"],
        "phase": movie["phase"],
        "phase_name": movie["phase_name"],
        "saga": movie["saga"],
        "status": movie["status"],
        "is_released": movie["is_released"],
        "franchise": movie["franchise"],
        "directors": movie["directors"],
        "screenwriters": movie["screenwriters"],
        "producers": movie["producers"],
        "budget_million_usd": 0
        if movie["budget_million_usd"] is None
        else movie["budget_million_usd"],
        "box_office_worldwide_million_usd": 0
        if movie["box_office_worldwide_million_usd"] is None
        else movie["budget_million_usd"],
        "notes": movie["notes"],
    }
    for movie in movies
]

clear_movies = [
    {
        **movie,
        "budget_million_usd": 0
        if movie["budget_million_usd"] is None
        else movie["budget_million_usd"],
        "box_office_worldwide_million_usd": 0
        if movie["box_office_worldwide_million_usd"] is None
        else movie["box_office_worldwide_million_usd"],
    }
    for movie in movies
]
pprint(clear_movies)

# Фильтр. Мы делаем перебор словарей. Фильтруем по budget_million_usd < 100
# new_movies = [movie for movie in movies if movie["budget_million_usd"] > 200]
# print(new_movies)

# # Фильтр. заголовок содержит "человек"
# new_movies = [movie for movie in movies if "человек" in movie["title"].lower()]
# pprint(new_movies)
