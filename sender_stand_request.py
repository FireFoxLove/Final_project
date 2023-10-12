import configuration
import requests
import data


#Создание нового пользователя
def post_new_order(body, headers):
    return requests.post(configuration.URL_SERVICE + configuration.ADD_ORDER_PATH,  #подставляем полный url
        json=body,  #тело
        headers=headers)  #заголовки


def get_order_by_track(params):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH, params=params)











