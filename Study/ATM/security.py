from Study.ATM.card import Card
from sql_atm import SqlAtm
from typing import Optional


class Security:
    # Добавляем менеджера для работы с БД
    def __init__(self, db_manager: SqlAtm):
        self.db = db_manager

    def authenticate(self) -> Optional[Card]:
        # Логика аутентификации (получение номера карты и пин-кода)
        card = self.input_number()

        if card is None:
            return None

        if self.input_pin(card.pin):
            return card

    # Возможно стоит добавить проверку на корректность
    def input_number(self) -> Optional[Card]:
        for _ in range(3):
            result = None

            number_card = input('Введите номер карты:\n')

            if number_card.isdigit() and len(number_card) == 4:
                result = self.db.input_card(int(number_card))

            if result is not None:
                return Card(*result)

            print('Введен некорректный номер карты.')

        print('Сожалеем, но количество попыток ввода исчерпано.')
        return None

    @staticmethod
    def input_pin(card_pin: int) -> bool:
        for _ in range(3):
            input_pin = input('Введите пин-код:\n')

            if input_pin == str(card_pin):
                return True

            print('Введен некорректный пин-код.')

        print('Сожалеем, но количество попыток ввода исчерпано.')
        return False
