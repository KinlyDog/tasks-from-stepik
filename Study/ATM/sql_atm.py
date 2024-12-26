import sqlite3
from card import Card
from typing import Optional, Tuple


class SqlAtm:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name  # Указываем имя БД для подключения

    # Подключаемся к БД
    def connect(self):
        return sqlite3.connect(self.db_name)

    # Создание таблицы Users_data
    def create_table(self):
        with self.connect() as db:
            cur = db.cursor()

            cur.execute("""
                        CREATE TABLE IF NOT EXISTS Users_data(
                        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Number_card INTEGER NOT NULL,
                        Pin_code INTEGER NOT NULL,
                        Balance INTEGER NOT NULL);
                        """)

            print("Создание таблицы Users_data")

    # Создание нового пользователя
    def insert_user(self, user: Card):
        with self.connect() as db:
            cur = db.cursor()
            data_user = (None, user.number, user.pin, user.balance,)

            cur.execute("""
                        INSERT INTO Users_data(UserID, Number_card, Pin_code, Balance)
                        VALUES(?, ?, ?, ?);
                        """, data_user)

            print("Создание нового пользователя")

    # Ввод и проверка номера карты
    def input_card(self, number_card: int) -> Optional[Tuple]:
        with self.connect() as db:
            cur = db.cursor()

            cur.execute("""
                    SELECT *
                    FROM Users_data
                    WHERE Number_card = ?
                    """, (number_card,))

            return cur.fetchone()

    # Снятие денежных средств с баланса карты
    def cash_withdrawal(self, card: Card, amount_cash: int) -> Card:
        with self.connect() as db:
            cur = db.cursor()

            new_balance = card.balance - amount_cash

            cur.execute("""
                        UPDATE Users_data
                        SET Balance = ?
                        WHERE Number_card = ?
                        """, (new_balance, card.number,))
            db.commit()

            return Card(card.user_id, card.number, card.pin, new_balance)


    # Снятие денежных средств с баланса карты
    @staticmethod
    def depositing_money(number_card: int) -> bool:
        amount = input('Введите пожалуйста сумму которую желаете внести: ')

        with sqlite3.connect('atm.db') as db:
            try:
                cur = db.cursor()

                cur.execute("""
                                    UPDATE Users_data
                                    SET Balance = Balance + ?
                                    WHERE Number_card = ?
                                    """, (amount, number_card,))
                db.commit()
                SqlAtm.info_balance(number_card)
            except:
                print('Попытка выполнить некорректное действие')
                return False
