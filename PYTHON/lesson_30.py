"""

# ======================================================================
# Специальные методы арифметики в Python
# ======================================================================
#
# ОБЫЧНЫЕ ОПЕРАЦИИ (+, -, *, /)
# Каноничное поведение: создают и возвращают НОВЫЙ объект,
# исходные операнды не меняются.
#   __add__      -> a + b
#   __sub__      -> a - b
#   __mul__      -> a * b
#   __truediv__  -> a / b  (истинное деление, результат float)
#
# IN-PLACE ОПЕРАЦИИ (+=, -=, *=, /=)
# Каноничное поведение: изменяют объект НА МЕСТЕ (self)
# и по соглашению возвращают этот же объект.
#   __iadd__      -> a += b
#   __isub__      -> a -= b
#   __imul__      -> a *= b
#   __itruediv__  -> a /= b
#
# КЛЮЧЕВАЯ РАЗНИЦА
# 1. Обычные методы ничего не мутируют: они собирают новый экземпляр
#    класса и возвращают его: result = a + b.
# 2. In-place методы мутируют self и возвращают его же — так работает
#    семантика "a += b": изменённый объект снова привязывается к имени a.
# 3. Откат (fallback): если in-place метод не определён, Python
#    выполняет a += b как a = a + b, то есть через обычную операцию
#    с созданием нового объекта.
# 4. Нюанс иммутабельных типов (int, str, tuple): изменить их на месте
#    нельзя, поэтому даже __iadd__ там вынужден вернуть новый объект.
"""
from functools import total_ordering

@total_ordering
class Playlist:
    def __init__(self, name: str):
        self.songs: list = []
        self.name = name

    def add_song(self, *song: str):
        [self.songs.append(single_song) for single_song in song]

    def __str__(self):
        joined_songs = "\n".join(self.songs)
        return f"Плейлист: {self.name}\nКомпозиции:\n{'\n'}" + joined_songs

    def __add__(self, other: Playlist) -> Playlist:
        if not isinstance(other, Playlist):
            raise TypeError("Можно складывать только эекземпляры Playlist")
        new_playlist = Playlist(f"{self.name} + {other.name}")
        new_playlist.songs = self.songs + other.songs
        return new_playlist

    def __iadd__(self, other: Playlist) -> Playlist:
        """
        В отличие от метода `__add__`, метод `__iadd__` в Python отвечает за in-place сложение. Записывается оно как `2 += 2`.

        Это означает, что относительно плейлистов это будет записано как `playlist1 += playlist2`. Таким образом, эта операция по соглашению не создаёт новых экземпляров плейлиста, а видоизменяет левый операнд.
        """
        if not isinstance(other, Playlist):
            raise TypeError("Можно складывать только эекземпляры Playlist")
        self.songs += other.songs
        return self

    def __eq__(self, other: Playlist) -> bool:
        return len(self.songs) == len(other.songs)

    def __lt__(self, other: Playlist) -> bool:
        return len(self.songs) < len(other.songs)





playlist_1 = Playlist("Для прогулок")
playlist_2 = Playlist("Бодрая")

playlist_1.add_song("ДДТ - Что такое осень", "ДДТ - Только рюрмка на столе", "Metallica - Nothing Else Matter")
playlist_2.add_song("Rammstein - Mutter", "Metallica - Ride the Lightning")

print(id(playlist_1))  # 140735524888000
print(id(playlist_2))  # 140735524888040

playlist_3 = playlist_1 + playlist_2
print(id(playlist_3))

print(playlist_3)

playlist_1 += playlist_2
print(id(playlist_1))
print(playlist_1)

print(playlist_1 > playlist_2)
