from Study.ATM.security import Security
from sql_atm import SqlAtm
from card import Card


class ATM:
    def __init__(self, db_manager: SqlAtm):
        self.db = db_manager
        self.security = Security(db_manager)
        self.card = None

    def start(self):
        # Запуск процесса аутентификации
        self.card = self.security.authenticate()

        if self.card:
            self.input_operation()  # Если аутентификация успешна, продолжаем
        else:
            print("Аутентификация не удалась.")

    # Выбор операции
    @staticmethod
    def welcome() -> None:
        print('Введите, пожалуйста, операцию которую хотите совершить:\n'
              '1. Узнать баланс\n'
              '2. Снять денежные средства\n'
              '3. Внести денежные средства\n'
              'x. Завершить работу\n'
              '5.\n'
              '6.\n')

    @staticmethod
    def goodbye() -> None:
        print('Спасибо за ваш визит. Всего доброго!')

    # Выбор операции
    def input_operation(self) -> None:
        self.welcome()
        operation = input()

        while operation not in ('1', '2', '3', 'x'):
            print('Данная операция недоступна. Попробуйте другой ввод.\n')
            operation = input()

        if operation == 'x':
            return self.goodbye()

        if operation == '1':
            self.balance()

        if operation == '2':
            self.cash_withdrawal()

        if operation == '3':
            self.depositing_cash(self.card)

    def balance(self) -> None:
        print(f'Ваш баланс: {self.card.balance}\n')
        self.menu()

    def menu(self) -> None:
        print('Выберите нужный раздел:\n'
              '1. Вернуться в главное меню.\n'
              'x. Завершить обслуживание')

        while True:
            op = input()

            if op == '1':
                return self.input_operation()

            if op == 'x':
                return self.goodbye()

            print('Данная операция недоступна. Попробуйте другой ввод.')

    def cash_withdrawal(self) -> bool:
        amount_cash = self.correct_input_cash()

        self.card = self.db.cash_withdrawal(self.card, amount_cash)
        self.balance()
        return True

    def correct_input_cash(self) -> int:
        while True:
            amount_cash = input('Введите, пожалуйста, сумму которую хотите снять:\n')

            if not amount_cash.isdigit() or int(amount_cash) < 1:
                print('Вы ввели некорректную сумму.')

            if int(amount_cash) < self.card.balance:
                return int(amount_cash)

            print('На вашей карте недостаточно денежных средств.')

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
