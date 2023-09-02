# Татьяна Романова, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import sending_requests

#Создание заказа. Возвращает его трек
def creat_new_order():
    response = sending_requests.post_new_orders()
    return response.json()["track"]


#Тест создания и получения заказа в БД
def test_create_and_get_new_order():
    track = creat_new_order()
    response =sending_requests.get_order_info(track)
    assert response.status_code == 200