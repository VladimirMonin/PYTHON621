"""
Lesson 31: Полиморфизм  и наследование
- Полиморфизм как взаимозаменяемость экземпляров разных классов
"""


class Document:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def open(self):
        print(f"Метод open из Document")

    def show_path(self):
        print(f"Путь к файлу: {self.file_path}")


class MarkdownDocument(Document):
    def open(self):
        super().open()
        # Document.open(self) ВОТ ЭТО ЗАМЕНА СУПЕР
        print(f"MarkdownDocument имеет расширенный метод open!")


class TxtDocument(Document):
    def open(self):
        print(f"TxtDocument имеет свой метод open!")


class WordDocument(Document): ...


md_1 = MarkdownDocument("example.md")
txt_1 = TxtDocument("example.txt")
wd_1 = WordDocument("example.docx")

documents = [md_1, txt_1, wd_1]

for doc in documents:
    doc.open()


print(MarkdownDocument.mro())
