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

    # Создание пользователя
    def create_user(self, user: User) -> bool:
        # Подключаемся к БД для создания пользователя
        with self.connect() as db:
            cur = db.cursor()

            # Параметры для запроса получаем из объекта User переданного в аргументы метода
            data_user = (user.rub, user.usd, user.eur)

            cur.execute("""
                        INSERT INTO users_balance(Balance_RUB, Balance_USD, Balance_EUR)
                        VALUES (?, ?, ?);
                        """, data_user)

            db.commit()
            print("Пользователь успешно добавлен.")
            return True

    def exchange(self, target_currency: str, new_amount: float, source_currency: str, amount: float) -> str:
        # Подключаемся к БД
        with self.connect() as db:
            cur = db.cursor()

            # Запрашиваем данные пользователя
            cur.execute("""
                        SELECT *
                        FROM users_balance
                        WHERE UserID = 1;
                        """)

            user_data = list(cur.fetchone()) # получаем данные пользователя в список
            user_data[int(source_currency)] -= new_amount # изменяем количество исходной валюты
            user_data[int(target_currency)] += amount # изменяем количество новой валюты

            # При отсутствии нужной суммы, радуем пользователя
            if user_data[int(source_currency)] < 0:
                return 'Недостаточно средств в выбранной валюте.'

            # Загоняем обновленные данные в кортеж для использования параметризированного запроса
            update_params = (user_data[1], user_data[2], user_data[3], 1)

            cur.execute("""
                        UPDATE users_balance SET Balance_RUB = ?, Balance_USD = ?, Balance_EUR = ?
                        WHERE UserID = ?; 
                        """, update_params)

            # Фиксируем изменения
            db.commit()

            return (f'Обмен успешно произведен.\n\n'
                    f'Ваш баланс:\n'
                    f'{user_data[1]:.1f} RUB\n'
                    f'{user_data[2]:.1f} USD\n'
                    f'{user_data[3]:.1f} EUR')
