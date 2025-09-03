import pytest
from helpers.curl import post, get
from helpers.data import ORDERS

class TestOrders:
    @pytest.mark.parametrize("colors", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    def test_create_order_with_colors(self, colors):
# Создаём заказ с параметризацией цвета
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

    def test_get_orders_list(self):
# Запрос списка заказов возвращает ключ 'orders' (list)
        response = get(ORDERS)
        assert response.status_code == 200
        body = response.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)