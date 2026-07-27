// Lesson 19 - Async - Await

// Пример синхронного кода в JS

function consoleIt(text) {
  console.log(text);
}

// Три запуска
consoleIt("Запуск 1");
consoleIt("Запуск 2");
consoleIt("Запуск 3");

// Результат
// Запуск 1
// Запуск 2
// Запуск 3

// setTimeout - асинхронная функция, которая выполняет код после определенного времени

consoleIt("Запуск 1");
setTimeout(() => {
  consoleIt("Запуск 2");
}, 5000);
consoleIt("Запуск 3");

// Пример с 2мя таймерами

consoleIt("Запуск 1");

setTimeout(() => {
  consoleIt("Запуск 2. Таймер 3000 мс");
}, 3000);

setTimeout(() => {
  consoleIt("Запуск 3. Таймер 500 мс");
}, 500);

consoleIt("Запуск 2");

// Пример с блокирующим кодом
const shape = document.getElementById("shape");
const startSync = document.getElementById("startSync");
const otherAction = document.getElementById("otherAction");
const startAsync = document.getElementById("startAsync");

function changeToRedSquare() {
  shape.className = "shape red-square";
  console.log("🟥 Фигура стала красным квадратом");
}
function changeToBlueCircle() {
  shape.className = "shape blue-circle";
  console.log("🔵 Фигура стала синим кругом");
}
function blockFor(ms) {
  const end = Date.now() + ms;
  while (Date.now() < end) {
    // Намеренная блокировка потока
  }
}
function runSyncAnimation() {
  console.log("▶️ Синхронная анимация началась");
  changeToRedSquare();
  console.log("⏳ Начинаем блокирующее ожидание 5 секунд");
  blockFor(5000);
  changeToBlueCircle();
  console.log("✅ Синхронная анимация завершена");
}
function runOtherAction() {
  console.log("⚙️ Выполняется другая функция");
}
startSync.addEventListener("click", runSyncAnimation);
otherAction.addEventListener("click", runOtherAction);

// Вариант асинхронного кода
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function runAsyncAnimation() {
  console.log("▶️ Асинхронная анимация началась");
  changeToRedSquare();
  console.log("⏳ Ждем 5 секунд...");
  await delay(5000);
  changeToBlueCircle();
  console.log("✅ Асинхронная анимация завершена");
}

startAsync.addEventListener("click", runAsyncAnimation);

// simple-fetch-example
// fetch - встроенная функция для выполнения HTTP-запросов

// simple-fetch-example.js

async function loadPost() {
  console.log("📤 Отправляем запрос на сервер...");

  const response = await fetch("https://jsonplaceholder.typicode.com/posts/1");
//   Мы отправили запрос
// Await говорит - можно пока занятся другими делами
// Когда внутренний промис фетч разрешится - продолжим работу
  console.log("📥 Ответ от сервера получен");

// На самом деле мы только дождались НАЧАЛА получения ответа
// И второй await как раз таки дожидается ОКОНЧАНИЯ получения ответа и преобразования его в JSON
  const post = await response.json();
  console.log("✅ Данные преобразованы в объект:", post);
}

loadPost();
console.log("⚙️ Этот console.log выполнится раньше, чем придет ответ");