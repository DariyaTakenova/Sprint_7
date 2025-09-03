import requests
from helpers.data import BASE_URL, COURIER_CREATE, generate_random_string

def register_new_courier_and_return_login_password():

# Регистрирует нового курьера через API и возвращает [login, password, firstName].
# Если регистрация не удалась — вернёт пустой список.

    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(BASE_URL + COURIER_CREATE, data=payload)

    if response.status_code == 201:
        return [login, password, first_name]

    return []