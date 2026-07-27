// Lesson 13: Objects
// Объекты - это структуры данных, которые позволяют хранить и организовывать данные в виде пар "ключ-значение". Они являются фундаментальной частью JavaScript и широко используются для моделирования реальных объектов и хранения данных.

// Создание объекта
const cat = {
  name: "Кусислав",
  age: 5,
  catType: "Доровой чешир",
  isHungry: true,
  favoreteToys: ["мышь", "мяч", "веревка"],
};

// Доступ к свойствам объекта
console.log(cat.name); // Выводит: Кусислав
console.log(cat["age"]); // Выводит: 5
console.log(cat.favoreteToys); // Выводит: ["мышь", "мяч", "веревка"]

// Доступ можно получить через точку или через квадратные скобки. Квадратные скобки полезны, когда имя свойства хранится в переменной или содержит специальные символы.

// Изменение свойств объекта
cat.isHungry = false; // Изменение значения свойства isHungry
console.log(cat.isHungry); // Выводит: false

// Добавление новых свойств
cat.color = "серый"; // Добавление нового свойства color
console.log(cat.color); // Выводит: серый

// Удаление свойств
delete cat.age; // Удаление свойства age
console.log(cat.age); // Выводит: undefined

// Готовые методы объектов
// keys() - возвращает массив ключей объекта
// values() - возвращает массив значений объекта
// entries() - возвращает массив пар [ключ, значение]
// hasOwnProperty() - проверяет, содержит ли объект определенное свойство

const keys = Object.keys(cat); // ["name", "age", "color"]
console.log("Циклы для объектов:");
for (let key in keys) {
  console.log(`${keys[key]}`); // Выводит все пары ключ-значение объекта cat
}

for (let value of Object.values(cat)) {
  console.log(value); // Выводит все значения объекта cat
}

console.log(`Entries: ${Object.entries(cat)}`); // Выводит все пары ключ-значение объекта cat в виде массива
for (let [key, value] of Object.entries(cat)) {
  console.log(`${key}: ${value}`); // Выводит все пары ключ-значение объекта cat
}

// PRACTICE - Программа введите имя и возраст котика, пока имя != стоп - и программа отрисует в HTML
// Всех котиков которые были введены пользователем
const cats = [];
const catsTableBody = document.getElementById("catsTableBody");

while (true) {
  let newCat = {};
  newCat.name = prompt("Введите имя котика (или 'стоп' для завершения):");
  if (newCat.name.toLowerCase() === "стоп") {
    break;
  }
  newCat.age = prompt("Введите возраст котика:");
  cats.push(newCat);
}

console.debug(cats);
// Отрисовка котиков в HTML
for (let cat of cats) {
  const row = document.createElement("tr");
  const nameCell = document.createElement("td");
  const ageCell = document.createElement("td");
  nameCell.textContent = cat.name;
  ageCell.textContent = cat.age;
  row.appendChild(nameCell);
  row.appendChild(ageCell);
  catsTableBody.appendChild(row);
}
