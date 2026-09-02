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

jpeg_file = JpegImageFile("image.jpeg")
png_file = PngImageFile("image.png")