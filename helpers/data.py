import requests
import random
import string

# Базовый URL сервиса (без суффикса /api)
BASE_URL = "https://qa-scooter.praktikum-services.ru"
API_PREFIX = "/api/v1"

# Эндпоинты (используем относительные пути, чтобы собирать полный URL в curl.py)
COURIER_CREATE = "/api/v1/courier"
COURIER_LOGIN = "/api/v1/courier/login"
ORDERS = "/api/v1/orders"
PING = "/api/v1/ping"

# Ожидаемые сообщения об ошибках (чтобы не дублировать строки в тестах)
ERR_NOT_ENOUGH_DATA = "Недостаточно данных"
ERR_LOGIN_EXISTS = "Этот логин уже используется"
ERR_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"

# Генератор случайной строки (только маленькие буквы), используется в тестах
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра,
    # в качестве параметра передаём длину строки
    def generate_random_string_local(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string_local(10)
    password = generate_random_string_local(10)
    first_name = generate_random_string_local(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f"{BASE_URL}{API_PREFIX}/courier", data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass