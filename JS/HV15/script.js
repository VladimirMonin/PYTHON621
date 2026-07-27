// ------------------------------------------------------------
// ДАННЫЕ ПРОЕКТА
// ------------------------------------------------------------

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

// ------------------------------------------------------------
// DOM-ЭЛЕМЕНТЫ
// ------------------------------------------------------------

const hallEl = document.getElementById("hall");
const saleForm = document.getElementById("sale-form");
const salesBody = document.getElementById("sales-body");
const filterInput = document.getElementById("filter-input");
const msgEl = document.getElementById("form-message");
const emptyState = document.getElementById("empty-state");
const soldCount = document.getElementById("sold-count");

// ------------------------------------------------------------
// РЕНДЕР ЗАЛА
// ------------------------------------------------------------

function renderHall() {
  hallEl.textContent = "";

  seats.forEach((s) => {
    const div = document.createElement("div");
    div.className = `seat ${s.status}`;
    div.textContent = `${s.row}-${s.seat}`;
    div.title = s.status === "sold" ? `Продано: ${s.buyer}` : "Свободное место";
    hallEl.appendChild(div);
  });
}

// ------------------------------------------------------------
// РЕНДЕР ТАБЛИЦЫ ПРОДАЖ
// ------------------------------------------------------------

function renderSalesTable() {
  salesBody.textContent = "";

  const sold = seats.filter((s) => s.status === "sold");

  sold.forEach((s) => {
    const tr = document.createElement("tr");
    [s.buyer, s.row, s.seat].forEach((val) => {
      const td = document.createElement("td");
      td.textContent = val;
      tr.appendChild(td);
    });
    salesBody.appendChild(tr);
  });

  soldCount.textContent = sold.length;
}

// ------------------------------------------------------------
// ФИЛЬТР ТАБЛИЦЫ
// ------------------------------------------------------------

function applyFilter() {
  const query = filterInput.value.trim().toLowerCase();
  const rows = Array.from(salesBody.querySelectorAll("tr"));
  let visible = 0;

  rows.forEach((tr) => {
    const match = tr.cells[0].textContent.toLowerCase().includes(query);
    tr.classList.toggle("is-hidden", !match);
    if (match) visible++;
  });

  emptyState.classList.toggle("is-hidden", !(rows.length > 0 && visible === 0));
}

// ------------------------------------------------------------
// ОБРАБОТКА ФОРМЫ
// ------------------------------------------------------------

saleForm.addEventListener("submit", (event) => {
  event.preventDefault();
  msgEl.className = "message is-hidden";

  const buyer = saleForm.elements.buyer.value.trim();
  const row = Number(saleForm.elements.row.value);
  const seat = Number(saleForm.elements.seat.value);

  if (!buyer) {
    msgEl.textContent = "Введите имя покупателя.";
    msgEl.className = "message message--error";
    return;
  }

  if (
    !Number.isInteger(row) ||
    !Number.isInteger(seat) ||
    row < 1 ||
    row > 4 ||
    seat < 1 ||
    seat > 5
  ) {
    msgEl.textContent = "Допустимые значения: ряд 1–4, место 1–5.";
    msgEl.className = "message message--error";
    return;
  }

  const found = seats.find((s) => s.row === row && s.seat === seat);

  if (found.status === "sold") {
    msgEl.textContent = `Место ${row}-${seat} уже продано (${found.buyer}).`;
    msgEl.className = "message message--error";
    return;
  }

  found.status = "sold";
  found.buyer = buyer;

  renderHall();
  renderSalesTable();
  applyFilter();

  msgEl.textContent = `Билет успешно продан: ${buyer}, ряд ${row}, место ${seat}.`;
  msgEl.className = "message message--success";

  saleForm.reset();
  saleForm.elements.buyer.focus();
});

filterInput.addEventListener("input", applyFilter);

// ------------------------------------------------------------
// ПЕРВЫЙ РЕНДЕР
// ------------------------------------------------------------

renderHall();
renderSalesTable();
