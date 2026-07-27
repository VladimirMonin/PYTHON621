// Функции в JS

// Функция - это блок кода, который выполняет определенную задачу и может быть повторно использован в программе. Функции позволяют организовать код, сделать его более читаемым и поддерживаемым.

// Стиль объявления функции в JavaScript:
// function имя_функции(параметры) {
//     // тело функции
// }

// Правила нейминга функций:
// 1. Имена функций должны быть описательными и отражать их назначение.
// 2. lowerCamelCase с глаголом в начале (например, calculateSum, getUserData).

function logHello() {
  // Тело функции - это код, который выполняется при вызове функции
  console.log("Hello, World!");
}
logHello(); // Вызов функции

let result = logHello(); // Вызов функции и сохранение результата в переменной
console.log(result); // undefined, так как функция не возвращает значение

let result2; // - ТОЖЕ будет undefined, т.е. без значения, так как функция не возвращает значение

function getHello() {
  return "Hello, World!"; // Возвращаемое значение функции
}

let result3 = getHello(); // Вызов функции и сохранение возвращаемого значения в переменной
console.log(result3); // "Hello, World!"

// Функция с параметрами
function greetByName(name) {
  return `Hello, ${name}!`; // Используем шаблонные строки для вставки значения параметра
}
let greeting = greetByName("Глубокослав"); // Вызов функции с аргументом
console.log(greeting); // "Hello, Глубокослав!"

// Функция с несколькими параметрами
function greetByFullName(firstName, lastName) {
  return `Hello, ${firstName} ${lastName}!`;
}

let fullGreeting = greetByFullName("Океания", "Подкредитная");
console.log(fullGreeting); // "Hello, Океания Подкредитная!"

// Функция которая рендерит список
let ulElement = document.getElementById("myList");

function renderList(items) {
  ulElement.innerHTML = ""; // Очищаем существующий список

  for (let item of items) {
    let liElement = document.createElement("li");
    liElement.textContent = item; // Устанавливаем текст элемента списка
    ulElement.appendChild(liElement); // Добавляем элемент в список
  }
}

let fruits = ["Яблоко", "Банан", "Апельсин"];
renderList(fruits); // Вызов функции для рендеринга списка фруктов

function askUsersFruits() {
  let userFruits = prompt("Введите ваши любимые фрукты через запятую:");
  if (userFruits) {
    let fruitsArray = userFruits.split(",");
    return fruitsArray;
  } else {
    return [];
  }
}

// Функция на кнопку которая запустит логику
function handleButtonClick() {
  let userFruits = askUsersFruits();
  // Тут МОЖЕТ быть скрипт, нет смысла паковать ВСЕ в функции!!!!
  renderList(userFruits);
}

// Простая функция валидатор на длину слова
function validateWordLength(word, minLength) {
  if (word.length >= minLength) {
    return true; // Слово валидно
  } else {
    return false; // Слово не валидно
  }
}

let wordToValidate = "Привет";
let isValid = validateWordLength(wordToValidate, 5);

if (isValid) {
  console.log("Слово валидно.");
} else {
  console.log("Слово не валидно.");
}

if (validateWordLength(wordToValidate, 5)) {
  console.log("Слово валидно.");
} else {
  console.log("Слово не валидно.");
}
