// Манипуляции с DOM - Lesson 17

// Найти элементы
// getElementById - по ID
// querySelector - по селектору (классы, теги, атрибуты)
// querySelectorAll - по селектору, но возвращает массив

// Создать элемент
// createElement - создает элемент, который еще не добавлен в DOM

// Изменить (добавить, удалить, переместить) элемент
// appendChild - добавляет элемент в конец родителя
// insertBefore - добавляет элемент перед другим элементом
// removeChild - удаляет элемент из родителя
// replaceChild - заменяет один элемент на другой

// Текст и классы и внутренний код
// textContent - текст внутри элемента
// innerHTML - HTML внутри элемента

// classList - список классов элемента
// toggle - добавляет класс, если его нет, и удаляет, если он есть
// add - добавляет класс
// remove - удаляет класс
// contains - проверяет, есть ли класс

// Атрибуты
// getAttribute - получить значение атрибута
// setAttribute - установить значение атрибута
// removeAttribute - удалить атрибут

// ПРИМЕР 1 - ЛОГИЧЕСКАЯ ОШИБКА - ЭЛЕМЕНТЫ НЕ ПОЯВЛЯЮТСЯ В СПИСКЕ ЕСЛИ МЫ УМЕНЬШИЛИ ВЫДАЧУ А ПОТОМ ПЫТАЕМСЯ ЕЕ УВЕЛИЧИТЬ
// let form = document.querySelector("form");

// form.addEventListener("submit", function (event) {
//   event.preventDefault();
// });

// function searchItem() {
//   let listElement = document.getElementById("list");
//   // Ищем форму и блокируем отправку формы

//   let searchInput = document.querySelector("#search");
//   let searchTerm = searchInput.value.toLowerCase();

//   let items = listElement.querySelectorAll("li");

//   // Фильтруем элементы списка
//   let filteredItems = [];
//   items.forEach((item) => {
//     if (item.textContent.toLowerCase().includes(searchTerm)) {
//       filteredItems.push(item);
//     }
//   });

//   // Очищаем список
//   listElement.innerHTML = "";

//   // Добавляем отфильтрованные элементы обратно в список
//   filteredItems.forEach((item) => {
//     listElement.appendChild(item);
//   });
// }

// Пример №3 - Фильтрация таблицы

let form = document.querySelector("form");

form.addEventListener("submit", function (event) {
  event.preventDefault();
});

function searchItem() {
  let listElement = document.getElementById("list");
  // Ищем форму и блокируем отправку формы

  let searchInput = document.querySelector("#search");
  let searchTerm = searchInput.value.toLowerCase();

  let items = listElement.querySelectorAll("li");

  // Скрываем \ отображаем элементы списка через style.display
  items.forEach((item) => {
    if (item.textContent.toLowerCase().includes(searchTerm)) {
      item.style.display = ""; // Показываем элемент
    } else {
      item.style.display = "none"; // Скрываем элемент
    }
  });
}

// Практика 3 - Фильтрация таблицы
let nameSearch = document.querySelector("#nameSearch");
let studentsTable = document.querySelector("#studentsTable > tbody");
let studentsTableRows = studentsTable.querySelectorAll("tr");

// Блокируем отправку формы
nameSearch.addEventListener("submit", function (event) {
  event.preventDefault();
});

nameSearch.addEventListener("input", function () {
  let searchTerm = nameSearch.value.toLowerCase();

  //   Идем циклом по rows и скрываем \ показываем строки через style.display
  for (let row of studentsTableRows) {
    // Номер
    let number = row.querySelector("td:nth-child(1)").textContent.toLowerCase();
    // Имя
    let name = row.querySelector("td:nth-child(2)").textContent.toLowerCase();
    // Фамилия
    let surname = row
      .querySelector("td:nth-child(3)")
      .textContent.toLowerCase();
    // Отчество
    let patronymic = row
      .querySelector("td:nth-child(4)")
      .textContent.toLowerCase();

    if (
      number.includes(searchTerm) ||
      name.includes(searchTerm) ||
      surname.includes(searchTerm) ||
      patronymic.includes(searchTerm)
    ) {
      row.style.display = ""; // Показываем строку
    } else {
      row.style.display = "none"; // Скрываем строку
    }
  }
});
