const form1 = document.getElementById("form1");
const username = document.getElementById("username");
const password = document.getElementById("password");
const showPassword = document.getElementById("showPassword");
const passwordMessage = document.getElementById("passwordMessage");
const registerButton = document.getElementById("registerButton");
const url = "https://google.com";

form1.addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent form submission
  //   TODO - Отправляем форму сами
});

// Функция для отображения или скрытия пароля
showPassword.addEventListener("click", function () {
  if (password.type === "password") {
    password.type = "text"; // Показываем пароль
    showPassword.textContent = "Скрыть пароль"; // Меняем текст кнопки
  } else {
    password.type = "password";
    showPassword.textContent = "Показать пароль"; // Меняем текст кнопки
  }
});

// Валидация поля ввода пароля на длину 8 знаков
// .incorrect-password
// .correct-password
{
  /* <span id="passwordMessage"></span> */
}
password.addEventListener("input", function () {
  if (password.value.length < 8) {
    password.classList.add("incorrect-password");
    password.classList.remove("correct-password");
    passwordMessage.textContent = "Пароль должен быть не менее 8 символов";
    registerButton.disabled = true; // Блокируем кнопку регистрации
  } else {
    password.classList.remove("incorrect-password");
    password.classList.add("correct-password");
    passwordMessage.textContent = "";
    registerButton.disabled = false; // Разблокируем кнопку регистрации
  }
});

// Логика отправки формы метдом пост только функция которую мы разместим в обработчике события submit
function submitForm() {
  const formData = {
    username: username.value,
    password: password.value,
  };
    // TODO - Отправляем данные на сервер
// 