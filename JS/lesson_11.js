// Lesson 11: For Loops
// 0. Ведро с картошкой
// 1. Берем картошку
// 1.1 Проверяем - гнилая или нет?
// 2. Чистим картошку
// 3. Кладем картошку в ведро
// 4. Проверяем что почистили достаточно. Если нет, чистим дальше.

// Итеративность - iteration - повторение
// iterable - итерируемый - такой, который можно повторять
// строка = "1234 45;% АбВ"
// массив = [1, 2 , "хлебушек", [1 , 2, 4]]

let potatosBasket = [
  "картошка 1",
  "картошка 2 Гнилая",
  "картошка 3",
  "картошка 4 ППЦ КАКАЯ ГНИЛАЯ",
  "картошка 5",
  "картошка 6",
  "картошка 7 гнилая",
];
console.log(potatosBasket);

// Цикл for - перебор
// Цикл while - пока условие выполняется

// Самый простой цикл for в современном JS
// Перебор картошки в ведре
// for (let potato of potatosBasket) {
//   console.log(potato);
// }
// let counter = 0;
// for (let potato of potatosBasket) {
//   console.log(`Проверяем ${potato} №${counter}`);
//   counter++;
// }

// ++ - инкремент - увеличение на единицу
// -- - декремент - уменьшение на единицу
// полная запись counter = counter + 1;

// Обходим всю картошку и считаем хорошую
let goodPotatos = 0;

for (let potato of potatosBasket) {
  console.debug(`Проверяем ${potato}`);
  if (potato.toLowerCase().includes("гнилая")) {
    console.log(`Выбрасываем ${potato}`);
  } else {
    console.log(`Кладем ${potato} в ведро`);
    goodPotatos++;
  }
}
console.debug("Цикл закончился");
console.log(`Всего хорошей картошки: ${goodPotatos}`);

// Методы массивов
// push - добавляет элемент в конец массива
// pop - удаляет последний элемент массива и возвращает его
// unshift - добавляет элемент в начало массива
// shift - удаляет первый элемент массива и возвращает его
// includes - проверяет наличие элемента в массиве и возвращает true или false
// indexOf - возвращает индекс элемента в массиве или -1, если элемент не найден
// slice - возвращает новый массив, содержащий копию части исходного массива
// splice - изменяет содержимое массива, удаляя или заменяя существующие элементы и/или добавляя новые элементы на месте
// join - объединяет все элементы массива в строку, используя указанный разделитель
// split - разбивает строку на массив подстрок, используя указанный разделитель
// forEach - выполняет указанную функцию один раз для каждого элемента массива
// map - создает новый массив с результатом вызова указанной функции для каждого элемента массива
// filter - создает новый массив со всеми элементами, которые прошли проверку, задаваемую в передаваемой функции

let productsCart = [];
// push - добавляет элемент в конец массива
productsCart.push("хлеб");
productsCart.push("молоко");
productsCart.push("масло");
console.log(productsCart);

// unshift - добавляет элемент в начало массива
productsCart.unshift("яйца");
console.log(productsCart);

let lastItem = productsCart.pop(); // удаляет последний элемент массива и возвращает его
console.log(productsCart);
console.log(`Удаленный элемент: ${lastItem}`);

// join - объединяет все элементы массива в строку, используя указанный разделитель
let productsString = productsCart.join(", ");
console.log(productsString);

// split - разбивает строку на массив подстрок, используя указанный разделитель
let productsArray = productsString.split(", ");
console.log(productsArray);

productsCart.push("мЯски");
productsCart.push("кОлбаски");
productsCart.push("сЫр");
console.log(productsCart);

// Обойти это и сделать нижним регистром
// Вариант 1 - цикл

let optimizedProductsCart = [];
for (let product of productsCart) {
  optimizedProductsCart.push(product.toLowerCase());
}
console.log(optimizedProductsCart);

// Индексы
console.log(productsCart[0]); // первый элемент

productsCart.push("мяски")
productsCart.push("мяски")

// indexOf - возвращает индекс элемента в массиве или -1, если элемент не найден
console.log(productsCart)
console.log(productsCart.indexOf("мяски")); // 4 - индекс первого вхождения элемента