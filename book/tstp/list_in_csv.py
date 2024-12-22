import csv

films_list = [["Звёздные войны", "Терминатор", "Искусственный интеллект"],
              ["Дурак", "Матильда", "Левиафан"],
              ["Люди в черном", "Я - робот", "Эволюция"]]

with open("st.csv", "w", newline='') as file:
    w = csv.writer(file, delimiter=",")

    for films in films_list:
        w.writerow(films)

with open('st.csv', 'r') as file:
    r = csv.reader(file, delimiter=',')

    for row in r:
        print(",".join(row))