import sqlite3
from typing import Optional, Tuple

from user import User


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
