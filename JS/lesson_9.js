// Lesson 9: Знакомство с Bool

// Числа на опыты
let simplePositiveNumber = 5;
let simpleNegativeNumber = -5;
let zero = 0;

// Строки на опыты
let emptyString = "";
let simpleString = "чебурек";
let whiteSpacesString = " ";

// Коллекции на опыты
let emptyArray = [];
let simpleArray = [1, 2, 3];
let emptyObject = {};
let simpleObject = { name: "Alice", age: 30 };

// Приведение к булевому типу
// Number("5") - Приводим строку к числу
// Boolean(5) - Приводим число к булевому типу. Тут может быть ровно 2 позиции true или false

// Числа
console.log(Boolean(simplePositiveNumber)); // true
console.log(Boolean(simpleNegativeNumber)); // true
console.log(Boolean(zero)); // false
// Строки
console.log(Boolean(emptyString)); // false
console.log(Boolean(simpleString)); // true
console.log(Boolean(whiteSpacesString)); // true
// Коллекции
console.log(Boolean(emptyArray)); // true - в JavaScript все массивы являются истинными, даже если они пустые
console.log(Boolean(simpleArray)); // true
console.log(Boolean(emptyObject)); // true - в JavaScript все объекты являются истинными, даже если они пустые
console.log(Boolean(simpleObject)); // true

let userName = prompt("Введите ваше имя:");
if (userName) {
  console.log(`Привет, ${userName}!`);
} else {
  console.log("Привет, редиска!");
}

// Серия проверок

let product = "птица";

if (product == "мясо") {
  console.log("Вы выбрали мясо");
}
if (product == "рыба") {
  console.log("Вы выбрали рыбу");
}
if (product == "птица") {
  console.log("Вы выбрали птицу");
} else {
  console.log("Вы выбрали что-то другое");
}

// Серия проверок 2

let product2 = "птица";

if (product == "мясо") {
  console.log("Вы выбрали мясо");
}
if (product == "птица") {
  console.log("Вы выбрали птицу");
}
if (product == "рыба") {
  console.log("Вы выбрали рыбу");
}
if (product == "птица") {
  console.log("Вы выбрали птицу ОПЯТЬ!");
} else {
  console.log("Вы выбрали что-то другое");
}

// Серия проверок 3

if (product == "мясо") {
  console.log("Вы выбрали мясо");
}
if (product == "птица") {
  console.log("Вы выбрали птицу");
}
if (product == "птица") {
  console.log("Вы выбрали птицу ОПЯТЬ!");
}
if (product == "рыба") {
  console.log("Вы выбрали рыбу");
} else {
  console.log("Вы выбрали что-то другое");
}

// Серия проверок 4

if (product == "мясо") {
  console.log("Вы выбрали мясо");
} else if (product == "птица") {
  console.log("Вы выбрали птицу");
} else if (product == "рыба") {
  console.log("Вы выбрали рыбу");
} else {
  console.log("Вы выбрали что-то другое");
}

// Операторы сравнения
// == - оператор сравнения, который проверяет только значение
// > - оператор сравнения, который проверяет больше ли левый операнд правого
// < - оператор сравнения, который проверяет меньше ли левый операнд правого
// >= - оператор сравнения, который проверяет больше или равно ли левый операнд правого
// <= - оператор сравнения, который проверяет меньше или равно ли левый операнд правого
// != - оператор сравнения, который проверяет неравенство значений

console.log(5 == 5); // true
console.log(5 > 5); // false
console.log(5 < 5); // false
console.log(5 >= 5); // true
console.log(5 <= 5); // true
console.log(5 != 5); // false

console.log(5 == "5"); // true - оператор == приводит строку к числу перед сравнением и оно пройдет успешно
console.log(5 === "5"); // false - оператор === не приводит строку к числу перед сравнением и оно не пройдет успешно, так как типы данных разные
console.log(5 !== "5"); // true - оператор !== не приводит строку к числу перед сравнением и оно пройдет успешно, так как типы данных разные

console.log(5 > "чебурека"); // false (чебурек = NaN, а любое сравнение с NaN возвращает false)

// Логические операторы И (&&) и ИЛИ (||) НЕ (!)
// истина И истина = истина
// истина И ложь = ложь
// ложь ИЛИ истина = истина
// ложь ИЛИ ложь = ложь
// истина ИЛИ ложь = истина
// НЕ ложь = истина
// НЕ истина = ложь
// СКОБОЧКИ

// ПРИОРИТЕТЫ ОПЕРАТОРОВ
// 1. СКОБОЧКИ
// 2. НЕ (!)
// 3. И (&&)
// 4. ИЛИ (||)

// ЕСЛИ: НЕ(ПИЛ ИЛИ КУРИЛ) И ПОМЫЛ_ПОСУДУ = ....

let mark = 22;
if (mark > 0 && mark < 25) {
  console.log("Оценка: 2");
} else if (mark >= 25 && mark < 50) {
  console.log("Оценка: 3");
} else if (mark >= 50 && mark < 75) {
  console.log("Оценка: 4");
} else if (mark >= 75 && mark <= 100) {
  console.log("Оценка: 5");
} else {
  console.log("Некорректная оценка");
}

// Базовая математика
// + - сложение
// - - вычитание
// * - умножение
// / - деление
// % - остаток от деления
// ** - возведение в степень
// ЦЕЛОЧИСЛЕННОЕ_ДЕЛЕНИЕ = Math.floor(5 / 2) - округление вниз до ближайшего целого числа

// Работа со временем. Количество часы по минутам.
let minutes = 135;
let hours = Math.floor(minutes / 60);
console.log(`Часы: ${hours}`); // 2
console.log(`Минуты: ${minutes % 60}`); // 15

// ОДНОСТРОЧНЫЙ ВАРИАНТ IF В JS
// Тернарный оператор
let age = 18;
let canVote = age >= 18 ? "Можете голосовать" : "Не можете голосовать";
console.log(canVote); // Можете голосовать

// Приведение данных к булевому типу
let product3 = "шавуля";
console.log(Boolean(product3)); // true - любая непустая строка является истинной

let someNumber = "0"; // ИЗ промпта мы получаем строку, а не число
console.log(Number(someNumber)); // 0 - строка "0" приводится к числу 0

// Проверка типа данных
console.log(typeof someNumber); // string - someNumber является строкой

// Проверка на ЧИСЛО!
let userInput = prompt("Введите число:");
if (isNaN(userInput)) {
  console.log("Вы ввели не число!");
} else {
  console.log("Вы ввели число!");
}

if (!isNaN(userInput)) {
  console.log("Вы ввели число!");
}
else {
  console.log("Вы ввели не число!");
}

let result = (!isNaN(userInput)) ? "Вы ввели число!" : "Вы ввели не число!";
console.log(result);

isMarried = true;
isStudent = false;
isEmployed = true;
isHappy = isMarried && isEmployed; // true