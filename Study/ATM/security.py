from sql_atm import SqlAtm


class Security:
    # Добавляем менеджера для работы с БД
    def __init__(self, db_manager: SqlAtm):
        self.db = db_manager

    def start(self):
        card = self.input_number()

        if self.input_pin(card.pin):
            self.input_operation(card)

    @staticmethod
    def input_pin(card_pin: int) -> bool:
        while True:
            input_pin = input('Введите пин-код.\n'
                              'Для завершения обслуживания введите "x":\n')

            if input_pin == 'x':
                return False

            if input_pin == str(card_pin):
                return True

            print('Введен некорректный пин-код.')

    # Добавить тип возвращаемого значения
    def input_number(self) -> Card:
        while True:
            card = None

            number_card = input('Введите номер карты.\n'
                                'Для завершения обслуживания введите "x":\n')

            if number_card == 'x':
                quit()  # переписать

            if number_card.isdigit() and len(number_card) == 4:
                card = self.db.input_card(int(number_card))

            if card is Card:
                return card

            print('Введен некорректный номер карты.')