class Car:
    def __init__(self, model: str, year: int, v_engine: float, price: int, mileage: int):
        self.model = model
        self.year = year
        self.v_engine = v_engine
        self.price = price
        self.mileage = mileage
        self.wheel = 4

    def description(self):
        return (f'Модель: {self.model}\n'
                f'Год выпуска: {self.year}\n'
                f'Объём двигателя: {self.v_engine}\n'
                f'Цена: {self.price}\n'
                f'Пробег: {self.mileage}\n'
                f'Кол-во колёс: {self.wheel}\n')


toyota_camry = Car("Toyota Camry", 1998, 2.4, 450_000, 328_932)
print(toyota_camry.description())


class Truck(Car):
    def __init__(self, model: str, year: int, v_engine: float, price: int, mileage: int):
        super().__init__(model, year, v_engine, price, mileage)
        self.wheel = 8


kamaz = Truck("KamAZ 43082", 2024, 3.8, 6_410_000, 0)
print(kamaz.description())
