from db_setup import DBSetup
from user import User
from db_manager import DBManager
from application import Application

# Имя БД
db_name = 'exchanger.db'

# Создание БД и новой таблицы
# new_db = DBSetup(db_name, 'users_balance', 'UserID', 'Balance_RUB', 'Balance_USD', 'Balance_EUR')
# new_db.create_table()

# Подключение к БД с помощью вспомогательного класса
db_manager = DBManager(db_name)

# # Проверка добавления пользователя с помощью класса для работы с БД
# user = User(100000, 1000, 1000)
# db_manager.create_user(user)

#
# Запуск приложения с передачей менеджера по работе с БД в аргументах
Application(db_manager).start()
