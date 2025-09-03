import pytest
from helpers.curl import post
from helpers.data import COURIER_LOGIN, ERR_NOT_ENOUGH_DATA, ERR_ACCOUNT_NOT_FOUND, generate_random_string
from helpers.courier_utils import register_new_courier_and_return_login_password

def test_login_success(new_courier):
# Курьер, который зарегистрирован, может залогиниться — ответ содержит id
    response = post(COURIER_LOGIN, {"login": new_courier["login"], "password": new_courier["password"]}, use_json=False)
    assert response.status_code == 200
    assert "id" in response.json()

@pytest.mark.parametrize("payload", [
    {"password": generate_random_string()},  # нет логина
    {"login": generate_random_string()}      # нет пароля
])
def test_login_without_required_fields(payload):
    """Если не передать login или password — вернётся 400"""
    response = post(COURIER_LOGIN, payload, use_json=False)
    assert response.status_code == 400
    assert ERR_NOT_ENOUGH_DATA in response.text

def test_login_wrong_password():
# Неверный пароль — ожидаем 400/404
    creds = register_new_courier_and_return_login_password()
    payload = {"login": creds[0], "password": "wrong_password"}
    response = post(COURIER_LOGIN, payload, use_json=False)
    assert response.status_code in (400, 404)
    assert ERR_ACCOUNT_NOT_FOUND in response.text or "не найден" in response.text.lower()

def test_login_non_existing_user():
# Попытка логина несуществующего пользователя — ожидаем 404/400
    payload = {"login": generate_random_string(), "password": generate_random_string()}
    response = post(COURIER_LOGIN, payload, use_json=False)
    assert response.status_code in (400, 404)
    assert ERR_ACCOUNT_NOT_FOUND in response.text or "не найден" in response.text.lower()