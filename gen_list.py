from random import shuffle

def gen_array():
    # 3: Heart, 4: diamond, 5: clubs, 6: spades
    symbols = [chr(i) for i in range(3, 7)]
    cards = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']
    res = []
    for i in range(13):
        for j in range(4):
            res.append([cards[i], symbols[j]])
    return res

def print_board(matrix, m, flag):
    n = 4
    lst = [' '] + [str(i) for i in range(1, m+1)]
    for item in lst:
        print(item, end = "  " if flag else " ")
    print("\n")
    for i in range(n):
        print(str(i+1), end=" ")
        for j in range(m):
            item = matrix[i][j]
            if flag:
                print(item[0] + item[1], end=" ")
            else:
                print(item, end=" ")
            
        print("\n")

def create_final(gen, m):
    res = []
    for i in range(4):
        row = []
        for j in range(m):
            row.append(gen[m*i + j])
        res.append(row)
    return res
        

def get_arrays(difficulty):
    gen = gen_array()
    levels = [4, 10, 13]
    
    if difficulty == 1:
        gen = gen[-4*4:]
    elif difficulty == 2:
        gen = gen[:4*10]

    dif = levels[difficulty-1]
    shuffle(gen)
    final = create_final(gen, dif)
    starting = create_final(['X']*(4*dif), dif)
    #print_board(starting, dif, False)
    return [starting, final]
