from tabulate import tabulate
from helpers import *
import config
from fileModules import pickleModule, textModule, csvModule


def load():
    if config.fileType == 'csv':
        config.table = csvModule.load_table()
    if config.fileType == 'txt':
        config.table = textModule.load_table()
    if config.fileType == 'pickle':
        config.table = pickleModule.load_table()


def save():
    if config.fileType == 'csv':
        config.table = csvModule.save_table()
    if config.fileType == 'txt':
        config.table = textModule.save_table()
    if config.fileType == 'pickle':
        config.table = pickleModule.save_table()


def copy():
    config.copyName = input('Введите имя файла: ')
    config.copyType = input('Введите тип файла: ')
    if config.copyType == 'csv':
        config.copyTable = csvModule.copy_table()
    if config.copyType == 'txt':
        config.copyTable = textModule.copy_table()
    if config.copyType == 'pickle':
        config.copyTable = pickleModule.copy_table()


# номер строки, начиная с 1 (и до строки с номером stop включительно)
def get_rows_by_number(start=1, stop=None, copy_table=False):
    newTable = config.table[start - 1:stop] if stop is not None else config.table[start - 1:]
    print(tabulate(newTable))
    if copy_table:
        config.copyTable = newTable
        copy()
    else:
        config.table = newTable
        save()


def get_rows_by_index(*vals, copy_table=False):
    newTable = []
    for i in vals:
        for r in range(len(config.table)):
            if str(config.table[r][0]) == str(i):
                newTable += [config.table[r]]
    print(tabulate(newTable))
    if copy_table:
        config.copyTable = newTable
        copy()
    else:
        config.table = newTable
        save()


# индекс с 0
def get_column_types(by_number=True):
    if by_number:
        types_dict = {i: [] for i in range(len(config.table[0]))}
        for r in range(len(config.table)):
            for c in range(len(config.table[r])):
                types_dict[c] += [item_type(str(config.table[r][c]))]
    else:
        types_dict = {config.table[0][i]: [] for i in range(len(config.table[0]))}
        for r in range(1, len(config.table)):
            for c in range(len(config.table[r])):
                types_dict[config.table[0][c]] += [item_type(str(config.table[r][c]))]
    print(types_dict)


def set_column_types(types_dict, by_number=True):
    if by_number:
        for r in range(len(config.table)):
            for c in range(len(config.table[r])):
                try:
                    config.table[r][c] = types_dict[c][r](config.table[r][c])
                except:
                    pass
    else:
        for r in range(1, len(config.table)):
            for c in range(len(config.table[r])):
                try:
                    config.table[r][c] = types_dict[config.table[0][c]][r - 1](config.table[r][c])
                except:
                    pass
    print_table()
    return config.table


# индекс с 0
def get_values(column=0):
    res_col = []
    if isinstance(column, int):
        for r in range(len(config.table)):
            res_col += [config.table[r][column]]
    else:
        for r in range(1, len(config.table)):
            for c in range(len(config.table[r])):
                if config.table[0][c] == column:
                    res_col += [config.table[r][c]]
    print(res_col)


def get_value(column=0):
    if len(config.table) == 1:
        if isinstance(column, int):
            print(config.table[0][column])
        else:
            print(config.table[0][config.table.index(column)])
    else:
        print('В таблице больше одной строки. Используйте get_values()')


def set_values(values, column=0):
    if isinstance(column, int):
        for r in range(len(config.table)):
            for c in range(len(config.table[r])):
                if c == column:
                    try:
                        config.table[r][c] = values[r]
                    except IndexError:
                        pass
    else:
        for r in range(1, len(config.table)):
            for c in range(len(config.table[r])):
                if config.table[0][c] == column:
                    try:
                        config.table[r][c] = values[r]
                    except IndexError:
                        pass
    print_table()
    save()


def set_value(value, column=0):
    try:
        if isinstance(column, int):
            config.table[column] = value
            print_table()
            return save()
        else:
            config.table[0][config.table[0].index(column)] = value
            return save()
    except:
        print('Таблица содержит больше одной строки. Используйте метод set_values')


def print_table():
    print(tabulate(config.table))


def add(start=0, stop=len(config.table[0])-1, copy_table=False):
    newTable = config.table
    s = [0]*len(newTable)
    if all(item_type(str(newTable[r][c])) in ['int', 'float', 'bool'] for r in range(len(newTable)) for c in
           range(start, stop+1)):
        for r in range(len(newTable)):
            for c in range(start, stop+1):
                s[r] += newTable[r][c]
        for r in range(len(newTable)):
            newTable[r] += [s[r]]
        print(tabulate(newTable))
        if copy_table:
            config.copyTable = newTable
            copy()
        else:
            config.table = newTable
            save()
    else:
        print('Сложить столбцы нельзя')


def sub(start=0, stop=len(config.table[0])-1, copy_table=False):
    newTable = config.table
    s = [newTable[i][start] for i in range(len(newTable))]
    if all(item_type(str(newTable[r][c])) in ['int', 'float', 'bool'] for r in range(len(newTable)) for c in
           range(start, stop+1)):
        for r in range(len(newTable)):
            for c in range(start+1, stop+1):
                s[r] -= newTable[r][c]
        for r in range(len(newTable)):
            newTable[r] += [s[r]]
        print(tabulate(newTable))
        if copy_table:
            config.copyTable = newTable
            copy()
        else:
            config.table = newTable
            save()
    else:
        print('Вычесть столбцы нельзя')


def mul(start=0, stop=len(config.table[0])-1, copy_table=False):
    newTable = config.table
    s = [1]*len(newTable)
    if all(item_type(str(newTable[r][c])) in ['int', 'float', 'bool'] for r in range(len(newTable)) for c in
           range(start, stop+1)):
        for r in range(len(newTable)):
            for c in range(start, stop+1):
                s[r] *= newTable[r][c]
        for r in range(len(newTable)):
            newTable[r] += [s[r]]
        print(tabulate(newTable))
        if copy_table:
            config.copyTable = newTable
            copy()
        else:
            config.table = newTable
            save()
    else:
        print('Умножить столбцы нельзя')


def div(start=0, stop=len(config.table[0])-1, copy_table=False):
    newTable = config.table
    s = [newTable[i][start] for i in range(len(newTable))]
    if all(item_type(str(newTable[r][c])) in ['int', 'float', 'bool'] for r in range(len(newTable)) for c in
           range(start, stop+1)):
        for r in range(len(newTable)):
            for c in range(start+1, stop+1):
                try:
                    s[r] /= newTable[r][c]
                except ZeroDivisionError:
                    pass
        for r in range(len(newTable)):
            newTable[r] += [s[r]]
        print(tabulate(newTable))
        if copy_table:
            config.copyTable = newTable
            copy()
        else:
            config.table = newTable
            save()
    else:
        print('Поделить столбцы нельзя')
