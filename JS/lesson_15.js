console.debug("Подключен файл lesson_15.js");

let catName = "Котомир";
console.log(catName);
function greetByName() {
  let catName = "Шустролап";
  console.log(`Привет, ${catName}!`); // Локальная переменная name внутри функции
}
// greetByName(); // Вызов функции, которая использует локальную переменную name
// console.log(catName);

// Экспорт функции для использования в другом файле
export { greetByName, catName };
