from Study.ATM.card import Card
from sql_atm import SqlAtm
from typing import Optional


# Класс безопасности, для аутентификации
class Security:
    # Добавляем класс для работы с БД
    def __init__(self, sql_atm: SqlAtm):
        self.db = sql_atm

    # Логика аутентификации (получение номера карты и пин-кода)
    def authenticate(self) -> Optional[Card]:
        card = self.input_number()

        if card is None:
            return None

        if self.input_pin(card.pin):
            return card

    # Ввод номера карты (3 попытки)
    def input_number(self) -> Optional[Card]:
        result = None
        print('Добро пожаловать!')

        for _ in range(3):
            print('Введите номер карты:')
            number_card = input().strip()

            if number_card.isdigit() and len(number_card) == 4:
                result = self.db.input_card(int(number_card))

            if result:
                return Card(*result)

            print('Введен некорректный номер карты.')

        print('Сожалеем, но количество попыток ввода исчерпано.')
        return None

    # Ввод пин-кода карты (3 попытки)
    @staticmethod
    def input_pin(card_pin: int) -> bool:
        for _ in range(3):
            input_pin = input('Введите пин-код:\n')

            if input_pin == str(card_pin):
                return True

            print('Введен некорректный пин-код.')

        print('Сожалеем, но количество попыток ввода исчерпано.')
        return False
