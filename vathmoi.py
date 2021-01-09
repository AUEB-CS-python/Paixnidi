def vathmoi()
    sum=0
    if cards[0]=='A' :
        p=1
        sum+=p
    elif cards[0] in [str(i) for i in range(2, 11)]:
        p=int(card)
        sum+=p
    elif cards[0] in ['J', 'Q', 'K'] :
        if cards[0]==['J'] :
            p=10
            sum+=p
            #play again
        elif cards[0]==['K']:
            p=10
            sum+=p
            #xanei seira o epomenos
        elif cards == ['K'] + ['Q'] :
            #anoigeis kai 3h karta
            #an tautizontai pairnei p==10
            p=10
    return sum
