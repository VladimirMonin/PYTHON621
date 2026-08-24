"""
Lesson 29 - инкапсуляция данных в классах
_
__
@property
__dict__

"""


class Car:
    min_speed_limit = 0
    max_speed_limit = 500

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
        return f"Модель {self.model}, Максимальная скорость {self.__max_speed} км/ч"

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, new_speed: int):
        self.__max_speed = self.__max_speed_vadidator(new_speed)

    def __max_speed_vadidator(self, new_speed: int) -> int:
        if self.min_speed_limit < new_speed < self.max_speed_limit:
            return new_speed
        else:
            raise ValueError(
                f"Максимальная скорость должна быть в диапазоне от {self.min_speed_limit} до {self.max_speed_limit} км/ч"
            )


car1 = Car("Лада Малина", 200)

# print("Максимальная скорость автомобиля", car1.__max_speed)
# Таки пробуем добыть недобываемое

print("Максимальная скорость автомобиля", car1._Car__max_speed)

# car1.__gas_controller()
print(car1)

# car1.__max_speed = 400
print(car1)
# car1.start()

# car1.max_speed = 600
print(car1.max_speed)

print(car1)


import json


class Config:
    required_fields = ["baseURL", "api_key", "model"]
    supported_models = [
        "deepseek/deepseek-v4-flash-vision-exp",
        "z-ai/glm-5.3",
        "google/gemini-3.7-flash",
        "deepseek/deepseek-v4-pro-0813",
        "x-ai/grok-4.6",
    ]
    vision_models = [
        "deepseek/deepseek-v4-flash-vision-exp",
        "google/gemini-3.7-flash",
        "x-ai/grok-4.6",
    ]

    supported_base_urls = ["https://polza.ai/api/v1", "https://openrouter.ai/api/v1"]

    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__baseURL: str = ""
        self.__api_key: str = ""
        self.__model: str = ""
        self.__config_file: dict = {}
        self.__load_config()

    @property
    def baseURL(self):
        return self.__baseURL

    @property
    def api_key(self):
        return self.__api_key

    @property
    def model(self):
        return self.__model


    def __load_config(self):
        with open(self.__file_path, "r", encoding="utf8") as file:
            self.__config_file = json.load(file)

        # Валидация данных
        self.__model_validate()
        self.__base_url_validate()
        self.__set_is_vision_model()

        # Если все хорошо, то сохраняем данные
        self.__baseURL = self.__config_file["baseURL"]
        self.__api_key = self.__config_file["api_key"]
        self.__model = self.__config_file["model"]

    def __model_validate(self):
        if self.__config_file["model"] not in self.supported_models:
            raise ValueError("Выбранная модель не поддерживается")

    def __base_url_validate(self):
        if self.__config_file["baseURL"] not in self.supported_base_urls:
            raise ValueError("Выбранный базовый URL не поддерживается")

    def __set_is_vision_model(self):
        if self.__config_file["model"] in self.vision_models:
            self.is_vision_model = True
        else:
            self.is_vision_model = False


CONFIG_FILE = r"C:\PY\ПРИМЕРЫ КОДА\PYTHON621\PYTHON\config.json"

config = Config(CONFIG_FILE)
print(config.baseURL)
