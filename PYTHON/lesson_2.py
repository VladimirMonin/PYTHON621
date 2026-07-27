# Lesson 1
print("Привет, мир!")

# Комментарий - это строка, которая не выполняется, а служит для пояснения кода. Она начинается с символа # и продолжается до конца строки.

# Правила нейминга переменных:
# 1. Никаких пробелов, спецсимволов и знаков препинания, кроме подчеркивания (_).
# 2. Нельзя начинать имя переменной с цифры.
# 3. Существительные и прилогательные для переменных, глаголы для функций.
# 4. Используется стиль snake_case для переменных и функций (например, my_variable, calculate_sum).

my_message = "Привет, мир!"
print(id(my_message))  # Выводит уникальный идентификатор объекта в памяти

my_message2 = "Привет, мир!"
print(id(my_message2))  # Выводит уникальный идентификатор объекта в памяти

my_full_name = "Монин" + " " + "Владимир" + " " + "Александрович"

first_name = "Владимир"
last_name = "Монин"
middle_name = "Александрович"

my_full_name2 = f"{first_name} {last_name} {middle_name * 2}"
print(my_full_name)
print(my_full_name2)

print("---" * 10)

# Типы данных в Python:
# 1. Числа (int, float)
# 2. Строки (str)
# 3. Логические значения (bool)
# 4. Списки (list)
# 5. Кортежи (tuple)
# 6. Множества (set)
# 7. Словари (dict)
# 8. NoneType (None)

# int - integer (целые числа)
# float - floating-point number (числа с плавающей запятой)

a = 9
b = 2

print(a + b)  # Сложение
print(a - b)  # Вычитание
print(a * b)  # Умножение
print(a / b)  # Деление (Даст float в любом случае)
print(a // b)  # Целочисленное деление (Даст int)
print(a % b)  # Остаток от деления
print(a**b)  # Возведение в степень

user_time = input("Введите время в миллисекундах: ")
user_time_int = int(user_time)  # Преобразуем строку в целое число

seconds = user_time_int // 1000
minutes = seconds // 60
hours = minutes // 60

print(seconds)
print(minutes)
print(hours)

print("---" * 10)
# Получим нормальные данные)))
user_time = input("Введите время в миллисекундах: ")
ms = int(user_time)  # Преобразуем строку в целое число

total_seconds = ms // 1000
seconds = total_seconds % 60
minutes = (total_seconds // 60) % 60
hours = (total_seconds // 3600) % 24
days = total_seconds // 86400

print(f"{days} дней, {hours} часов, {minutes} минут, {seconds} секунд")
