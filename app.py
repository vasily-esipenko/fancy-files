from tableOperations import *
import config


def app():
    config.fileName = input('Введите имя файла: ')
    config.fileType = input('Введите тип файла: ')
    config.pickleTableType = input('Тип огранизации данных (list/dict): ') if config.fileType == 'pickle' else ''
    load()
    print(tabulate(config.table))
    op = input('Введите операцию: ')
    while op != 'exit':
        if op == 'save':
            save()
        if op == 'copy':
            copy()
        if op == 'get_rows_by_number':
            start = int(input('Введите номер строки, с которой начать: '))
            try:
                stop = int(input('Введите номер строки, на которой закончить: '))
            except ValueError:
                stop = None
            copy_table = input('Скопировать таблицу? (y/n): ') == 'y'
            get_rows_by_number(start, stop, copy_table)
        if op == 'get_rows_by_index':
            vals = input('Введите первые элементы строк: ').split()
            copy_table = input('Скопировать таблицу? (y/n): ') == 'y'
            get_rows_by_index(*vals, copy_table=copy_table)
        if op == 'get_column_types':
            by_number = input('По номеру? (y/n): ') == 'y'
            get_column_types(by_number)
        if op == 'set_column_types':
            types_dict = {}
            by_number = input('По номеру? (y/n): ') == 'y'
            set_column_types(types_dict, by_number)
        if op == 'get_values':
            column = input('Введите номер столбца: ')
            try:
                column = int(column)
            except ValueError:
                pass
            get_values(column)
        if op == 'get_value':
            column = input('Введите номер столбца: ')
            try:
                column = int(column)
            except ValueError:
                pass
            get_values(column)
        if op == 'set_values':
            column = input('Введите номер столбца: ')
            values = input('Введите значения для столбца (через пробел): ').split()
            values = [origin_type(value, item_type(value)) for value in values]
            try:
                column = int(column)
            except ValueError:
                pass
            set_values(values, column)
        if op == 'set_value':
            column = input('Введите номер столбца: ')
            value = input('Введите значение для столбца: ')
            value = origin_type(value, item_type(value))
            try:
                column = int(column)
            except ValueError:
                pass
            set_value(value, column)
        if op == 'add':
            res_col = input('Записать результат вычислений в новый столбец справа? (y/n): ') == 'y'
            copy_table = input('Скопировать таблицу? (y/n): ') == 'y'
            add(res_col, copy_table)
        if op == 'sub':
            res_col = input('Записать результат вычислений в новый столбец справа? (y/n): ') == 'y'
            copy_table = input('Скопировать таблицу? (y/n): ') == 'y'
            sub(res_col, copy_table)
        if op == 'mul':
            res_col = input('Записать результат вычислений в новый столбец справа? (y/n): ') == 'y'
            copy_table = input('Скопировать таблицу? (y/n): ') == 'y'
            mul(res_col, copy_table)
        if op == 'div':
            res_col = input('Записать результат вычислений в новый столбец справа? (y/n): ') == 'y'
            copy_table = input('Скопировать таблицу? (y/n): ') == 'y'
            div(res_col, copy_table)
        print(tabulate(config.table))
        op = input('Введите операцию: ')


app()
