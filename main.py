from gen_list import *
from game_procedure import *
from computer import play_turn
import time

def card_check(card_num, name, column, whoisplaying, starting_dict, final_dict, difficulty):
    cards = []
    row = []
    col = []
    while card_num < 2:
        r, c = pick_cards(card_num, column, name, whoisplaying - 1)
        r -= 1
        c -= 1
        card = final_dict[(r, c)]
        if card == starting_dict[(r, c)]:
            print('Η κάρτα αυτή είναι ήδη ανοιχτή.')
        else:
            row.append(r)
            col.append(c)
            card_num += 1
            starting_dict[(r, c)] = card
            cards.append(card)
            print_board(starting_dict, difficulty)
    return cards, row, col


def main():
    print('Καλώς ορίσατε στο παιχνίδι "Κάρτες αλά Πληροφορική 101" !!!,\n')
    print('Με λένε Μπάμπη και θα είμαι ο βοηθός σας. Ας ξεκινήσουμε!\n')

    difficulty = input("Δώστε επίπεδο δυσκολίας: Εύκολο (1), Μέτριο (2), Δύσκολο (3): ")
    while True:
        if difficulty in ('1', '2', '3'):
            difficulty = int(difficulty)
            break
        else:
            print('Ουπς! Κάτι πήγε στραβά. Παρακαλώ απαντήστε με τους αριθμούς 1, 2 ή 3. ')
            difficulty = input()
    if difficulty == 1:
        columns = 4
    elif difficulty == 2:
        columns = 10
    else:
        columns = 13

    final_dict = get_arrays(difficulty)[1]  # αυτη θα δωθει ως παραδειγμα εμφανισης
    print('Ακολουθεί ενδεικτικό στήσιμο καρτών.')
    print_board(final_dict, difficulty)
    player_num = set_player_num()

    name = []
    for i in range(player_num):
        x = input('Πως θες να ονομάζεσαι παίκτη ' + str(i + 1) + ' ? ')
        while True:
            if x not in name:
                name.append(x)
                break
            else:
                print('Παίκτη ' + str(i + 1) + ' διάλεξε κάποιο διαφορετικό όνομα. ')
                x = input()
    name.sort()

    bonus1 = activate_bonus1()

    starting_dict, final_dict = get_arrays(difficulty)
    from time import sleep

    print('Γίνεται ανακάτεμα των καρτών', end='')
    sleep(0.75)  # ένα μικρό εφέ
    text = '...'
    for i in range(3):
        print(text[i], end='')
        sleep(0.75)
        if i == 2:
            print('\n')

    if player_num > 1:
        Sum = [0] * player_num

        whoisplaying = 1
        cards_left = columns*4
        while starting_dict != final_dict:
            print_board(starting_dict, difficulty)
            cards, row, column = card_check(0, name, columns, whoisplaying, starting_dict, final_dict, difficulty)
            Sum, whoisplaying, starting_dict, cards_left = vathmoi(cards, Sum, name, whoisplaying, starting_dict, row, column, final_dict, difficulty, cards_left, False, [],bonus1)
            whoisplaying += 1
            whoisplaying = whoisplaying % player_num

        max_idx = Sum.index(max(Sum))
        print(f'Νικητής είναι ο {name[max_idx]} με {Sum[max_idx]} πόντους!')
    else:
        print("Διάλεξες να παίξεις με τον υπολογιστή.")
        name.append('Υπολογιστής')
        player_num += 1

        whoisplaying = 1
        Sum = [0, 0]
        cards_left = 4*columns

        while starting_dict != final_dict:
            print_board(starting_dict, difficulty)
            if whoisplaying == 1:
                cards, row, column = card_check(0, name, columns, whoisplaying, starting_dict, final_dict, difficulty)
                Sum, whoisplaying, starting_dict, cards_left = vathmoi(cards, Sum, name, whoisplaying, starting_dict,
                                                                       row, column, columns, final_dict, difficulty,
                                                                       cards_left, False, [],bonus1)
            else:
                coords, starting_dict, history_coords = play_turn(starting_dict, final_dict, columns)
                cards = [final_dict[coords[0]], final_dict[coords[1]]]
                row = [coords[0][0], coords[1][0]]
                column = [coords[0][1], coords[1][1]]
                print('Ο πίνακας με τις κάρτες που διάλεξε ο υπολογιστής:')
                print_board(starting_dict, difficulty)
                time.sleep(1)
                Sum, whoisplaying, starting_dict, cards_left = vathmoi(cards, Sum, name, whoisplaying, starting_dict, row, column, columns, final_dict, difficulty, cards_left, True, history_coords,bonus1)
            whoisplaying += 1
            whoisplaying = whoisplaying % player_num
        max_idx = Sum.index(max(Sum))
        print(f'Νικητής είναι ο {name[max_idx]} με {Sum[max_idx]} πόντους!')


if __name__ == '__main__':
    main()
