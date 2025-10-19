import requests
import random
import string

from data.urls import Url


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    url = Url.BASE_URL + Url.COURIER_URL
    response = requests.post(url=url, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


#метод создает и регистрирует курьера. Возвращает логин и пароль курьера в том виде, в котором их можно передавать в метод логина
def new_courier():
    login_pass = register_new_courier_and_return_login_password()

    new_courier_data = {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }

    return new_courier_data


#метод создает логин, пароль, имя для курьера и возвращает в удобном виде.
def new_login_pass_fname():

    login_pass_fname = {
        "login" : generate_random_string(10),
        "password" : generate_random_string(10),
        "firstName" : generate_random_string(10)
    }
    
    return login_pass_fname

# метод получает id курьера, который нужен для удаления
def get_courier_id(login, password):
    payload = {
        "login": login,
        "password": password
    }
    response_login = requests.post(Url.BASE_URL + Url.COURIER_LOGIN_URL, json=payload)
    
    return response_login.json()["id"]

# метод удаляет курьера п
def delete_courier(login, password):
    id = get_courier_id(login, password)
    url = f'{Url.BASE_URL}{Url.COURIER_URL}/{id}'
    response_delete = requests.delete(url=url)

