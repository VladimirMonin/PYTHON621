console.debug("Логика подключена!");
console.debug("Датасет подключен и переменные с него доступны в этом файле!");

// Проверили - все доступно!
console.debug(proverbs.length);
console.debug(variants.length);

// Получили математически лимит на генерацию пословиц
let proverbsLimit = proverbs.length * variants.length;

console.debug(`Всего возможных пословиц: ${proverbsLimit}`);

// Взяли строку с числом от пользователя
let userInput = prompt("Сколько пословиц вы хотите?");

// Сделали проверку на число и на лимит
if (isNaN(userInput)) {
  console.error("Вы ввели не число!");
} else if (userInput < 1) {
  console.error("Вы ввели число меньше 1!");
} else if (userInput > proverbsLimit) {
  console.error(
    `Вы ввели число больше максимально возможного (${proverbsLimit})!`,
  );
} else {
  console.debug(`Вы ввели корректное число: ${userInput}`);
}

// Берем цикл и генерируем пословицы, пока не достигнем лимита или не нагенерируем нужное количество

// Вариант цикла while

let results = [];
let tryCounter = 0;
let ulResult = document.getElementById("result");

// ВАРИАНТ 1. СЛУЧАЙНЫЙ ПЕРЕБОР. МИНУС - ДАЖЕ при заказе около 80% от максимума - гигансткое количество итераций.
// Браузер зависает нафиг.

// while (results.length < userInput) {
//   // Случайное число от 0 до длины массива пословиц
//   let randomProverbIndex = Math.floor(Math.random() * proverbs.length);
//   // Случайное число от 0 до длины массива вариантов
//   let randomVariantIndex = Math.floor(Math.random() * variants.length);

//   // Получаем случайную пословицу и вариант (без удаления из массива
//   let randomProverb = proverbs[randomProverbIndex];
//   let randomVariant = variants[randomVariantIndex];

//   // Собираем пословицу

//   // Разбиваем пословицу на части по Ум
//   let parts = randomProverb.split("Ум");
//   let finalProverbs = randomVariant + parts[1];

//   // Добавляем результат в массив результатов ЕСЛИ его там еще нет (чтобы не было повторов)
//   if (!results.includes(finalProverbs)) {
//     results.push(finalProverbs);
//   }
//   tryCounter++;
// }

// ВАРИАНТ 2. ЦИКЛ В ЦИКЛЕ. Берем одну половицу и проходим по всем заменам.
// Плюсы - максимум достигается за 935 итарациий. Мат. идеал.
// Минусы - если пользователь хочет 1 пословицу - мы все равно проходим 935 итераций. Но это не так критично, как в первом варианте.

let allCustomProverbs = [];

for (let proverb of proverbs) {
  for (let variant of variants) {
    let parts = proverb.split("Ум");
    let finalProverb = variant + parts[1];
    allCustomProverbs.push(finalProverb);
  }
}

console.debug(`Всех возможных пословиц: ${allCustomProverbs.length}`);

// Теперь нам нужно взять из allCustomProverbs нужное количество случайных пословиц, без повторов
// ПРОСТОЙ ВАРИАНТ - СРЕЗ
let results2 = allCustomProverbs.slice(0, userInput);

// ВАРИАНТ 2 СФОРМИРОВАТЬ СЛУЧАЙНУЮ ВЫБОРКУ ИЗ ВСЕХ ВОЗМОЖНЫХ ПОСЛОВИЦ - более интересная выдача
while (results.length < userInput) {
  let randomIndex = Math.floor(Math.random() * allCustomProverbs.length);
  let randomProverb = allCustomProverbs[randomIndex];
  results.push(randomProverb);
}

console.debug(`Сгенерировано пословиц: ${results.length}`);
console.debug(results);
console.debug(`Потрачено попыток на генерацию: ${tryCounter}`);

// Циклом формирую LI и добавляю их в UL
for (let result of results) {
  let li = document.createElement("li");
  li.textContent = result;
  ulResult.appendChild(li);
}

let tableResult = document.getElementById("tableResult");

let counter = 0;
for (let result of results) {
  // Создали строку таблицы
  let tr = document.createElement("tr");
  //   Ячейка 1 с номером пословицы
  let tdNumber = document.createElement("td");
  tdNumber.textContent = counter++;

  //   Ячейка 2 с текстом пословицы
  let tdText = document.createElement("td");
  tdText.textContent = result;
  // Добавляем ячейки в строку по очереди
  tr.appendChild(tdNumber);
  tr.appendChild(tdText);

  // Добавляем строку в таблицу
  tableResult.appendChild(tr);
}
