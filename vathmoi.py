def vathmoi(cards1, cards2) :
    sum=0
    if cards1[0]==cards2[0] :
        if cards1[0]=='A' :
            p=1
            sum+=p
        elif cards1[0] in [str(i) for i in range(2, 11)]:
            p=int(cards1[0])
            sum+=p
        elif cards1[0] in ['J', 'Q', 'K'] :
            if cards1[0]==['J'] :
                p=10
                sum+=p
                #play again
            elif cards1[0]==['K']:
                p=10
                sum+=p
                #xanei seira o epomenos
            elif cards1[0] == ['K'] + ['Q'] :
                #anoigeis kai 3h karta
                #an tautizontai pairnei p==10
                p=10
            elif cards1[0] == ['Q']:
                p=10
                sum += p
    return sum
