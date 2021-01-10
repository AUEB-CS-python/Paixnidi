def set_difficulty():
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
    return [difficulty,columns]

def set_player_num():
    player_num = input('Δώστε αριθμό παικτών. ')
    while True:
        l = len(player_num)
        for i in range(l):
            if player_num[i] not in (str(j) for j in range(10)):
                valid = False
                break
            else:
                valid = True
        if player_num == '0':
            print('Πρέπει να συμμετέχει τουλάχιστον ένας παίκτης. Ξαναδοκιμάστε. ')  # για num=1 θα το κανουμε μετα
            player_num = input()
        elif valid == False:
            print('Ουπς! Κάτι πήγε στραβά. Παρακαλώ ξαναδοκιμάστε.')
            player_num = input()
        else:
            player_num = int(player_num)
            break
    return player_num

def pick_cards(columns,is3rd):
    for i in range(2 + is3rd):
        while True:
                try:
                x, y = input('Δώστε γραμμή και στήλη ' + str(i + 1) + 'ης κάρτας (πχ 2,3): ').split(',')

                if x not in (str(j+1) for j in range(4)):
                    print('Η γραμμή πρέπει να είναι αριθμός από το 1 έως το 4. Ξαναδοκιμάστε. ')
                    x,y=input().split(',')
                elif y not in (str(j+1) for j in range(columns)):
                    print('Η στήλη πρέπει να είναι αριθμός από το 1 έως το '+str(columns)+'. Ξαναδοκιμάστε. ')
                    x, y = input().split(',')
                except ValueError:
                    print('Ο αριθμός γραμμής και στήλης πρέπει να χωρίζεται με "," . Ξαναδοκιμάστε. ')
                    x, y = input().split(',')
                