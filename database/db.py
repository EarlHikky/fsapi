from pony.orm import *
import models

db = Database()


class User(db.Entity):
    user_id = Required(str)
    nick = Required(str)
    age = Required(int)
    wallets = Set('Wallet')


class Wallet(db.Entity):
    address = Required(str)
    private_key = Required(str)
    owner = Required(User)


try:
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
except Exception as Ex:
    print(Ex)


@db_session
def print_user_name(user_id):
    u = User[user_id]
    print(u.nick)
    # кэш сессии базы данных будет очищен автоматически
    # соединение с базой данных будет возвращено в пул


@db_session
def add_wallet(user_id, address, private_key):
    Wallet(address=address, private_key=private_key, owner=User[user_id])
    # commit() будет выполнен автоматически
    # кэш сессии базы данных будет очищен автоматически
    # соединение с базой данных будет возвращено в пул


db.generate_mapping(create_tables=True)
u1 = User(nick='John', user_id="20", age=25)
u2 = User(nick='Mary', user_id="22", age=26)
u3 = User(nick='Bob', user_id="30", age=35)
w1 = Wallet(address='address1', private_key='private_key1', owner=u2)
w2 = Wallet(address='address2', private_key='private_key2', owner=u3)
commit()

users = select(u for u in User if u.age > 20)

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
