const seats = [
  { row: 1, seat: 1, status: "free", buyer: "" },
  { row: 1, seat: 2, status: "sold", buyer: "Анна" },
  { row: 1, seat: 3, status: "free", buyer: "" },
  { row: 1, seat: 4, status: "free", buyer: "" },
  { row: 1, seat: 5, status: "sold", buyer: "Борис" },

  { row: 2, seat: 1, status: "free", buyer: "" },
  { row: 2, seat: 2, status: "free", buyer: "" },
  { row: 2, seat: 3, status: "sold", buyer: "Вика" },
  { row: 2, seat: 4, status: "free", buyer: "" },
  { row: 2, seat: 5, status: "free", buyer: "" },

  { row: 3, seat: 1, status: "sold", buyer: "Глеб" },
  { row: 3, seat: 2, status: "free", buyer: "" },
  { row: 3, seat: 3, status: "free", buyer: "" },
  { row: 3, seat: 4, status: "sold", buyer: "Дина" },
  { row: 3, seat: 5, status: "free", buyer: "" },

  { row: 4, seat: 1, status: "free", buyer: "" },
  { row: 4, seat: 2, status: "free", buyer: "" },
  { row: 4, seat: 3, status: "sold", buyer: "Егор" },
  { row: 4, seat: 4, status: "free", buyer: "" },
  { row: 4, seat: 5, status: "free", buyer: "" },
];

const seatsContainer = document.getElementById("seats-container");
const nameInput = document.getElementById("nameInput");

function renderSingleSeat(seat) {
  const seatEl = document.createElement("div");
  seatEl.className = `seat ${seat.status}`;

  if (seat.searchHit) {
    seatEl.classList.add("search-hit");
  }

  seatEl.textContent = `${seat.row}-${seat.seat}`;
  seatEl.title =
    seat.status === "sold" ? `Продано: ${seat.buyer}` : "Свободное место";
  return seatEl;
}

function renderHall(seats) {
  seatsContainer.textContent = "";
  seats.forEach((seat) => {
    const seatEl = renderSingleSeat(seat);
    seatsContainer.appendChild(seatEl);
  });
}

renderHall(seats);

nameInput.addEventListener("input", () => {
  const query = nameInput.value.trim().toLowerCase();
  const updatedSeats = seats.map((seat) => {
    if (seat.buyer.toLowerCase().includes(query) && query !== "") {
      return { ...seat, searchHit: true };
    } else {
      const { searchHit, ...rest } = seat;
      return rest;
    }
  });
  renderHall(updatedSeats);
});

// РАБОТА С КУКАМИ ==========================
// В JavaScript все куки сайта свалены в одну кучу — свойство document.cookie. Это строка, где пары «ключ=значение» разделены точкой с запятой и пробелом.

// Чтение куков
console.debug("Текущие куки:", document.cookie);

// Запись куков
document.cookie = "username=JohnDoe; path=/; max-age=3600"; // Кука с именем username и значением JohnDoe, действительна 1 час

// Удаление куков
document.cookie = "username=; path=/; max-age=0"; // Удаляет куку username

// Чтение конкретной куки
function getCookie(name) {
  const cookies = document.cookie.split("; ");
  for (const cookie of cookies) {
    const [key, value] = cookie.split("=");
    if (key === name) {
      return value;
    }
  }
  return null;
}

// Локальное хранилище (localStorage) и сессионное хранилище (sessionStorage)

// Локальное хранилище сохраняет данные без срока действия, а сессионное хранилище удаляется при закрытии вкладки.

// Работа с localStorage
// localStorage.setItem("username", "JohnDoe");
console.debug("Username from localStorage:", localStorage.getItem("username"));
// localStorage.removeItem("username");

// Работа с sessionStorage
// sessionStorage.setItem("sessionId", "abc123");
console.debug(
  "Session ID from sessionStorage:",
  sessionStorage.getItem("sessionId"),
);
// sessionStorage.removeItem("sessionId");

// JSON - JavaScript Object Notation

// http://api.openweathermap.org/data/2.5/weather?q=&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru

// let weatherData = {
//   coord: { lon: 82.6103, lat: 49.9789 },
//   weather: [
//     { id: 741, main: "Fog", description: "плотный туман", icon: "50n" },
//   ],
//   base: "stations",
//   main: {
//     temp: -2.04,
//     feels_like: -2.04,
//     temp_min: -2.04,
//     temp_max: -2.04,
//     pressure: 1019,
//     humidity: 100,
//     sea_level: 1019,
//     grnd_level: 975,
//   },
//   visibility: 100,
//   wind: { speed: 1, deg: 0 },
//   clouds: { all: 100 },
//   dt: 1774894083,
//   sys: {
//     type: 1,
//     id: 8831,
//     country: "KZ",
//     sunrise: 1774829484,
//     sunset: 1774875397,
//   },
//   timezone: 18000,
//   id: 1520316,
//   name: "Усть-Каменогорск",
//   cod: 200,
// };

let someJsonString = '{"name": "John", "age": 30, "city": "New York"}';
// let someJsonString = "{'name': 'John', 'age': 30, 'city': 'New York'}";
let someObject = JSON.parse(someJsonString); // Преобразование JSON-строки в объект
console.debug("Parsed object:", someObject);

// Преобразование объекта в JSON-строку
let jsonString = JSON.stringify(someObject);


// Сохранить jsonString в localStorage
localStorage.setItem("user", jsonString);

// Получить jsonString из localStorage и преобразовать обратно в объект
let storedJsonString = localStorage.getItem("user");
let storedObject = JSON.parse(storedJsonString);
console.debug("Stored object:", storedObject);

// JSON жесткий стандарт. Требования серьезные:
// Ключи должны быть в двойных кавычках.
// Строковые значения должны быть в двойных кавычках.
// Числа, булевы значения и null не должны быть в кавычках.
// В конце НЕ ДОЛЖНО быть запятой после последнего элемента в объекте или массиве.