from gen_list import *
from game_procedure import *

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

final = get_arrays(difficulty)[1]  # αυτη θα δωθει ως παραδειγμα εμφανισης
print('Ακολουθεί ενδεικτικό στήσιμο καρτών.')
print_board(final, difficulty)
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
            x=input()
name.sort()

starting, final = get_arrays(difficulty)
from time import sleep

print('Γίνεται ανακάτεμα των καρτών', end='');
sleep(0.75)  # ένα μικρό εφέ
text = '...'
for i in range(3):
    print(text[i], end='');
    sleep(0.75)
    if i == 2:
        print('\n')
print_board(starting, difficulty)

Sum = []
for i in range(player_num):
    Sum.append(0)

def card_check(card_num, columns, name, whosplaying,starting, final, cards, is3rd):
    while card_num<2 or is3rd==False:
        row, column = pick_cards(card_num, columns, name, whosplaying - 1)
        card = final[row - 1][column - 1][0] + final[row - 1][column - 1][1]
        if card == starting[row - 1][column - 1]:
            print('Η κάρτα αυτή είναι ήδη ανοιχτή.')
            row, column = pick_cards(columns, card_num, name, whosplaying - 1)
        else:
            cards.append(card)
            starting[row - 1][column - 1] = cards[card_num - 1]
            print_board(starting, difficulty)
            card_num += 1
    print('mlkia1')
    return cards,row,column

while True:
    whosplaying=1
    cards=[]
    card_num = 0
    is3rd = False
    cards,row,column = card_check(card_num, columns, name, whosplaying,starting, final, cards, is3rd)
    print('mlkia2')
    if card_num == 2:
        vathmoi(cards,Sum,whosplaying-1,name)
    print('mlkia3')