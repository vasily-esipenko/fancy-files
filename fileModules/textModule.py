import config
from helpers import *


def load_table():
    with open(f"./files/{config.fileName}.txt", newline='') as file:
        file_arr = []
        for line in file:
            file_arr += [line.split(config.txtDelimiter)]
        for r in range(len(file_arr)):
            for c in range(len(file_arr[r])):
                file_arr[r][c] = origin_type(file_arr[r][c], item_type(file_arr[r][c]))
        return file_arr


def save_table():
    with open(f"./files/{config.fileName}.txt", "w", newline='') as file:
        file.truncate()
        for row in config.table:
            file.write(config.txtDelimiter.join([str(item) for item in row]))
    return load_table()


def copy_table():
    with open(f"./copiedFiles/{config.copyName}.txt", "w", newline='') as file:
        for row in config.copyTable:
            file.write(config.txtDelimiter.join([str(item) for item in row]))
