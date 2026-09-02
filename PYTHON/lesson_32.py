"""
Lesson 32: Абстрактные классы
- is и ==
- Множественное наследование, ромб и MRO
- Кооперативный `super()` и mixin-классы
"""


class Matryoska:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Матрешка {self.name}"


class MaterialMetalMixin:
    def __init__(self):
        self.material = "металл"

    def __str__(self):
        return f"Матрешка {self.name} из {self.material}"


class TolkingMixin:
    def __init__(self):
        self.feat = "говорит"
        self.phrase = "Сделаем Америку Грейт Агейн!"

    def change_words(self, new_phrase):
        self.phrase = new_phrase

    def voice_bottom(self):
        return f"{self.name} {self.feat}: {self.phrase}"

    def __str__(self):
        return f"Матрешка {self.name} {self.feat}: {self.phrase}"


class MetallicMatryoska(Matryoska, MaterialMetalMixin, TolkingMixin):
    def __init__(self, name):
        Matryoska.__init__(self, name)
        MaterialMetalMixin.__init__(self)
        TolkingMixin.__init__(self)

    def __str__(self):
        return f"Матрешка {self.name} из {self.material} {self.feat}: {self.phrase}"


tramp_matryoska = MetallicMatryoska("Трамп")
tramp_matryoska.change_words("Make America Great Again!")
print(tramp_matryoska.voice_bottom())

medved_matryoska = MetallicMatryoska("Медведев")
medved_matryoska.change_words("Денег нет, но вы держитесь!")
print(medved_matryoska.voice_bottom())
