// Строки в JS
// Строки оформляются в кавычки
// string - строка
// конвертация в строку - String(значение)
// строка это неизменяемая итерируемая последовательность символов

let string1 = "Привет, мир!";

// Конкатенация строк - склеивание строк
let string2 = "Привет, " + "мир!";

// Шаблонные строки - позволяют вставлять переменные и выражения внутрь строки
let name = "Алиса";
let greeting = `Привет, ${name}!`; // Привет, Алиса!

// Свойства имеющиеся у строк
console.log(string1.length); // 12 - длина строки
console.log(string1[0]); // П - первый символ строки
console.log(string1[string1.length - 1]); // ! - последний символ строки

//
let letterTwo = string1[1]; // р - второй символ строки
string1[1] = "а"; // строка неизменяемая, поэтому это не сработает

// Методы строк

let favoriteProduct = "ШаВерМа";
// Проверка не проходит. Буквы Ш b ш и остальные буквы РАЗНЫХ регистров имеют РАЗНЫЕ цифры в таблице кодирования. А сравнение происходит именно по этим цифрам. Поэтому результат false
console.log(favoriteProduct == "шаверма");

let optimizedFavoriteProduct = favoriteProduct.toLowerCase(); // оптимизированная строка для сравнения
console.log(optimizedFavoriteProduct == "шаверма"); // true

// Серия преобразований
let favoriteProduct2 = " Ша Вер Ма ";
// Последняя замена не произойдет, потому что у нас на этот момент уже не будет больших букв «ш».
let optimizedFavoriteProduct2 = favoriteProduct2
  .toLowerCase()
  .replaceAll(" ", "")
  .replaceAll("а", "о")
  .replaceAll("Ш", "ф");
console.log(optimizedFavoriteProduct2);

// Вариант 1
let approvedPersons = "вася маша коля";
let userName = prompt("Введите ваше имя");
let optimizedUserName = userName.toLowerCase().replaceAll(" ", "");

if (approvedPersons.includes(optimizedUserName)) {
  console.log(`Привет, ${userName}!`);
} else {
  console.log("Привет, Гость!");
}

// Вариант 2 с восстановлением заглавной буквы имени
let approvedPersons2 = "Вася Маша Коля";
let userName2 = prompt("Введите ваше имя");
let rawOptimizedUserName2 = userName2.toLowerCase().replaceAll(" ", "");
let optimizedUserName2 =
  rawOptimizedUserName2[0].toUpperCase() + rawOptimizedUserName2.slice(1);

if (approvedPersons2.includes(optimizedUserName2)) {
  console.log(`Привет, ${optimizedUserName2}!`);
} else {
  console.log("Привет, Гость!");
}

// Array - массив.
// Ссылочная, упорядоченная, итерируемая изменяемая коллекция данных разных типов
let numArray = [1, 2, 3];
let strArray = ["a", "b", "c"];
let mixedArray = [1, "a", true, null, undefined, [1, 2], { name: "Alice" }];


// Проверка концепции ссылочности массивов
let name1 = "Вася";
let name2 = "Денис";
let name3 = "Дарья";

let namesArray = [name1, name2, name3];

let namesString = "Венер, Денис, Дарья, Елена";
let namesArray2 = namesString.split(", "); // Метод split превращает строку в массив, разбивая её по указанному разделителю
console.log(namesArray2); // ["Вася", "Денис", "Дарья"]
// Елена исчезла потому что