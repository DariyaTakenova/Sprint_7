def generate_order_payload(colors=None):

    return {
        "firstName": "Ivan",
        "lastName": "Petrov",
        "address": "Moscow, Red Square",
        "metroStation": 4,
        "phone": "+79998887766",
        "rentTime": 3,
        "deliveryDate": "2025-09-01",
        "comment": "autotest order",
        "color": colors or []
    }
