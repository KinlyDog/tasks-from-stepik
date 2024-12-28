import sqlite3
from card import Card
from typing import Optional, Tuple


class SqlAtm:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name  # Указываем имя БД для подключения

    # Подключаемся к БД
    def connect(self):
        return sqlite3.connect(self.db_name)

    # Вывод ошибки, в случае перехвата
    @staticmethod
    def exception(e: Exception):
        print('Операция не может быть исполнена по техническим причинам.\n'
              'Попробуйте позднее.\n')
        print(f'Код для службы поддержки {e}')

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

            try:
                cur.execute("""
                            INSERT INTO Users_data(UserID, Number_card, Pin_code, Balance)
                            VALUES(?, ?, ?, ?);
                            """, data_user)

                print("Пользователь успешно создан.")
            except Exception as e:
                self.exception(e)

    # Ввод и проверка номера карты
    def input_card(self, number_card: int) -> Optional[Tuple]:
        with self.connect() as db:
            cur = db.cursor()

            try:
                cur.execute("""
                        SELECT *
                        FROM Users_data
                        WHERE Number_card = ?
                        """, (number_card,))

                return cur.fetchone()
            except Exception as e:
                self.exception(e)
                return None

    # Изменение баланса карты, при снятии или пополнении
    def update_balance(self, card: Card, new_balance: int) -> Card:
        with self.connect() as db:
            cur = db.cursor()

            try:
                cur.execute("""
                            UPDATE Users_data
                            SET Balance = ?
                            WHERE Number_card = ?
                            """, (new_balance, card.number,))
                db.commit()

                print('Операция прошла успешно!')
                return Card(card.user_id, card.number, card.pin, new_balance)

            except Exception as e:
                self.exception(e)
                return card

    # Ввод и проверка номера карты получателя
    def input_client_card(self, number_card: int) -> bool:
        with self.connect() as db:
            cur = db.cursor()

            cur.execute("""
                    SELECT *
                    FROM Users_data
                    WHERE Number_card = ?
                    """, (number_card,))

            return cur.fetchone() is not None

    # Перевод денег другому клиенту
    def transfer_money(self, card: Card, amount_cash: int, client_card_number) -> Card:
        if self.input_card(client_card_number) is None:
            print('Неверно указан номер карты получателя.')
            return card

        new_balance = card.balance - amount_cash

        with self.connect() as db:
            cur = db.cursor()

            try:
                cur.execute("""
                            UPDATE Users_data
                            SET Balance = ?
                            WHERE Number_card = ?
                            """, (new_balance, card.number,))

                cur.execute("""
                            UPDATE Users_data
                            SET Balance = Balance + ?
                            WHERE Number_card = ?
                            """, (amount_cash, client_card_number,))
                db.commit()

                print('Перевод прошёл успешно.')
                return Card(card.user_id, card.number, card.pin, new_balance)

            except Exception as e:
                self.exception(e)
                return card
