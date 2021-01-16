from gen_list import *
from game_procedure import *


def card_check(card_num, name, column, whoisplaying, starting_dict, final_dict, is3rd, difficulty):
    cards = []
    row = []
    col = []
    while card_num < 2:
        r, c = pick_cards(card_num, column, name, whoisplaying - 1)
        r -= 1
        c -= 1
        row.append(r)
        col.append(c)
        card = final_dict[(r, c)]
        if card == starting_dict[(r, c)]:
            print('Η κάρτα αυτή είναι ήδη ανοιχτή.')
        else:
            card_num += 1
            starting_dict[(r, c)] = card
            cards.append(card)
            print_board(starting_dict, difficulty)
    return cards, row, col


def main():
    print('Καλώς ορίσατε στο παιχνίδι "Κάρτες αλά Πληροφορική 101" !!!,\n')
    print('Με λένε Πύθωνα και θα είμαι ο βοηθός σας. Ας ξεκινήσουμε!\n')

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

    starting_dict, final_dict = get_arrays(difficulty)
    from time import sleep

    print('Γίνεται ανακάτεμα των καρτών', end='')
    sleep(0.75)  # ένα μικρό εφέ
    text = '...'
    for i in range(3):
        print(text[i], end='');
        sleep(0.75)
        if i == 2:
            print('\n')

    Sum = [0] * player_num

    whoisplaying = 1
    while starting_dict != final_dict:
        print_board(starting_dict, difficulty)
        # δειχνει ποιος παικτης παιζει
        # αποθηκευονται τα φυλλα που επελεξε ο παικτης
        # cards = []
        # ο αριθμος καρτών που έχει ανοίξει ο παίκτης
        card_num = 0
        # αν ειναι True τοτε θα υπάρξει τρίτη καρτα
        is3rd = False
        cards, row, column = card_check(card_num, name, columns, whoisplaying, starting_dict, final_dict, is3rd, difficulty)
        Sum, whoisplaying, starting_dict = vathmoi(cards, Sum, name, whoisplaying, starting_dict, row, column, columns, final_dict, difficulty)
        whoisplaying += 1
        whoisplaying = whoisplaying % player_num

    max_idx = Sum.index(max(Sum))
    print(f'Νικητής είναι ο {name[max_idx]} με {Sum[max_idx]} πόντους!')


if __name__ == '__main__':
    main()
