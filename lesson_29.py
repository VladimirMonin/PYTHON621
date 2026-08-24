"""
Lesson 29 - инкапсуляция данных в классах
_
__
@property
__dict__

"""


class Car:
    def __init__(self, model: str, max_speed: int):
        self.model = model
        self.__max_speed = max_speed
        self.speed = 0


    def start(self):
        self.gas_controller()
        print("Запуск двигателя!")

    def beep(self):
        print("Бип-бип!")

    def wheel(self, direction: str):
        print(f"Крутим руль в {direction}")

    def __gas_controller(self):
        print("Управление системой подачи топливом")

    def __str__(self):
        return(f"Модель {self.model}, Максимальная скорость {self.__max_speed} км/ч")



car1 = Car("Лада Малина", 200)

# print("Максимальная скорость автомобиля", car1.__max_speed)
# Таки пробуем добыть недобываемое

print("Максимальная скорость автомобиля", car1._Car__max_speed)

# car1.__gas_controller()
print(car1)

car1.__max_speed = 400
print(car1)
car1.start()

