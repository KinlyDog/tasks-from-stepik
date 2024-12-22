class Animal:
    def __init__(self, name: str, age: int, speed: int = 0):
        self._name = name
        self._age = age
        self._speed = speed

    def say(self):
        return "I'm Animal"

    @property
    def name(self):
        return self._name

    def name_set(self, name):
        return Animal(name, self._age, self._speed)

    @property
    def age(self):
        return self._age

    @property
    def speed(self):
        return self._speed


class Cat(Animal):
    def __init__(self, name: str, age: int, speed: int = 5, jump: int = 7):
        super().__init__(name, age, speed)
        self._jump = jump

    def say(self):
        return "Meow!"


barsik = Animal("Barsik", 5)
print(barsik.name)
print(barsik.speed)
print(barsik.say())

vasiliy = Cat("Vasiliy", 7, 10)
print(vasiliy.name)
print(vasiliy.age)
print(vasiliy.speed)
print(vasiliy.say())

print(barsik)
new_Cat = barsik.name_set("Klitor")
print(new_Cat)