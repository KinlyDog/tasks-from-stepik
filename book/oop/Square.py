class Square:
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def __repr__(self):
        _ = str(self.s1)

        return f'{_} x {_} x {_} x {_}'

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)

b_square = Square(50)
print(a_square.square_list)

print(b_square)