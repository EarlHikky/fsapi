import fastapi

import database
import pydantic_models
from database.db import fake_database

api = fastapi.FastAPI()

response = {"Ответ": "Который возвращает сервер"}


@api.get('/static/path')
def hello():
    return "hello"


@api.get('/user/{nick}')  # переменные в пути заключаются в фигурные скобки
def get_nick(nick):  # в функцию передаем эту переменную и работаем с ней дальше
    return {"user": nick}  # при запросе страницы вернет строку, которую мы вписали после последнего слеша


@api.get('/userid/{id:int}')  # мы можем задавать тип данных прямо в пути через двоеточие
def get_id(id):  # тут в пути обязательно должно быть число, иначе возникнет ошибка
    return {"user": id}


@api.get('/user_id/{id}')
def get_id2(id: int):  # либо же его можно задавать как тайп-хинт прямо в функции
    return {"user": id}  # возвращается число, а не строка, как было бы без объявления типа данных


@api.get('/user_id_str/{id:str}')
def get_id2(id):
    return {"user": id}  # тут id - это уже строка, так как мы объявили тип данных


@api.get('/get_info_by_user_id/{id:int}')
def get_info_about_user(id):
    return fake_database['users'][id - 1]


@api.get('/get_user_balance_by_id/{id:int}')
def get_user_balance(id):
    return fake_database['users'][id - 1]['balance']


# @api.get('/get_total_balance')
# def get_total_balance():
#     total_balance: float = 0.0
#     for user in fake_database['users']:
#         total_balance += user['balance']
#     return total_balance


@api.get('/get_total_balance')
def get_total_balance():
    total_balance: float = 0.0
    for user in fake_database['users']:
        total_balance += pydantic_models.User(**user).balance
    return total_balance


"""
У нас теперь есть функция для вывода юзеров из базы данных, а аргументы skip(пропуск) и limit(ограничение) будут браться из пути, который запрашивает пользователь, добавляются они после знака вопроса "?" и перечисляются через амперсанд "&", а их значения задаются через знак равно "=", то есть, чтобы задать значения аргументам skip=1 и limit=10 нам нужно выполнить GET-запрос, который будет иметь путь "/users?skip=1&limit=10"
"""


@api.get("/users/")
def get_users(skip: int = 0, limit: int = 10):
    return fake_database['users'][skip: skip + limit]  # http://127.0.0.1:8000/users/?skip=1&limit=10


# Значения по умолчанию
@api.get("/user/{user_id}")
def read_user(user_id: str, query: str | None = None):
    """
    Тут значение по умолчанию для query будет None
    """
    if query:
        return {"user_id": user_id, "query": query}
    return {"user_id": user_id}


@api.get("/users/")
def get_users(skip: int, limit: int):
    return fake_database['users'][skip: skip + limit]

# uvicorn app:api --reload
