from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from tabulate import tabulate

from cities import cities_list


# Создается служебный объект консоли
console = Console()


def print_city_info(city_name, city_data):
    # Rich: Panel красиво оформляет справку по выбранному городу.
    console.print(
        Panel.fit(
            f"Население: [bold]{city_data['population']}[/]\n"
            f"Регион: [bold]{city_data['district']}[/]\n"
            f"Округ: [bold]{city_data['subject']}[/]",
            title=f"[cyan]{city_name}[/]",
            border_style="cyan",
            box=box.ASCII,
        )
    )


def print_turn_title(title, color):
    # Rich: Rule делает красивый визуальный переход между ходами.
    console.print(Rule(f"[bold {color}]{title}[/]", style=color))


# from data.cities import cities_list
console.print(
    f"[green]Мы подключили датасет на[/] [bold]{len(cities_list)}[/] [green]городов[/]"
)

# Делаем сет городов для удобства работы
cities_set = {city["name"] for city in cities_list}

# Делаем альтернативную коллекцию для более быстрой работы (словарь словарей) - Пайтон не будет делать перебор при проверке на вхождение
city_by_name = {city["name"]: city for city in cities_list}

computer_cities = []
humans_cities = []
game_rounds = []
computer_city = ""
round_counter = 0
help_prompts_list = ["хелп", "хэлп", "help", "подсказка", "памагите", "помогите"]

while True:
    print_turn_title("Ход человека", "green")
    user_city = input("Введите название города: ").strip()

    if user_city.lower() in help_prompts_list:
        console.print(
            "[yellow]Ха-ха! Кожаному нужна помощь![/]\n[cyan]Держи пять городов![/]"
        )
        need_letter = computer_city[-1].lower() if computer_city else ""
        help_list = [
            city
            for city in cities_set
            if not need_letter or city[0].lower() == need_letter
        ][:5]
        console.print(help_list)
        user_city = input("Введите название города: ").strip()

    # Проверка что город есть в сете
    if user_city not in cities_set:
        console.print("[bold red]Кожаный мешок! Ты проиграл![/]")
        console.print("[red]Такого города НЕТ в сете с данными![/]")
        break

    if computer_city:
        # Проверка правил игры
        if computer_city[-1].lower() != user_city[0].lower():
            console.print("[bold red]Кожаный мешок! Ты проиграл![/]")
            console.print("[red]Ты нарушил правила игры![/]")
            break

    # Даем справку по городу
    city_data_by_name = city_by_name[user_city]
    print_city_info(user_city, city_data_by_name)

    # Удаляем город человека из сета
    cities_set.remove(user_city)
    humans_cities.append(user_city)

    print_turn_title("Ход компьютера", "magenta")

    # Переходим к ходу компьютера
    # Если бы это было однострочником? [city for city in cities_set if city[0].lower() == user_city[-1]]
    for city in cities_set:
        if city[0].lower() == user_city[-1].lower():
            computer_city = city
            console.print(
                f"[magenta]Компьютер выбрал город:[/] [bold]{computer_city}[/]"
            )

            # Даем справку по городу
            city_data_by_name = city_by_name[city]
            print_city_info(city, city_data_by_name)
            break
    else:
        # Сюда попадем только в том случае если break не случился в цикле for
        console.print(
            "[bold green]Кожаный мешок, ты выиграл! Я не могу найти город![/]"
        )
        break

    # Увеличиваем счетчик ходов
    round_counter += 1
    cities_set.remove(computer_city)
    computer_cities.append(computer_city)
    game_rounds.append([round_counter, user_city, computer_city])

print_turn_title("Статистика по игре", "blue")

# Tabulate: выводим историю ходов в виде аккуратной таблицы.
console.print(
    tabulate(
        game_rounds,
        headers=["Ход", "Человек", "Компьютер"],
        tablefmt="grid",
    )
)

stats_table = [
    ["Человек", len(humans_cities), ", ".join(humans_cities) if humans_cities else "-"],
    [
        "Компьютер",
        len(computer_cities),
        ", ".join(computer_cities) if computer_cities else "-",
    ],
    ["Осталось городов", len(cities_set), "-"],
]

# Tabulate: выводим итоговую статистику игроков и оставшихся городов.
console.print(
    tabulate(
        stats_table,
        headers=["Показатель", "Количество", "Города"],
        tablefmt="grid",
    )
)
console.print(f"[bold blue]Количество полных ходов:[/] {round_counter}")
