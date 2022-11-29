import numpy as np


def is_float(val: str):
    try:
        float(val)
        return True
    except ValueError:
        return False


def item_type(val: str):
    if val.isdigit() or (val.startswith('-') and val[1:].isdigit()):
        return 'int'
    if val in ["True", "False"]:
        return 'bool'
    if is_float(val):
        return 'float'
    return 'str'


def origin_type(val: str, t: str):
    if t == 'int':
        return int(val)
    if t == 'bool':
        return bool(val)
    if t == 'float':
        return float(val)
    return val


def dict_to_list(d: dict):
    arr = []
    for i in d:
        arr += [[i] + [d[i][j] for j in range(len(d[i]))]]
    return np.transpose(arr)


def list_to_dict(a: list):
    a = np.transpose(a)
    d = {}
    for r in range(len(a)):
        dict[a[r][0]] = []
    for r in range(len(a)):
        dict[a[r][0]] += [a[r][c] for c in range(1, len(a[r]))]
    return dict
