from user import User
from db_manager import DBManager


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
