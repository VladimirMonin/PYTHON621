const containerDone = document.getElementById("done");
const containerInProgress = document.getElementById("in-progress");

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
  let currentTimer = timer;

  for (let i = 0; i < retryCount; i++) {
    try {
      return await fetchData();
    } catch (error) {
      lastError = error;
      console.error(`Попытка ${i + 1} не удалась: ${error.message}`);
      // Можно добавить задержку перед следующей попыткой, если нужно
      await new Promise((resolve) => setTimeout(resolve, currentTimer));
      currentTimer *= 2; // Увеличиваем таймер для следующей попытки (экспоненциальная задержка)
    }
  }

  throw new Error(
    `Все попытки загрузки данных не удались. Последняя ошибка: ${lastError.message}`,
  );
}

// completed: false
// id: 1
// title: "delectus aut autem"
// userId: 

// Логика создания чекбокса (прожатого/непрожатого) для карточки
function createCheckboxGroup(isChecked) {
  const checkboxGroup = document.createElement("div");
  checkboxGroup.classList.add("checkbox-group");

  const label = document.createElement("label");
  label.textContent = "Статус задачи";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = isChecked;
  checkboxGroup.appendChild(label);
  checkboxGroup.appendChild(checkbox);
  return checkboxGroup;
}

// Логика рендера 1 карточки
function renderCard(cardData) {
  const card = document.createElement("div");
  card.classList.add("task");
  card.classList.add(cardData.completed ? "task-done" : "task-in-progress");
  const title = document.createElement("h3");
  title.textContent = cardData.title;
  card.appendChild(title);
  const checkboxGroup = createCheckboxGroup(cardData.completed);
  card.appendChild(checkboxGroup);
  const checkbox = checkboxGroup.querySelector("input[type='checkbox']");
  setupCheckboxListener(checkbox, cardData);
  return card;
}

// Логика рендера всех карточек
function renderCards(cardsData) {
  cardsData.forEach((cardData) => {
    const card = renderCard(cardData);
    if (cardData.completed) {
      containerDone.appendChild(card);
    } else {
      containerInProgress.appendChild(card);
    }
  });
}

// Функция для листнера которая будет слушать изменения чекбокса и менять статус задачи
function setupCheckboxListener(checkbox, cardData) {
  checkbox.addEventListener("change", () => {
    cardData.completed = checkbox.checked;
    // Логика для перемещения карточки между контейнерами
    const card = checkbox.closest(".task");
    if (checkbox.checked) {
      // Класс .task-in-progress удаляем, а класс .task-done добавляем
      card.classList.remove("task-in-progress");
      card.classList.add("task-done");
      containerDone.appendChild(card);
    } else {
      card.classList.remove("task-done");
      card.classList.add("task-in-progress");
      containerInProgress.appendChild(card);
    }
  });
}

async function main() {
  let data = await fetchDataRetry();
  console.debug("Загруженные данные: ", data);
  renderCards(data);
}

main();
