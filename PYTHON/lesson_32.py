"""
Lesson 32: Абстрактные классы
- is и ==
- Множественное наследование, ромб и MRO
- Кооперативный `super()` и mixin-классы
"""

from abc import ABC, abstractmethod


class AbstractImageFile(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def crop(self):
        pass

    def __str__(self):
        return f"Файл {self.__class__.__name__} с путем {self.file_path}"

    def __eq__(self, other):
        if isinstance(other, AbstractImageFile):
            return self.file_path == other.file_path
        return False


class JpegImageFile(AbstractImageFile):
    def read(self):
        print("Чтение JPEG файла")

    def crop(self):
        print("Обрезка JPEG файла")


class PngImageFile(AbstractImageFile):
    def read(self):
        print("Чтение PNG файла")

    def crop(self):
        print("Обрезка PNG файла")


a_str = "один"
b_str = "один"
c_str = "два"

print(a_str == b_str)  # True
print(a_str is b_str)  # True
print(a_str == c_str)  # False
print(a_str is c_str)  # False

jpeg_file = JpegImageFile("image.jpeg")
jpeg_file_2 = JpegImageFile("image.jpeg")
png_file = PngImageFile("image.png")

print(
    jpeg_file == jpeg_file_2
)  # False НО ЕСЛИ БУДЕТ eq который сверяет по атрибутам, то будет True
print(jpeg_file is jpeg_file_2)  # False

print(jpeg_file == jpeg_file)  # True
print(jpeg_file is jpeg_file)  # True


class BigMatryoshka:
    def __init__(self, name):
        self.big_name = name

    def __str__(self):
        return f"Имя: {self.big_name}"


class MediumMatryoshka(BigMatryoshka):
    def __init__(self, name):
        super().__init__(name)
        self.medium_name = name


class SmallMatryoshka(MediumMatryoshka):
    def __init__(self, name):
        super().__init__(name)
        self.small_name = name


small_matryoska = SmallMatryoshka("Байден Неволяшка")
print(small_matryoska.big_name)  # Байден Неволяшка

# Сделаем проверку на MRO (Method Resolution Order)
print(small_matryoska.__class__.__mro__)  # (<class '__main__.SmallMatryoshka'>, <class '__main__.MediumMatryoshka'>, <class '__main__.BigMatryoshka'>, <class 'object'>)