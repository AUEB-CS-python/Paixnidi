from main import card_check
from gen_list import print_board


def set_player_num():
    while True:
        try:
            player_num = input('Δώστε αριθμό παικτών: ')
            player_num = int(player_num)
            if player_num <= 0:
                print('Πρέπει να συμμετέχει τουλάχιστον ένας παίκτης. Ξαναδοκιμάστε. ')
                pass
            else:
                break
        except:
            print('Δώστε ακέραιο αριθμό: ')
            pass
    return player_num


def activate_bonus1():
    bonus1 = False
    x = input('Θέλετε να ενεργοποιήσετε την λειτουργία bonus 1? (ναι/όχι/help): ')
    while True:
        if x.lower() == 'ναι':
            bonus1 = True
            return bonus1
        elif x.lower() == 'οχι' or x.lower() == 'όχι':
            return bonus1
        elif x.lower() == 'help':
            print("""Με την λειτουργία bonus1 κερδίζετε πόντους και όταν τα επιλγμένα φύλλα ανήκουν στην ίδια σειρά.
            π.χ. 6♥ και 9♥. """)
            x = input('Θέλετε να ενεργοποιήσετε την λειτουργία bonus 1? (ναι/όχι/help): ')
        else:
            print('Σφάλμα. Παρακαλώ απαντήστε με ένα ναι, όχι ή help. ')
            χ=input()

def pick_cards(card_num, columns, name, whoisplaying):
    valid = False
    while not valid:
        try:
            row, column = input(
                name[whoisplaying] + ' δώσε γραμμή και στήλη ' + str(card_num + 1) + 'ης κάρτας (πχ 2,3): ').split(',')
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
    print(f'Μπράβο {name[whoisplaying - 1]}!!! Kερδίζεις {str(p)} πόντους. '
          f'Οι συνολικοί σου πόντοι είναι {sum[whoisplaying - 1]}.')


def vathmoi(cards, sum, name, whoisplaying, starting_dict, row, column, total_cols, final_dict, difficulty, bonus1):
    next_symbol = cards[1][0]
    current_symbol = cards[0][0]
    earntpoints1 = True
    earntpoints2 = False
    do_plus1=False
    do_minus1=False

    if bonus1:
        # order εννοουνται τα '♥', '♣', '♦', '♠'
        next_order = cards[1][1]
        current_order = cards[0][1]
        if next_symbol == 'A':
            p2 = 1
        elif next_symbol in [str(i) for i in range(2, 11)]:
            p2 = int(next_symbol)
        elif next_symbol in ['J', 'Q', 'K']:
            p2 = 10
        if current_symbol == 'A':
            p1 = 1
        elif current_symbol in [str(i) for i in range(2, 11)]:
            p1 = int(current_symbol)
        elif current_symbol in ['J', 'Q', 'K']:
            p1 = 20
        if next_order == current_order:
            sum[whoisplaying - 1] += p1 + p2
            earntpoints2=True

    if current_symbol == next_symbol:
        if current_symbol == 'A':
            p = 1
            sum[whoisplaying - 1] += p
        elif current_symbol in [str(i) for i in range(2, 11)]:
            p = int(current_symbol)
            sum[whoisplaying - 1] += p
        elif current_symbol in ['J', 'Q', 'K']:
            if current_symbol == 'J':
                p = 10
                sum[whoisplaying - 1] += p
                whoisplaying -= 1
                do_plus1=True
                print('Ξαναπαίζεις! ')
            elif current_symbol == 'K':
                p = 10
                sum[whoisplaying - 1] += p
                whoisplaying += 1
                do_minus1=True
                print('Ο επόμενος παίκτης χάνει την σειρά του! ')
            elif current_symbol == 'Q':
                p = 10
                sum[whoisplaying - 1] += p
    elif current_symbol == 'K' and next_symbol == 'Q' or current_symbol == 'Q' and next_symbol == 'K':
        valid = False
        while not valid:
            r, c = pick_cards(2, total_cols, name, whoisplaying - 1)
            r -= 1
            c -= 1
            card = final_dict[(r, c)]
            if card == starting_dict[(r, c)]:
                print('Η κάρτα αυτή είναι ήδη ανοιχτή.')
            else:
                valid = True
                # an einai kai ta duo K tote xanei th seira o epomenos
                starting_dict[(r, c)] = card
                p = 0
                print_board(starting_dict, difficulty)
                third_card_symbol=cards[0][0]
                if third_card_symbol == 'K':
                    p = 10
                    sum[whoisplaying - 1] += p
                    #if current_symbol == 'K':
                        # starting_dict[(row[1], column[1])] = ['X', ' ']
                    #else:
                        # starting_dict[(row[0], column[0])] = ['X', ' ']
                elif third_card_symbol == 'Q':
                    p = 10
                    sum[whoisplaying - 1] += p
                    #if current_symbol == 'Q':
                        #starting_dict[(row[1], column[1])] = ['X', ' ']
                    #else:
                        #starting_dict[(row[0], column[0])] = ['X', ' ']
                else:
                    earntpoints1 = False
                if bonus1:
                    third_card_order = cards[0][1]
                    if third_card_symbol == 'A':
                        p3 = 1
                    elif third_card_symbol in [str(i) for i in range(2, 11)]:
                        p3 = int(third_card_symbol)
                    elif third_card_symbol in ['J', 'Q', 'K']:
                        p3 = 10
                    if third_card_order==next_order:
                        if earntpoints2==True:           # αν True τότε ισχύει ότι next_order==current_order
                            sum[whoisplaying - 1] += p3  # άρα απλά προστίθεται και η αξία της τρίτης κάρτας
                        else:
                            sum[whoisplaying - 1] += p2+p3
                            earntpoints2=True
                    elif third_card_order==current_order:
                        sum[whoisplaying - 1] += p1+p3
                        earntpoints2=True
                # for i in range(2):
                #    starting_dict[(row[i], column[i])] = ['X', ' ']
                # starting_dict[(r, c)] = ['X', ' ']
    else:
        earnpoints1 = False
        # print('Οι κάρτες δεν ταιριάζουν. Δεν κερδίζεις πόντους. ')
    # for i in range(2):
    #    starting_dict[(row[i], column[i])] = ['X', ' ']
    if earntpoints1 or earntpoints2:
        if do_minus1:
            a = whoisplaying - 1
        elif do_plus1:
            a = whoisplaying + 1
        else:
            a = whoisplaying
            p=sum[a-1]
            print_win_msg(name, a, sum, p)
    else:
        print('Οι κάρτες δεν ταιριάζουν. Δεν κερδίζεις πόντους. ')
    return sum, whoisplaying, starting_dict
