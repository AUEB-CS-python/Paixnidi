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


def vathmoi(cards, sum, i, name):
    if cards[0][0] == cards[1][0]:
        if cards[0][0] == 'A':
            p = 1
            sum[i] += p
            print('Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[
                i] + '.')
        elif cards[0][0] in [str(i) for i in range(2, 11)]:
            p = int(cards[0][0])
            sum[i] += p
            print('Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[
                i] + '.')
        elif cards[0][0] in ['J', 'Q', 'K']:
            if cards[0][0] == ['J']:
                p = 10
                sum[i] += p
                print(
                    'Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[
                        i] + '.')
                # play again
            elif cards[0][0] == ['K']:
                p = 10
                sum[i] += p
                print(
                    'Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[
                        i] + '.')
                # xanei seira o epomenos
            elif cards[0][0] == ['Q']:
                p = 10
                sum[i] += p
                print(
                    'Μπράβο ' + name[i] + '!!! Kερδίζεις ' + str(p) + ' πόντους. Οι συνολικοί σου πόντοι είναι ' + sum[
                        i] + '.')
    elif cards[0][0] == ['K'] and cards[1][0] == ['Q'] or cards[0][0] == ['Q'] and cards[1][0] == ['K']:
        is3rd=True
        cards, row, column = card_check(starting, final, cards, card_num, is3rd)
        """"
        row, column = pick_cards(columns, card_num + 1, name)
        card = final[row - 1][column - 1][0] + final[row - 1][column - 1][1]
        if card == starting[row - 1][column - 1]:
            print('Η κάρτα αυτή είναι ήδη ανοιχτή.')
            card = pick_cards(columns, card_num, final)
        else:
            cards.append(card)
            starting[row - 1][column - 1] = cards[card_num - 1]
            print_board(starting, difficulty)
            """
    else:
        print('Οι κάρτες δεν ταιριάζουν. Δεν κερδίζεις πόντους. ')

    return sum
