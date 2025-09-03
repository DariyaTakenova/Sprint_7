import pytest
from helpers.curl import post
from helpers.data import COURIER_CREATE, ERR_NOT_ENOUGH_DATA, ERR_LOGIN_EXISTS
from helpers.courier_factory import generate_courier_payload

class TestCourierCreate:
    def test_create_courier_success(self):
# Курьера можно создать: возвращается 201 и {'ok': true}
        payload = generate_courier_payload()
        response = post(COURIER_CREATE, payload)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    def test_create_courier_duplicate(self):
# Нельзя создать двух одинаковых курьеров
        payload = generate_courier_payload()
        r1 = post(COURIER_CREATE, payload)
        assert r1.status_code == 201

        r2 = post(COURIER_CREATE, payload)
        assert r2.status_code in (400, 409)
        assert (ERR_LOGIN_EXISTS in r2.text) or (ERR_NOT_ENOUGH_DATA not in r2.text)

    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_required_field(self, missing_field):
# Если не передать обязательное поле — 400 + сообщение об ошибке
        payload = generate_courier_payload()
        payload.pop(missing_field)
        response = post(COURIER_CREATE, payload)
        assert response.status_code == 400
        assert ERR_NOT_ENOUGH_DATA in response.text