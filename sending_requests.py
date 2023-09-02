import requests

import config
import data


# Создание нового заказа
def post_new_orders():
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)


# Получение данных заказа по его треку
def get_order_info(track):
    return requests.get(config.URL_SERVICE + config.GET_ORDER_PATH,
                        params={"t": track})