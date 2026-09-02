"""
Lesson 32: Абстрактные классы
- is и ==
- Множественное наследование, ромб и MRO
- Кооперативный `super()` и mixin-классы
"""

from os import name


class Matryoska:
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f"Матрешка {self.name}"


class MaterialMetalMixin:
    def __init__(self, name):
        super().__init__(name)
        self.material = "металл"

    def __str__(self):
        return f"{super().__str__()} из материала {self.material}"


class TalkingMixin:
    def __init__(self, name):
        super().__init__(name)
        self.feat = "говорит"
        self.phrase = "Сделаем Америку Грейт Агейн!"

    def change_words(self, new_phrase):
        self.phrase = new_phrase

    def speak(self):
        return f"{self.name} {self.feat}: {self.phrase}"

    def __str__(self):
        return f"{super().__str__()} Говорящая! {self.feat}: {self.phrase}"


class RhinestoneMixin:
    def __init__(self, name):
        super().__init__(name)
        self.decoration = "стразы"

    def __str__(self):
        return f"{super().__str__()} украшена {self.decoration}"


class MatryoskaSpecialEdition(
    TalkingMixin, RhinestoneMixin, MaterialMetalMixin, Matryoska
): ...


tramp_matryoska = MatryoskaSpecialEdition("Трамп")
tramp_matryoska.change_words("Make America Great Again!")
print(tramp_matryoska.speak())

print(tramp_matryoska)


medved_matryoska = MatryoskaSpecialEdition("Медведев")
medved_matryoska.change_words("Денег нет, но вы держитесь!")
print(medved_matryoska.speak())

print(medved_matryoska)

for cls in MatryoskaSpecialEdition.__mro__:
    print(cls)