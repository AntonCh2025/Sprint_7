import requests
import allure
import pytest
import json

from data.urls import Url
from data.create_order_test_data import CreateOrderTestData as Td 


class TestCreateOrder:

    @allure.title("Проверка успешного создания заказа. Заказ с одним цветом: {color}")  
    @pytest.mark.parametrize('color', Td.available_colors)
    def test_create_order_with_one_color(self, color):
        order_data = Td.make_order_data(color)
        url = Url.BASE_URL + Url.ORDER_URL
        response = requests.post(url=url,json=order_data)
        assert response.status_code == Td.status_success

    @allure.title("Проверка успешного создания заказа. Заказ с двумя цветами")  
    def test_create_order_with_two_colors(self):
        order_data = Td.make_order_data(Td.available_colors)
        url = Url.BASE_URL + Url.ORDER_URL
        response = requests.post(url=url,json=order_data)
        assert response.status_code == Td.status_success

    @allure.title("Проверка успешного создания заказа. Цвет не передается")  
    def test_create_order_without_color(self):        
        order_data = Td.make_order_data()
        
        url = Url.BASE_URL + Url.ORDER_URL
        payload = json.dumps(order_data)
        response = requests.post(url=url,data=payload)
        assert response.status_code == Td.status_success

    @allure.title("Проверка успешного создания заказа. В ответе присутствует track")  
    def test_create_order_track_in_response(self):        
        order_data = Td.make_order_data()
        url = Url.BASE_URL + Url.ORDER_URL
        response = requests.post(url=url,json=order_data)
        assert response.json()["track"]
