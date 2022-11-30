import pickle
import csv

# создать pickle-файл на основе словаря
d = {
    'name': ['Alex', 'Ian', 'John'],
    'age': [18, 16, 25],
    'occupation': ['student', 'student', 'doctor']
}
with open('./files/dict.pickle', 'wb') as f:
    pickle.dump(d, f)

# создать pickle-файл на основе списка
arr = [['name', 'age', 'occupation'],
       [18, 16, 25],
       ['student', 'student', 'doctor']]
with open('./files/arr.pickle', 'wb') as f:
    pickle.dump(arr, f)


rand = [
    [1, 2, 3, 4],
    [55, True, 'auto', 132.3],
    [False, 'summer', 22, 44.5]
]
with open("./files/random.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for row in rand:
        writer.writerow(row)

num = [
    [1, 2, 3, 4],
    [55, 6, 21, 132.3],
    [11.67, 3.1415, 22, 44.5],
    [True, False, True, False]
]
with open("./files/num.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for row in num:
        writer.writerow(row)

onerow = [[123, 'альфа', 3.1415, True]]
with open("./files/onerow.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for row in onerow:
        writer.writerow(row)

numrow = [[222, 333, 545.323, 12]]
with open("./files/numrow.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for row in numrow:
        writer.writerow(row)

text = [
    ['hello', 'world'],
    [333, 25],
    [True, False]
]
with open("./files/text.txt", "w", newline='') as file:
    for row in text:
        file.write(','.join([str(item) for item in row]) + ' \n')
