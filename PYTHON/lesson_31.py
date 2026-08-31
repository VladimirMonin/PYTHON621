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


"""
В Python слово type обозначает два тесно связанных, но разных механизма, и различие удобнее всего показать через пару instance и subclass.

Когда речь идёт об instance (экземпляре), type — это встроенная функция: type(obj) возвращает класс, которым объект был создан. Каждый объект в Python хранит ссылку на свой класс, и type просто её читает, поэтому вызов выполняется мгновенно. Функция отвечает на вопрос «чем является этот объект» и не учитывает наследование: type(instance) вернёт именно тот класс, которым объект был создан, а не его базовые классы. Для проверки принадлежности с учётом всей иерархии наследования используют isinstance.

Когда речь идёт о subclass (подклассе), type — это уже не функция-инспектор, а класс-метакласс, который по умолчанию используется для создания новых классов. Каждое объявление вида class Foo(Bar) под капотом вызывает type с тремя аргументами: type(name, bases, namespace), и результатом вызова становится новый класс. Тот же механизм работает и при ручном динамическом создании классов во время выполнения программы.

Таким образом, type в применении к instance даёт возможность узнать фактический класс объекта и работать с ним, а type в применении к subclass даёт контроль над самим процессом порождения классов: перехватывать создание класса, изменять его атрибуты, автоматически регистрировать подклассы и накладывать на них ограничения.
"""


txt_doc = TxtDocument("example.txt")
word_doc = WordDocument("example.word")
md_doc = MarkdownDocument("example.md", "utf-8")

doc = Document("dfsfsf")

print(type(txt_doc))

print(isinstance(md_doc, Document))
print(isinstance(md_doc, MarkdownDocument))
print(isinstance(doc, MarkdownDocument))


print(issubclass(MarkdownDocument, Document))
print(issubclass(Document, MarkdownDocument))