from gen_list import print_board
from get_new_pairs import find_pair
import time

def set_player_num():
    while True:
        try:
            player_num = input('Δώστε αριθμό παικτών: ')
            player_num = int(player_num)
            if player_num == 0:
                print('Πρέπει να συμμετέχει τουλάχιστον ένας παίκτης. Ξαναδοκιμάστε. ')
                pass
            else:
                break
        except:
            print('Δώσε ακέραιο αριθμό')
            pass
    return player_num


def pick_cards(card_num, columns, name, whoisplaying):
    valid = False
    while not valid:
        try:
            row, column = input(
                name[whoisplaying] + ' δώσε γραμμή και στήλη ' + str(card_num+1) + 'ης κάρτας (πχ 2,3): ').split(',')
        except:
            print('Προέκυψε σφάλμα.  Παρακαλώ ξαναδοκίμασε. ')
        else:
            if row not in (str(j + 1) for j in range(4)):
                print('Η γραμμή πρέπει να είναι αριθμός από το 1 έως το 4. Ξαναδοκίμασε. ')
            elif column not in (str(j + 1) for j in range(columns)):
                print('Η στήλη πρέπει να είναι αριθμός από το 1 έως το ' + str(columns) + '. Ξαναδοκίμασε. ')
            else:
                valid = True
                row = int(row)
                column = int(column)
                return row, column


def print_win_msg(name, whoisplaying, sum, p):
    print(f'Μπράβο { name[whoisplaying-1] }!!! Kερδίζεις { str(p) } πόντους. '
          f'Οι συνολικοί σου πόντοι είναι {sum[whoisplaying-1]}.')


def vathmoi(cards, sum, name, whoisplaying, starting_dict, row, column, total_cols, final_dict, difficulty, cards_left, isComputer, history_coords):
    next = cards[1][0]
    current = cards[0][0]
    if current == next:
        cards_left -= 2
        if current == 'A':
            p = 1
            sum[whoisplaying-1] += p
            print_win_msg(name, whoisplaying, sum, p)
        elif current in [str(i) for i in range(2, 11)]:
            p = int(current)
            sum[whoisplaying-1] += p
            print_win_msg(name, whoisplaying, sum, p)
        elif current in ['J', 'Q', 'K']:
            if current == 'J':
                p = 10
                sum[whoisplaying-1] += p
                print_win_msg(name, whoisplaying, sum, p)
                whoisplaying -= 1
                if cards_left > 0:
                    print('Ξαναπαίζεις! ')
            elif current == 'K':
                p = 10
                sum[whoisplaying-1] += p
                print_win_msg(name, whoisplaying, sum, p)
                whoisplaying += 1
                if cards_left > 0:
                    print('Ο επόμενος παίκτης χάνει την σειρά του! ')
            elif current == 'Q':
                p = 10
                sum[whoisplaying-1] += p
                print_win_msg(name, whoisplaying, sum, p)
    elif current == 'K' and next == 'Q' or current == 'Q' and next == 'K':
        valid = False
        while not valid:
            if isComputer:
                r, c = find_pair(starting_dict, total_cols, history_coords)
            else:
                r, c = pick_cards(2, total_cols, name, whoisplaying-1)
                r -= 1
                c -= 1
            card = final_dict[(r, c)]
            if card == starting_dict[(r, c)]:
                print('Η κάρτα αυτή είναι ήδη ανοιχτή.')
            else:
                valid = True
                # an einai kai ta duo K tote xanei th seira o epomenos?
                starting_dict[(r, c)] = card
                p = 0
                print_board(starting_dict, difficulty)
                time.sleep(1)
                if card[0][0] == 'K':
                    whoisplaying += 1
                    print('Ο επόμενος παίκτης χάνει την σειρά του! ')
                    cards_left -= 2
                    p = 10
                    if current == 'K':
                        starting_dict[(row[1], column[1])] = ['X', ' ']
                    else:
                        starting_dict[(row[0], column[0])] = ['X', ' ']
                elif card[0][0] == 'Q':
                    cards_left -= 2
                    p = 10
                    if current == 'Q':
                        starting_dict[(row[1], column[1])] = ['X', ' ']
                    else:
                        starting_dict[(row[0], column[0])] = ['X', ' ']
                else:
                    for i in range(2):
                        starting_dict[(row[i], column[i])] = ['X', ' ']
                    starting_dict[(r, c)] = ['X', ' ']
                    print('Οι κάρτες δεν ταιριάζουν. Δεν κερδίζεις πόντους. ')
                if p > 0:
                    sum[whoisplaying-1] += p
                    print_win_msg(name, whoisplaying - (1 if card[0][0] == 'K' else 0), sum, p)
    else:
        print('Οι κάρτες δεν ταιριάζουν. Δεν κερδίζεις πόντους. ')

        for i in range(2):
            starting_dict[(row[i], column[i])] = ['X', ' ']
    return sum, whoisplaying, starting_dict, cards_left