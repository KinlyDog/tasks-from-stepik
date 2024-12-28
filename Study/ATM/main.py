from atm import ATM
from sql_atm import SqlAtm
from card import Card


class Main:
    sql_atm = SqlAtm('atm.db')
    # sql_atm.insert_user(Card(None, 2345, 2222, 10000))
    ATM(sql_atm).start()
