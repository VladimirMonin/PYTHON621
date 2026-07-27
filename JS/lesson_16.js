// Lesson 16: Functions
// Map vs ForEach
// Они отличаются тем, что map возвращает новый массив, а forEach - нет.

let potatosBasket = [
  "картошка",
  "морковка",
  "лук",
  "зеленый лук",
  "редиска",
  "петрушка",
  "укроп",
  "колбаска",
];

// Смотрим на forEach - он не возвращает новый массив, а просто выполняет функцию для каждого элемента
let workResult1 = potatosBasket.forEach((potato) =>
  console.log(`Почищено: ${potato}`),
);

console.log(workResult1); // - undefined

// Смотрим на map - он возвращает новый массив, который состоит из результатов выполнения функции для каждого элемента
let workResult2 = potatosBasket.map((potato) => `Почищено: ${potato}`);
console.log(workResult2); // - массив с результатами

// Фильтр - он возвращает новый массив, который состоит из элементов, которые прошли проверку, заданную в функции

let badPotatosBasket = [
  "картошка",
  "гнилая картошка",
  "морковка",
  "лук",
  "зеленый лук",
  "редиска",
  "петрушка",
  "укроп",
  "колбаска",
];

let goodVegetables = badPotatosBasket.filter(
  (vegetable) => !vegetable.includes("гнилая"),
);
let goodVegetables2 = badPotatosBasket.filter((vegetable) => {
  return !vegetable.includes("гнилая");
});

console.log(goodVegetables); // - массив без гнилой картошки
console.log(goodVegetables2); // - массив без гнилой картошки

///////////////// DOM знакомство
let productList = document.getElementById("productList");

// У нас УЖЕ есть goodVegetables2 - нам надо под КАЖДЫЙ элемент
// создать LI, добавить в него текст, и добавить в UL

goodVegetables2.forEach((vegetable) => {
  let li = document.createElement("li");
  console.log("Первый вывод элемента", li);
  li.textContent = vegetable;
  console.log("Второй вывод элемента", li);
  productList.appendChild(li);
  console.log("Третий вывод элемента", li);
});

// Найдем элемент div по классу "red"
redDiv = document.querySelector(".red");

function divOnClick() {
  redDiv.classList.toggle("blue");
  if (redDiv.textContent === "Красный") {
    redDiv.textContent = "Синий";
  } else {
    redDiv.textContent = "Красный";
  }
}

// Набор данных для примера "Рендер карточек"
// Массив объектов, всего два поля - текст и распродажа или нет string и boolean
let products = [
  { name: "Пикачу с пулемётом", onSale: true },
  { name: "Чебурашка с ракетой", onSale: false },
  { name: "Гомер Симпсон с пончиком", onSale: true },
  { name: "Губка Боб с лопаткой", onSale: false },
  { name: "Шрек с топором", onSale: true },
  { name: "Бендер с пивом", onSale: false },
];

// Рендер карточек
// Создать карточку. Дать класс карточка. Если распродажа - добавить класс распродажа. Внутри карточки создать элемент с текстом из name. И добавить карточку в контейнер

let cardsContainer = document.querySelector(".card-container");

products.forEach((product) => {
  //   Создаем карточку
  let card = document.createElement("div");
  //  Добавляем класс карточка
  card.classList.add("card");
  // Добавляю текст в карточку
  card.textContent = product.name;

  //   Если распродажа - добавить класс распродажа
  if (product.onSale) {
    card.classList.add("card-sale");
  }
  //   И добавить карточку в контейнер
  cardsContainer.appendChild(card);
});
