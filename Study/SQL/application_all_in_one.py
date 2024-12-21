import sqlite3
from typing import Optional, Tuple


# Класс пользователя
class User:
    def __init__(self, login: str, password: str, code: str):
        self.login = login
        self.password = password
        self.code = code


# Класс для взаимодействия с БД
class DBManager:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name  # Указываем имя БД для подключения

    # Подключаемся к БД
    def connect(self):
        return sqlite3.connect(self.db_name)

    # Получаем пользователя из БД
    def get_user(self, user: User) -> Optional[Tuple]:
        with self.connect() as db:
            cur = db.cursor()

            cur.execute("""
                        SELECT Login, Password, Code FROM users_data WHERE Login = ?;
                        """, (user.login.lower(),))

            # Возвращаем кортеж с данными или None, если пользователь отсутствует в БД
            return cur.fetchone()

    # Создание пользователя
    def create_user(self, user: User) -> bool:
        db_user = self.get_user(user)  # Получение пользователя из БД

        # Проверяем, если объект пользователя с БД не пустой
        # Значит, что пользователь уже существует
        if db_user is not None:
            print("Пользователь уже существует.")
            return False

        # Подключаемся к БД для создания пользователя
        with self.connect() as db:
            cur = db.cursor()

            # Параметры для запроса получаем из объекта User переданного в аргументы метода
            data_user = (user.login.lower(), user.password, user.code)

            cur.execute("""
                        INSERT INTO users_data(Login, Password, Code)
                        VALUES (?, ?, ?);
                        """, data_user)

            db.commit()
            print("Пользователь успешно добавлен.")
            return True

    # Логин пользователя
    def login(self, user: User):
        # Получаем из БД пользователя
        db_user = self.get_user(user)

        # Если None, значит пользователя не существует
        if db_user is None:
            print("Пользователь не существует")
            return False

        # Сравниваем пароль пользователя из БД и пароль переданный в аргументы метода
        if db_user[1] == user.password:
            return True

        print("Некорректный пароль")
        return False

    # Восстановление пароля
    def password_restore(self, user: User) -> bool:
        # Получаем пользователя из БД
        db_user = self.get_user(user)

        if db_user is None:
            print("Пользователь не существует")
            return False

        # Сравниваем код восстановления пользователя из БД и код переданный в аргументы
        if db_user[2] != user.code:
            print("Ввёден неверный код восстановления пароля.")
            return False

        # Подключаемся к БД для изменения пароля, в случае, если код соответствует
        with self.connect() as db:
            cur = db.cursor()
            update_params = (user.password, user.login,)

            cur.execute("""
                UPDATE users_data SET Password = ? WHERE Login = ?;
                """, update_params)

            db.commit()
            return True


# Класс приложения
class Application:
    # Добавляем менеджера для работы с БД
    def __init__(self, db_manager: DBManager):
        self.db = db_manager

    @staticmethod
    def welcome():
        print('Для выбора действия, введите нужный символ:\n'
              '1 - Регистрация нового пользователя\n'
              '2 - Авторизация в системе\n'
              '3 - Восстановление пароля\n'
              'x - Выход')

    @staticmethod
    def goodbye():
        print("Завершение работы. Всего доброго!")

    # Точка входа в приложение
    def start(self):
        self.welcome()

        while True:
            user_input = input()

            if user_input == '1':
                return self.registration()

            if user_input == '2':
                return self.authorisation()

            if user_input == '3':
                return self.password_recovery()

            if user_input == 'x':
                return self.goodbye()

            print("Некорректный ввод.\n"
                  "Повторите попытку:")

    # Модуль регистрации с проверкой валидации всех полей
    def registration(self):
        print('Процедура регистрации.')

        print('Введите логин (от 4 до 16 символов):')
        login = self.get_valid_login()

        print('Введите пароль (от 4 до 16 символов):')
        password = self.get_valid_password()

        print('Введите код для восстановления пароля (4 цифры):')
        code = self.get_valid_code()

        # Обращаемся к БД через менеджер для регистрации
        self.db.create_user(User(login, password, code))

    # Модуль валидации поля логин
    @staticmethod
    def get_valid_login() -> str:
        while True:
            login = input()

            if 3 < len(login) < 17:
                return login

            print("Длина логина должна быть от 4 до 16 символов.\n"
                  "Введите корректный логин:")

    # Модуль валидации поля пароль
    @staticmethod
    def get_valid_password() -> str:
        while True:
            password = input()

            if 3 < len(password) < 17:
                return password

            print("Длина пароля должна быть от 4 до 16 символов.\n"
                  "Введите корректный пароль:")

    # Модуль валидации поля код
    @staticmethod
    def get_valid_code() -> str:
        while True:
            code = input()

            if code.isdigit() and len(code) == 4:
                return code

            print("Код должен быть четырёхзначным числом.\n"
                  "Введите корректный код:")

    # Модуль авторизации с проверкой валидации всех полей
    def authorisation(self):
        print('Введите логин:')
        login = self.get_valid_login()

        print('Введите пароль:')
        password = self.get_valid_password()

        # Обращаемся к БД через менеджер для авторизации
        if self.db.login(User(login, password, None)):
            print("Авторизация прошла успешно")

    # Модуль восстановления пароля по коду с проверкой валидации всех полей
    def password_recovery(self):
        print('Процедура восстановления пароля.')

        print('Введите логин (от 4 до 16 символов):')
        login = self.get_valid_login()

        print('Введите код для восстановления пароля (4 цифры):')
        code = self.get_valid_code()

        print("Введите новый пароль:")
        new_password = self.get_valid_password()

        # Обращаемся к БД через менеджер для смены пароля по коду восстановления
        if self.db.password_restore(User(login, new_password, code)):
            print("Пароль успешно восстановлен.")


# Подключение к БД с помощью вспомогательного класса
db_name = 'registration.db'
db_manager = DBManager(db_name)

# Проверка добавления пользователя с помощью класса для работы с БД
# ivan = User('Ivan', 'qwer1234', '1234')
# db_manager.create_user(ivan)

# Запуск приложения с передачей менеджера по работе с БД в аргументах
Application(db_manager).start()
