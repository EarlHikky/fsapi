import pony

fake_database = {'users': [
    {
        "id": 1,  # тут тип данных - число
        "name": "Anna",  # тут строка
        "nick": "Anny42",  # и тут
        "balance": 15.01  # а тут float
    },

    {
        "id": 2,  # у второго пользователя
        "name": "Dima",  # такие же
        "nick": "dimon2319",  # типы
        "balance": 8.01  # данных
    }
    , {
        "id": 3,  # у третьего
        "name": "Vladimir",  # юзера
        "nick": "Vova777",  # мы специально сделаем
        "balance": "23"  # нестандартный тип данных в его балансе
    }
], }
