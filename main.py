from gen_list import *
from game_procedure import *
print('Καλώς ορίσατε στο παιχνίδι "Κάρτες αλά Πληροφορική 101" !!!,\n')
print('Με λένε Πύθωνα και θα είμαι ο βοηθός σας. Ας ξεκινήσουμε!\n')
difficulty = input("Δώστε επίπεδο δυσκολίας: Εύκολο (1), Μέτριο (2), Δύσκολο (3): ")
set_difficulty()
difficulty=set_difficulty()[0]
columns=set_difficulty()[1]
get_arrays(difficulty)
final = get_arrays(difficulty)[1] # αυτη θα δωθει ως παραδειγμα εμφανισης
print('Ακολουθεί ενδεικτικό στήσιμο καρτών.')
print_board(final, columns, True)
player_num=set_player_num()
name=[]
for i in range(player_num):
    name.append(input('Πως θες να ονομάζεσαι παίκτη '+str(i)+' ? '))
name.sort()
get_arrays(difficulty)
starting=get_arrays(difficulty)[0]
final=get_arrays(difficulty)[1]
from time import sleep
print('Γίνεται ανακάτεμα των καρτών',end=''); sleep(0.75)
text='...'
for i in range(3):
    print(text[i],end=''); sleep(0.75)
    if i==2:
        print('\n')
print_board(starting,columns,False)
for i in range(player_num):
    sum[i]=0
while starting!=final:
is3rd=False
pick_cards(columns,is3rd)