# Класс пользователя
class Card:
    def __init__(self, user_id: int, number: int, pin: int, balance: int) -> None:
        self.user_id = user_id
        self.number = number
        self.pin = pin
        self.balance = balance