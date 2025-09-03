import pytest
from helpers.courier_factory import register_new_courier_and_return_login_password

@pytest.fixture
def new_courier():
# Фикстура: создаёт нового курьера и возвращает его данные
    creds = register_new_courier_and_return_login_password()
    assert creds, "Не удалось зарегистрировать курьера"
    return creds
