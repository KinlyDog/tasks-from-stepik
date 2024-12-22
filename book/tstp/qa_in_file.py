answer = input("Вы гей?")

with open("answer.txt", 'w') as file:
    file.write(answer)

with open('answer.txt', 'r') as file:
    print(file.read())