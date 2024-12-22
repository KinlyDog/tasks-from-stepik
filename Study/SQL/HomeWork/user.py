# Класс пользователя
class User:
    def __init__(self, login: str, password: str, code: str):
        self.login = login
        self.password = password
        self.code = code