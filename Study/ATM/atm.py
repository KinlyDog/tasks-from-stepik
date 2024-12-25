from sql_atm import SqlAtm
from card import Card


# toDo: Попробовать реализовать добавление класса карты непосредственно в конструктор.
# toDo: Возможно придется поменять реализацию, запрашивать сразу номер карты и пароль (эмуляция банкомата)

class ATM:
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

    # Выбор операции
    @staticmethod
    def welcome() -> None:
        print('Введите, пожалуйста, операцию которую хотите совершить:\n'
              '1. Узнать баланс\n'
              '2. Снять денежные средства\n'
              '3. Внести денежные средства\n'
              '4. Завершить работу\n'
              '5.\n'
              '6.\n')

    @staticmethod
    def goodbye() -> None:
        print('Спасибо за ваш визит. Всего доброго!')

    # Выбор операции
    def input_operation(self, card: Card) -> bool:
        self.welcome()

        while True:
            operation = input()

            if operation == '1':
                print(f'Ваш баланс: {card.balance}')
                return True

            if operation == '2':
                return self.cash_withdrawal(card)

            if operation == '3':
                self.depositing_cash(card)
                return True

            if operation == 'x':
                self.goodbye()
                return False

            else:
                print('Данная операция недоступна. Попробуйте другой ввод.')

    def cash_withdrawal(self, card) -> bool:
        amount_cash = self.correct_input_cash()

        if amount_cash > card.balance:
            print('На вашей карте недостаточно денежных средств.')
            return False

        return self.db.cash_withdrawal(card, amount_cash)

    @staticmethod
    def correct_input_cash() -> int:
        while True:
            amount_cash = input('Введите, пожалуйста, сумму которую хотите снять:\n')

            if not amount_cash.isdigit():
                print('Вы ввели некорректную сумму.')

            if int(amount_cash) > 0:
                return int(amount_cash)

    def depositing_cash(self, card):
        pass

    def atm_logic(self):
        user_2 = Card(2345, 2222, 10_000)
        SqlAtm.insert_user(user_2)
        SqlAtm.create_table()
        # SQLAtm.inserts_users((1234, 1111, 10000))
        number_card = input('Введите, пожалуйста, номер карты:\n')

        while True:
            if SqlAtm.input_card(number_card):
                if SqlAtm.input_code(number_card):
                    self.input_operation(number_card)
                    break
                else:
                    break
            else:
                break


start = ATM()
start.atm_logic()
