from helpers.data import generate_random_string, COURIER_CREATE
from helpers.curl import post

def generate_courier_payload():
# Генерирует данные для нового курьера
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }

def register_new_courier_and_return_login_password():
# Создаёт курьера через API и возвращает dict с login/password/firstName
    payload = generate_courier_payload()
    response = post(COURIER_CREATE, payload)
    if response.status_code == 201:
        return payload
    return None