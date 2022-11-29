import csv
from helpers import *
import config


def load_table():
    with open(f"./files/{config.fileName}.csv", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        file_arr = []
        for row in reader:
            file_arr += [row]
    for r in range(len(file_arr)):
        for c in range(len(file_arr[r])):
            file_arr[r][c] = origin_type(file_arr[r][c], item_type(file_arr[r][c]))
    return file_arr


def save_table():
    with open(f"./files/{config.fileName}.csv", "w", newline='') as file:
        file.truncate()
        writer = csv.writer(file, delimiter=',')
        for row in config.table:
            writer.writerow(row)
    return load_table()


def copy_table():
    with open(f"./copiedFiles/{config.copyName}.csv", "w", newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for row in config.copyTable:
            writer.writerow(row)
