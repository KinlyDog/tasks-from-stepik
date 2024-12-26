from atm import ATM
from sql_atm import SqlAtm


class Main:
    sql_atm = SqlAtm('atm.db')

    ATM(sql_atm).start()
