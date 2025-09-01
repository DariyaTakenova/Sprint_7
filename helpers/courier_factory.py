from helpers.data import generate_random_string

def generate_courier_payload():

    # Возвращает словарь с полями login, password, firstName.

    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }
