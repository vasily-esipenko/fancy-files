import pickle
import config
from helpers import *


def load_table():
    with open(f"files/{config.fileName}.pickle", "rb") as file:
        lf = pickle.load(file)
        return lf if config.pickleTableType == 'arr' else dict_to_list(lf)


def save_table():
    with open(f"files/{config.fileName}.pickle", "wb") as file:
        if config.pickleTableType == 'arr':
            pickle.dump(config.table, file)
        else:
            pickle.dump(list_to_dict(config.table), file)
    return load_table()


def copy_table():
    with open(f"copiedFiles/{config.copyName}.pickle", "wb") as file:
        if config.pickleTableType == 'arr':
            pickle.dump(config.copyTable, file)
        else:
            pickle.dump(list_to_dict(config.copyTable), file)
