import pytest
from helpers.courier_utils import register_new_courier_and_return_login_password


@pytest.fixture
def new_courier():
# Фикстура: регистрирует курьера и возвращает его данные
    creds = register_new_courier_and_return_login_password()
    if not creds:
        pytest.fail("Не удалось создать курьера через API")
    return {"login": creds[0], "password": creds[1], "firstName": creds[2]}
