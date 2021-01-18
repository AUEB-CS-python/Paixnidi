from get_new_pairs import find_pair, check_if_opened
history_symbols = []
history_coords = []


def get_indexes(item):
    indexes = []
    for i, a in enumerate(history_symbols):
        if a == item:
            indexes.append(i)
    return indexes


def get_doubles(starting_dict):
    n = len(history_coords)
    for i in range(n):
        first = history_coords[i]
        for j in range(i+1, n):
            second = history_coords[j]
            if history_symbols[i][0] == history_symbols[j][0] and history_symbols[i] != '-1':
                if starting_dict[first][0] == 'X' and starting_dict[second][0] == 'X':
                    return [first, second]

    return [(-1, -1), (-1, -1)]


def check_history_symbols(symbol):
    indexes = []
    flag = False
    for i, lst in enumerate(history_symbols):
        if symbol == lst[0]:
            flag = True
            indexes.append(i)
    return indexes, flag


def play_turn(starting_dict, final_dict, number_of_cols):
    coords = get_doubles(starting_dict)
    if (-1, -1) != coords[0]:
        starting_dict[coords[0]] = final_dict[coords[0]]
        starting_dict[coords[1]] = final_dict[coords[1]]
        idx_1 = history_coords.index(coords[0])
        idx_2 = history_coords.index(coords[1])
        history_symbols[idx_1] = '-1'
        history_symbols[idx_2] = '-1'

        return coords, starting_dict, history_coords
    else:
        r, c = find_pair(starting_dict, number_of_cols, history_coords)
        symbol = final_dict[(r, c)][0]
        starting_dict[(r, c)] = final_dict[(r, c)]
        coords = [(r, c)]
        indexes, flag = check_history_symbols(symbol)
        flag2 = False
        for index in indexes:
            if not check_if_opened(history_coords[index], starting_dict):
                flag2 = True
                break
        if flag and flag2:
            starting_dict[history_coords[index]] = final_dict[history_coords[index]]
            history_symbols[index] = '-1'
            coords.append(history_coords[index])
            return coords, starting_dict, history_coords
        else:
            r, c = find_pair(starting_dict, number_of_cols, history_coords)
            coords.append((r, c))
            starting_dict[(r, c)] = final_dict[r, c]
            if final_dict[coords[0]][0] != final_dict[coords[1]][0]:
                history_symbols.append(final_dict[coords[0]])
                history_symbols.append(final_dict[coords[1]])
                history_coords.append(coords[0])
                history_coords.append(coords[1])

            return coords, starting_dict, history_coords
