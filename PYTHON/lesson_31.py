"""
Lesson 31: Полиморфизм  и наследование
- Полиморфизм как взаимозаменяемость экземпляров разных классов
"""


class Document:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.special: str = "Специальный общий параметр"
        self.validate_path()

    def open(self):
        print(f"Метод open из Document")

    def show_path(self):
        print(f"Путь к файлу: {self.file_path}")

    def validate_path(self):
        if len(self.file_path) < 3:
            raise ValueError("Название файла слишком короткое")
        return True



class MarkdownDocument(Document):
    def __init__(self, file_path: str, encoding: str):
        # self.file_path = file_path
        # self.encoding = encoding

        self.encoding = encoding
        super().__init__(file_path)

    def open(self):
        super().open()
        # Document.open(self) ВОТ ЭТО ЗАМЕНА СУПЕР
        print(f"MarkdownDocument имеет расширенный метод open!")


class TxtDocument(Document):
    def open(self):
        print(f"TxtDocument имеет свой метод open!")


class WordDocument(Document): ...

md_1 = MarkdownDocument("!", "utf-8")
md_1.show_path()
print(md_1.special)