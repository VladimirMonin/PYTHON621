// Lesson 20
// <li>Блок Try - Catch</li>
// throw new Error("Что-то пошло не так!"); - выброс исключения
// <li>Работа с запросами и разбор статусов ответов</li>
// <li>Обработка ошибок и исключений</li>
// <li>Промисы</li>

// Когда нам нужно создавать исключение? Когда происходит ошибка, которая не может быть обработана в текущем контексте. Например, если мы пытаемся получить доступ к свойству объекта, которого не существует, или если мы пытаемся выполнить операцию, которая не поддерживается.

function getSum(a, b) {
  // Просто делим а на b
  return a / b;
}

// Какие тут проблемы есть?
// 1. Деление на ноль. JS не даст ошибку, а вернет Infinity, что может привести к неправильным результатам в дальнейшем коде.
// 2. Деление строки на строку, числа на строку, строки на число.

console.debug(getSum(10, 2)); // 5
console.debug(getSum(10, 0)); // Infinity
console.debug(getSum("10", "2")); // 5 потому что JS пытается преобразовать строки в числа
console.debug(getSum("10", 2)); // 5 потому что JS пытается преобразовать строку в число
console.debug(getSum(10, "чебурек")); // NaN потому что JS не может преобразовать строку "чебурек" в число

function getSum2(a, b) {
  // Оба аргумента должны быть числом
  // b - не должен быть нулем
  if (!isNaN(a) && !isNaN(b) && b != 0) {
    return a / b;
  } else {
    throw new Error(
      "Некорректные аргументы! Оба аргумента должны быть числами, а второй аргумент не должен быть нулем.",
    );
  }
}

console.debug(getSum2(10, 2)); // 5
// Ошибка: Некорректные аргументы! Оба аргумента должны быть числами, а второй аргумент не должен быть нулем.
// console.debug(getSum2(10, 0));
// console.debug(getSum2("10", "2"));
// console.debug(getSum2("10", 2));
// console.debug(getSum2(10, "чебурек"));

// Error - сам по себе не конец. Это просто особый случай который надо отработать. Пользователь ввел не те данные. Сервер не ответил во время. И т.п.
// Try - catch - блок для отлова ошибок. Код внутри try выполняется, если возникает ошибка, выполнение переходит в блок catch, где мы можем обработать эту ошибку.

let a = prompt("Введите число а");
let b = prompt("Введите число b");

function someFuncUsingGetSum2() {
  try {
    const result = getSum2(a, b);
    console.debug("Результат: ", result);
  } catch (error) {
    console.error("Произошла ошибка: ", error.message);
  }
}

someFuncUsingGetSum2();

// https://jsonplaceholder.typicode.com/users/1/todos
// Тренировка с имитацией апи

async function fetchData() {
  const response = await fetch(
    "https://jsonplaceholder.typicode.com/users/1/todos",
  );
  console.debug("Ответ от сервера: ", response);

  if (!response.ok) {
    throw new Error(`Ошибка HTTP: ${response.status}`);
  }

  return response.json();
}

async function fetchDataRetry(retryCount = 3, timer = 2000) {
  let lastError;

  for (let i = 0; i < retryCount; i++) {
    try {
      return await fetchData();
    } catch (error) {
      lastError = error;
      console.error(`Попытка ${i + 1} не удалась: ${error.message}`);
      // Можно добавить задержку перед следующей попыткой, если нужно
      await new Promise((resolve) => setTimeout(resolve, timer));
    }
  }

  throw new Error(
    `Все попытки загрузки данных не удались. Последняя ошибка: ${lastError.message}`,
  );
}

async function main() {
  let data = await fetchDataRetry();
  console.debug("Загруженные данные: ", data);
  renderCards(data);
}

// completed: false
// id: 1
// title: "delectus aut autem"
// userId: 1

// Логика рендера 1 карточки
function renderCard(cardData) {
  const card = document.createElement("div");
  card.classList.add("card");
  const title = document.createElement("h3");
  title.textContent = cardData.title;
  const status = document.createElement("span");
  status.classList.add("status");
  status.textContent = cardData.completed ? "Выполнено" : "Не выполнено";
  card.appendChild(title);
  card.appendChild(status);
  return card;
}

// Логика рендера всех карточек
function renderCards(cardsData) {
    const container = document.getElementById("cards-container");
    cardsData.forEach(cardData => {
        const card = renderCard(cardData);
        container.appendChild(card);
    });
}

main();
