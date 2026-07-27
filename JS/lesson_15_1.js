console.debug("Подключен файл lesson_15_1.js");
import { greetByName, catName } from "./lesson_15.js"; // Импорт функции и переменной из другого файла

// let catName = "Котомир";
console.log(catName); // Вывод глобальной переменной catName

// Хочу функцию из другого файла!
greetByName();

// Аргументы функции

console.log("один", "два", "три"); // Вывод нескольких аргументов в консоль

// Массив данных
let numbers = [1, 2, 3, 4, 5];
console.log(...numbers); // Используем оператор spread для передачи элементов массива как отдельных аргументов

// Создание функции с множественными аргументами
function sumManyNumbers(...args) {
  console.log(args); // Вывод массива аргументов
  let finalSum = 0;
  for (let num of args) {
    finalSum += num; // Суммируем все аргументы
  }
  return finalSum; // Возвращаем итоговую сумму
}

let total = sumManyNumbers(1, 2, 3, 4, 5); // Вызов функции с несколькими аргументами
console.log(total); // Вывод результата суммы

let total2 = sumManyNumbers(...numbers); // Вызов функции с использованием spread оператора для передачи массива

// Подстава с типа данных = строки
let products = ["Молоко", "Хлеб", "Яйца"];

let breakfastSum = sumManyNumbers(...products); // Попытка передать строки в функцию, которая ожидает числа
console.log(breakfastSum); // Результат будет NaN, так как строки не могут быть сложены как числа

// Способы объявить функцию
// 1. Function Declaration (Объявление функции)
// Прозрачность, понятность, возможность вызова до объявления

let bananaResult = getBananas(); // Вызов функции до её объявления
console.log(bananaResult); // Вывод результата функции

function getBananas() {
  return "Бананы получены!";
}

// 2. Function Expression (Функциональное выражение)

let getApples = function () {
  return "Яблоки получены!";
};

console.log(getApples()); // Вызов функции после её объявления

// 3. Arrow Function (Стрелочная функция)

let getOranges = () => {
  return "Апельсины получены!";
};

let getOrangesShort = () => "Апельсины получены!"; // Короткая запись стрелочной функции
// Если тело функции состоит из одного выражения, можно опустить фигурные скобки и ключевое слово return
let potatosBasket = [
  "картошка",
  "картошка",
  "картошка",
  "картошка гнилая",
  "картошка",
  "картошка",
  "картошка гнилая",
  "картошка",
  "картошка гнилая",
  "картошка",
  "картошка",
];

// Два варианта. Полноценная функция убрать гнилую картошку через полноценную функцию с циклом и условием. И второй вариант - стрелочная функция.

// Вариант 1 - полноценная функция
function removeRottenPotatoes(...potatoes) {
  let freshPotatoes = [];
  for (let potato of potatoes) {
    if (!potato.includes("гнилая")) {
      freshPotatoes.push(potato);
    }
  }
  return freshPotatoes;
}

let cleanPotatoes = removeRottenPotatoes(...potatosBasket);
console.log(cleanPotatoes);

// Анатомия стрелочной функции:
// 1. Круглые скобки для параметров (можно опустить, если параметр один)
// 2. Стрелка => после параметров
// 3. Фигурные скобки для тела функции (можно опустить, если тело состоит из одного выражения)

// Вариант 2 - стрелочная функция без фильтра =>
potatosBasket.forEach((potato) => {
  if (potato.includes("гнилая")) {
    console.log(`Удаляем ${potato}`);
  }
});

let potatosBasket2 = [
  "картошка",
  "картошка",
  "картошка",
  "картошка гнилая",
  "картошка",
  "картошка",
  "картошка гнилая",
  "картошка",
  "картошка гнилая",
  "картошка",
  "картошка",
];

// Эволюция стрелки!
let removeRottenPotatoesShort = () => console.log("Удаляем гнилые картошки!"); // Стрелочная функция без параметров и с коротким телом
potatosBasket2.forEach(removeRottenPotatoesShort); // Вызов функции для каждого элемента массива
potatosBasket2.forEach((potato) => console.log(`Удаляем ${potato}`)); // Вызов стрелочной функции с параметром для каждого элемента массива

potatosBasket2.forEach((potato) => {
  if (potato.includes("гнилая")) {
    console.log(`Удаляем ${potato}`);
  }
}); // Вызов стрелочной функции с условием для каждого элемента массива

// Вариант со стрелкой и тернарным оператором
potatosBasket2.forEach((potato) => potato.includes("гнилая") ? console.log(`Удаляем ${potato}`) : null); // Вызов стрелочной функции с тернарным оператором для каждого элемента массива