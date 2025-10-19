import allure
import pytest
import requests

from data.urls import Url
from data.courier_login_test_data import CourierLoginTestData as Td


class TestCourierLogin:

    @allure.title("Проверка успешного логина. Курьер может авторизоваться")    
    def test_courier_login_success_status_code(self, new_courier_registered):
        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=new_courier_registered)
        assert response.status_code == Td.success_login_status


    @allure.title("Проверка успешного логина. Успешный запрос возвращает id")    
    def test_courier_login_success_id_is_present(self, new_courier_registered):
        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=new_courier_registered)
        assert response.json()["id"]

    
    @allure.title("Проверка входа с неполными данными. Неуспешная авторизация. Код 400. Передан только: {param}")    
    @pytest.mark.parametrize('param', Td.required_fields)
    def test_courier_login_required_fields_bad_login_status_code(self, param, new_courier_registered):
        payload = {param: new_courier_registered[param]}

        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=payload)
        assert response.status_code == Td.bad_login_status


    @allure.title("Проверка входа с неполными данными. Неуспешная авторизация. Сообщение об ошибке. Передан только: {param}")    
    @pytest.mark.parametrize('param', Td.required_fields)
    def test_courier_login_required_fields_bad_login_message_is_present(self, param, new_courier_registered):
        payload = {param: new_courier_registered[param]}

        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=payload)
        assert response.json()["message"] == Td.bad_login_message


    @allure.title("Проверка входа с неправильными данными. Неуспешная авторизация. Код 404. Некорректно передан: {param}")    
    @pytest.mark.parametrize('param', Td.required_fields)
    def test_courier_wrong_login_status_code(self, param, new_courier_registered):
        new_courier_registered[param] += "_wrong_!"
        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=new_courier_registered)
        assert response.status_code == Td.wrong_login_status


    @allure.title("Проверка входа с неправильными данными. Неуспешная авторизация. Сообщение об ошибке. Некорректно передан: {param}")    
    @pytest.mark.parametrize('param', Td.required_fields)
    def test_courier_wrong_login_message_is_present(self, param, new_courier_registered):
        new_courier_registered[param] += "_wrong_!"

        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=new_courier_registered)
        assert response.json()["message"] == Td.wrong_login_message
