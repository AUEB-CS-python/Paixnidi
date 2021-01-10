def vathmoi(cards1, cards2,sum,i):
    if cards1[0] == cards2[0]:
        if cards1[0] == 'A':
            p = 1
            sum[i] += p
        elif cards1[0] in [str(i) for i in range(2, 11)]:
            p = int(cards1[0])
            sum[i] += p
        elif cards1[0] in ['J', 'Q', 'K']:
            if cards1[0] == ['J']:
                p = 10
                sum[i] += p
                # play again
            elif cards1[0] == ['K']:
                p = 10
                sum[i] += p
                # xanei seira o epomenos
            elif cards1[0] == ['Q']:
                p = 10
                sum[i] += p
    #elif (cards1[0] == ['K'] and cards2[0] == ['Q']) or cards1[0] == ['Q'] and cards2[0] == ['K']:
    return sum