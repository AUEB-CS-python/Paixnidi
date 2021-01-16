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

def vathmoi(cards, sum, name,whoisplaying,starting,row,column):
    if cards[0][0] == cards[1][0]:
        if cards[0][0] == 'A':
            p = 1
            sum[whoisplaying-1] += p
            print('Μπράβο ' + name[whoisplaying-1] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[
                i] + '.')
        elif cards[0][0] in [str(i) for i in range(2, 11)]:
            p = int(cards[0][0])
            sum[whoisplaying-1] += p
            print('Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[
                whoisplaying-1] + '.')
        elif cards[0][0] in ['J', 'Q', 'K']:
            if cards[0][0] == ['J']:
                p = 10
                sum[whoisplaying-1] += p
                print('Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[whoisplaying-1] + '.')
                whoisplaying-=1
                print('Ξαναπαίζεις! ')
            elif cards[0][0] == ['K']:
                p = 10
                sum[whoisplaying-1] += p
                print('Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[whoisplaying-1] + '.')
                whoisplaying+=1
                print('Ο επόμενος παίκτης χάνει την σειρά του! ')
            elif cards[0][0] == ['Q']:
                p = 10
                sum[whoisplaying-1] += p
                print('Μπράβο ' + name[whoisplaying-1] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[whoisplaying-1] + '.')
    elif cards[0][0] == ['K'] and cards[1][0] == ['Q'] or cards[0][0] == ['Q'] and cards[1][0] == ['K']:
        is3rd=True
        cards, row, column = card_check(card_num, columns, name, whoisplaying,starting, final, cards, is3rd)
        if cards[2][0]=='Q':
            p=10
            sum[whoisplaying-1]+=p
            print('Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[whoisplaying-1] + '.')
            if cards[0][0]=='Q':
                starting[row[1]-1][column[1]-1]='X'
            else:
                starting[row[0] - 1][column[0] - 1] = 'X'
        elif cards[2][0]=='K':
            p = 10
            sum[whoisplaying - 1] += p
            print('Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[whoisplaying-1] + '.')
            if cards[0][0] == 'K':
                starting[row[1] - 1][column[1] - 1] = 'X'
            else:
                starting[row[0] - 1][column[0] - 1] = 'X'
        else:
            print('Οι κάρτες δεν ταιριάζουν. Δεν κερδίζεις πόντους. ')
            for i in range(3):
                starting[row[i] - 1][column[i] - 1] = 'X'
    else:
        print('Οι κάρτες δεν ταιριάζουν. Δεν κερδίζεις πόντους. ')
        for i in range(2):
            starting[row[i] - 1][column[i] - 1] = 'X'
    return sum,whoisplaying,starting