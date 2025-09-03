import string
import random

# Базовый URL
BASE_URL = "https://qa-scooter.praktikum-services.ru"

# Эндпоинты
COURIER_CREATE = "/api/v1/courier"
COURIER_LOGIN = "/api/v1/courier/login"
ORDERS = "/api/v1/orders"
PING = "/api/v1/ping"

# Сообщения об ошибках
ERR_NOT_ENOUGH_DATA = "Недостаточно данных"
ERR_LOGIN_EXISTS = "Этот логин уже используется"
ERR_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"


def generate_random_string(length=10):
# Генерация случайной строки из латинских букв
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
