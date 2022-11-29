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
    print(config.table)
    newTable = config.table[start - 1:stop] if stop is not None else config.table[start - 1:]
    print(tabulate(newTable))
    if copy_table:
        config.copyTable = newTable
        copy()
    else:
        config.table = newTable
        save()


def get_rows_by_index(*vals, copy_table=False):
    print(config.table)
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
                types_dict[config.table[0][c]] += [item_type(config.table[r][c])]
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
        print(config.table[0][config.table.index(column)])
    return get_values(column)


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
    if len(config.table) == 1:
        if isinstance(column, int):
            config.table[0][column] = value
            print_table()
            return save()
        else:
            config.table[0][config.table[0].index(column)] = value
            return save()
    print('Таблица содержит больше одной строки. Используйте метод set_values')


def print_table():
    print(tabulate(config.table))


def add(start=1, stop=None, res_col=True, copy_table=False):
    start -= 1
    stop = stop - 1 if stop is not None else len(config.table) - 1
    s = [0 for i in range(len(config.table))]
    if all(item_type(str(config.table[r][c])) in ['int', 'float', 'bool'] for r in range(len(config.table)) for c in
           range(start, stop + 1)):
        for r in range(len(config.table)):
            for c in range(start, stop + 1):
                s[r] += config.table[r][c]
        finalize_arithm_op(s, res_col, copy_table)
    else:
        print('Сложить столбцы нельзя')


def sub(start=1, stop=None, res_col=True, copy_table=False):
    start -= 1
    stop = stop - 1 if stop is not None else len(config.table) - 1
    s = [config.table[0][i] for i in range(len(config.table[0]))]
    if all(item_type(str(config.table[r][c])) in ['int', 'float', 'bool'] for r in range(len(config.table)) for c in
           range(start, stop + 1)):
        for r in range(1, len(config.table)):
            for c in range(start, stop + 1):
                s[r] -= config.table[r][c]
        finalize_arithm_op(s, res_col, copy_table)
    else:
        print('Вычесть столбцы нельзя')


def mul(start=1, stop=None, res_col=True, copy_table=False):
    start -= 1
    stop = stop - 1 if stop is not None else len(config.table) - 1
    s = [1 for i in range(len(config.table))]
    if all(item_type(str(config.table[r][c])) in ['int', 'float', 'bool'] for r in range(len(config.table)) for c in
           range(start, stop + 1)):
        for r in range(len(config.table)):
            for c in range(start, stop + 1):
                s[r] *= config.table[r][c]
        finalize_arithm_op(s, res_col, copy_table)
    else:
        print('Умножить столбцы нельзя')


def div(start=1, stop=None, res_col=True, copy_table=False):
    start -= 1
    stop = stop - 1 if stop is not None else len(config.table) - 1
    s = [config.table[0][i] for i in range(len(config.table[0]))]
    if all(item_type(str(config.table[r][c])) in ['int', 'float', 'bool'] for r in range(len(config.table)) for c in
           range(start, stop + 1)):
        for r in range(1, len(config.table)):
            for c in range(start, stop + 1):
                try:
                    s[r] /= config.table[r][c]
                except ZeroDivisionError:
                    pass
        finalize_arithm_op(s, res_col, copy_table)
    else:
        print('Поделить столбцы нельзя')


def finalize_arithm_op(s, res_col=True, copy_table=False):
    for r in range(len(config.table)):
        if res_col:
            config.table[r] += [s[r]]
        else:
            config.table[r][len(config.table[r]) - 1] = s[r]
    print_table()
    if copy_table:
        copy()
    else:
        save()
