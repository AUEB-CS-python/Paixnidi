from random import randint


def check_if_opened(coords, starting_dict):
    if starting_dict[coords][0] == 'X':
        return False
    return True


def find_opened_columns(starting_dict, col_numbers):
    opened_cols = []
    for j in range(col_numbers):
        flag = True
        for i in range(4):
            if check_if_opened((i, j), starting_dict):
                flag = False
        if flag:
            opened_cols.append(j)

    return opened_cols


def find_opened_rows(starting_dict, col_numbers):
    opened_rows = []
    for i in range(4):
        flag = True
        for j in range(col_numbers):
            if check_if_opened((i, j), starting_dict):
                flag = False
        if flag:
            opened_rows.append(i)
    return opened_rows


def get_available_pairs(starting_dict, number_of_cols, history_coords):
    res = []
    for i in range(4):
        for j in range(number_of_cols):
            if not check_if_opened((i, j), starting_dict) and (i, j) not in history_coords:
                res.append((i, j))
    return res


def find_pair(starting_dict, number_of_cols, history_coords):
    pairs = get_available_pairs(starting_dict, number_of_cols, history_coords)
    idx = randint(0, len(pairs)-1)
    r = pairs[idx][0]
    c = pairs[idx][1]

    return r, c
