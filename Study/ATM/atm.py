from Study.ATM.security import Security
from sql_atm import SqlAtm
from card import Card


class ATM:
    def __init__(self, sql_atm: SqlAtm):
        self.db = sql_atm  # Подключаем класс для работы с БД
        self.security = Security(sql_atm)  # Класс для аутентификации
        self.card = None  # Класс карты (пользователя)

    # Запуск процесса аутентификации
    def start(self) -> None:
        self.card = self.security.authenticate()

        if self.card:
            self.main_menu()  # Если аутентификация успешна, продолжаем
        else:
            print("Аутентификация не удалась.")

    def main_menu(self) -> None:
        while True:
            print('\nВведите, пожалуйста, номер операции которую хотите совершить:\n'
                  '1. Узнать баланс\n'
                  '2. Снять денежные средства\n'
                  '3. Внести денежные средства\n'
                  '4. Перевести денежные средства\n'
                  '5. Завершить работу')

            operation = input().strip()

            if operation == "1":
                self.show_balance()
            elif operation == "2":
                self.withdraw_cash()
            elif operation == "3":
                self.deposit_cash()
            elif operation == "4":
                self.transfer_money()
            elif operation == "5":
                print("Спасибо за визит. До свидания!")
                return
            else:
                print("Некорректный ввод. Попробуйте ещё раз.")

    # 1. Узнать баланс
    def show_balance(self) -> None:
        print(self.card.balance)

    # Корректный ввод суммы
    @staticmethod
    def correct_input_amount() -> int:
        while True:
            amount = input("Введите сумму:\n").strip()

            if amount.isdigit() and int(amount) > 0:
                return int(amount)

            print("Некорректный ввод. Повторите попытку.")

    # 2. Снять денежные средства
    def withdraw_cash(self) -> None:
        print("Введите сумму которую хотите снять:")
        amount = self.correct_input_amount()

        if not self.is_amount_within_balance(amount):
            return

        new_balance = self.card.balance - amount

        self.card = self.db.update_balance(self.card, new_balance)
        self.show_balance()

    # 3. Внести денежные средства
    def deposit_cash(self) -> None:
        print("Введите сумму которую хотите внести:")
        amount = self.correct_input_amount()

        new_balance = self.card.balance + amount

        self.card = self.db.update_balance(self.card, new_balance)
        self.show_balance()

    # 4. Перевести денежные средства
    def transfer_money(self) -> None:
        print("Введите сумму которую хотите перевести:")
        amount = self.correct_input_amount()

        if not self.is_amount_within_balance(amount):
            return

        client_card_number = self.correct_input_card_number()

        if client_card_number == -1:
            print('Вы ввели некорректный номер карты получателя.')
            return

        self.card = self.db.transfer_money(self.card, amount, client_card_number)
        self.show_balance()

    # Корректный ввод номера карты
    @staticmethod
    def correct_input_card_number() -> int:
        print('Введите номер карты:')
        number_card = input().strip()

        if number_card.isdigit() and len(number_card) == 4:
            return int(number_card)

        return -1

    # Проверка, что сумма не превышает баланс
    def is_amount_within_balance(self, amount: int) -> bool:
        if amount > self.card.balance:
            print("На вашем счёте недостаточно средств.")
            return False

        return True
