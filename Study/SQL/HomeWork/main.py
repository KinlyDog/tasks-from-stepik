from user import User
from db_setup import DBSetup
from application import Application
from db_manager import DBManager

# Имя БД
db_name = 'registration.db'

# Создание БД и новой таблицы
# new_db = DBSetup(db_name, 'users_data', 'UserID', 'Login', 'Password', 'Code')
# new_db.create_table()

# Подключение к БД с помощью вспомогательного класса
db_manager = DBManager(db_name)

# Проверка добавления пользователя с помощью класса для работы с БД
ivan = User('Ivan', 'qwer1234', '1234')
db_manager.create_user(ivan)

# Запуск приложения с передачей менеджера по работе с БД в аргументах
Application(db_manager).start()
