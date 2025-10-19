import requests
import allure
import pytest

from data.urls import Url
import helpers.new_courier as courier
from data.create_courier_test_data import CreateCourierTestData as Td


class TestCreateCourier:

    @allure.title("Проверка успешного создания курьера. Курьера можно создать. Код 201")   
    def test_create_courier_success_status(self, new_courier_unregistered):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_courier_unregistered)
        assert response.status_code == Td.success_status


    @allure.title('Проверка успешного создания курьера. Успешный запрос возвращает {"ok":true};')   
    def test_create_courier_success_response_ok_true(self, new_courier_unregistered):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_courier_unregistered)
        assert response.json()["ok"] == True

    @allure.title('Проверка создания одинаковых курьеров. Статус 409.')   
    def test_create_courier_two_similar_couriers_status_code_409(self, new_courier_registered):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_courier_registered)
        assert response.status_code == Td.conflict_status

    @allure.title('Проверка создания одинаковых курьеров. Сообщение об ошибке.')   
    def test_create_courier_two_similar_couriers_message(self, new_courier_registered):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_courier_registered)
        assert response.json()["message"] == Td.conflict_message


    @allure.title("Проверка создания курьера с отсутствующими обязательными полями. Код 400. Отсутствует: {param}")    
    @pytest.mark.parametrize('param', Td.required_fields)
    def test_create_courier_required_fields_bad_request_status_code(self, param):
        payload = courier.new_login_pass_fname()
        del payload[param]

        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=payload)
        assert response.status_code == Td.bad_status


    @allure.title("Проверка создания курьера с отсутствующими обязательными полями. Сообщение об ошибке. Отсутствует: {param}")    
    @pytest.mark.parametrize('param', Td.required_fields)
    def test_create_courier_required_fields_bad_request_message(self, param):
        payload = courier.new_login_pass_fname()
        del payload[param]

        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=payload)
        assert response.json()["message"] == Td.bad_message
