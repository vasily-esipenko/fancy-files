import pickle

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
