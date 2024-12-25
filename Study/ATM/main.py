from atm import ATM
from sql_atm import SqlAtm

class Main:
    sql_atm = SqlAtm('Users_data')
    atm = ATM(sql_atm)
    atm.start()