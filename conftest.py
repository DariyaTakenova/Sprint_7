import pytest
from helpers.data import register_new_courier_and_return_login_password, COURIER_CREATE, COURIER_LOGIN
from helpers.curl import post, delete

@pytest.fixture
def new_courier():

    creds = register_new_courier_and_return_login_password()
    assert creds, "Не удалось зарегистрировать курьера через API"

    courier = {"login": creds[0], "password": creds[1], "firstName": creds[2]}

    yield courier

    login_res = post(COURIER_LOGIN, {"login": courier["login"], "password": courier["password"]}, use_json=False)
    if login_res.status_code == 200 and "id" in login_res.json():
        courier_id = login_res.json()["id"]
        # DELETE /api/v1/courier/:id
        delete(f"{COURIER_CREATE}/{courier_id}")