import pytest
from helpers.curl import post, get
from helpers.data import ORDERS

@pytest.mark.parametrize("colors", [
    ["BLACK"],          # только BLACK
    ["GREY"],           # только GREY
    ["BLACK", "GREY"],  # оба
    []                  # отсутствие цвета
])
def test_create_order_with_colors(colors):
# Создаём заказ с разными цветами
    payload = {
        "firstName": "Ivan",
        "lastName": "Petrov",
        "address": "Moscow, Red Square",
        "metroStation": 4,
        "phone": "+79998887766",
        "rentTime": 3,
        "deliveryDate": "2025-09-01",
        "comment": "autotest order",
        "color": colors
    }
    response = post(ORDERS, payload)
    assert response.status_code == 201
    assert "track" in response.json()

def test_get_orders_list():
# Запрос списка заказов — в теле должен быть ключ 'orders'
    response = get(ORDERS)
    assert response.status_code == 200
    body = response.json()
    assert "orders" in body
    assert isinstance(body["orders"], list)