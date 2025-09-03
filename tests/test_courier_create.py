import pytest
from helpers.curl import post
from helpers.data import COURIER_CREATE, ERR_NOT_ENOUGH_DATA, ERR_LOGIN_EXISTS
from helpers.courier_factory import generate_courier_payload

def test_create_courier_success():
# Курьера можно создать: возвращается 201 и {'ok': true}
    payload = generate_courier_payload()
    response = post(COURIER_CREATE, payload)
    assert response.status_code == 201
    assert response.json().get("ok") is True

def test_create_courier_duplicate():
# Нельзя создать двух одинаковых курьеров — сервер должен ответить 409/400
    payload = generate_courier_payload()

    r1 = post(COURIER_CREATE, payload)
    assert r1.status_code == 201

    r2 = post(COURIER_CREATE, payload)
    assert r2.status_code in (400, 409)
    assert ERR_LOGIN_EXISTS in r2.text

@pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
def test_create_courier_missing_required_field(missing_field):
# Если не передать обязательное поле — ожидаем 400 и сообщение 'Недостаточно данных'
    payload = generate_courier_payload()
    payload.pop(missing_field)
    response = post(COURIER_CREATE, payload)
    assert response.status_code == 400
    assert ERR_NOT_ENOUGH_DATA in response.text