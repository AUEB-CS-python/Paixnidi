from random import shuffle


# Συνάρτηση που επιστρέφει μια λίστα που έχει όλες τις 52 πιθανές κάρτες μιας τράπουλας
def gen_array():
    # Σύμβολα μιας  τράπουλας
    symbols = ['♥', '♣', '♦', '♠']
    # Οι πιθανές κάρτες χωρίς σύμβολα
    cards = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']
    # Τελική λίστα
    res = []
    # 13 γιατί υπάρχουν 13 διαφορετικές κάρτες χωρίς σύμβολο
    for i in range(13):
        # 4 γιατί υπάρχουν 4 σύμβολα
        for j in range(4):
            # append στην τελική λίστα
            res.append([cards[i], symbols[j]])
    return res


# Συνάρτηση που εμφανίζει τα στοιχεία του πίνακα μαζί με τους αριθμούς στηλών και γραμμών,
# matrix είναι ο πίνακας μορφής 4*m και m είναι ο αριθμός των στηλών
def print_board(matrix, diff):
    levels = [4, 10, 13]
    m = levels[diff-1]
    n = 4
    # λίστα που έχει τους αριθμούς στηλών 1-m
    lst = [' '] + [str(i) for i in range(1, m+1)]
    # Η πρώτη γραμμή εποτελέιται μόνο από τους αριθμούς των στηλών
    for item in lst:
        print(item, end="  ")
    print("\n")
    # Για κάθε γραμμή
    for i in range(n):
        # εμφανίζει τον αριθμό της γραμμής
        print(str(i+1), end=" ")
        # Για κάθε στήλη
        for j in range(m):
            # item είναι το στοιχείο του πίνακα που βρίσκεται στη γραμμή i και στήλη j
            item = matrix[i][j]
            # item[0] + item[1] επειδή το item είναι λίστα δυο στοιχείων
            print(item[0] + item[1], end=" ")

        print("\n")


# Συνάρτηση που μετατρέπει λίστα μορφής 1 x (4*m) σε πίνακα μορφής 4 x m
# gen είναι λίστα μορφής 1 x (4*m), m είναι ο αριθμός των στηλών
def create_final(gen, m):
    res = []
    # Για κάθε γραμμή
    for i in range(4):
        # Λίστα που θα περιέχει τα στοιχεία της i γραμμής
        row = []
        for j in range(m):
            row.append(gen[m*i + j])
        res.append(row)
    return res
        

# Συνάρτηση που επιστρέφει μια λίστα που περιέχει δύο στοιχεία
# Το πρώτο στοιχείο είναι ένας πίνακας που περιέχει μόνο Χ
# Το δεύτερο στοιχείο είναι ένας πίνακας που περιέχει
# ανακατεμένες κάρτες μαζί με σύμβολα με βάση τη δυσκολία
def get_arrays(difficulty):
    # Λίστα με όλες τις πιθανές κάρτες μιας τράπουλας
    gen = gen_array()
    # είναι τα 3 επίπεδα, και αν diff είναι 1 θα έχει 4 στηλες κλπ
    levels = [4, 10, 13]

    # Αν είναι δυσκολίας 1, διάλεξε τα 16 τελευταία στοιχεία της λίστας (10 - Κ)
    if difficulty == 1:
        gen = gen[-4*4:]
    # Αν είναι δυσκολίας 2, διάλεξε τα 40 πρώτα στοιχεία της λίστας (Α-10)
    elif difficulty == 2:
        gen = gen[:4*10]

    # Αν είναι δυσκολίας 3, θα υπάρχουν όλα τα φύλλα
    # Το dif θα είναι ο αριθμός των στηλών
    dif = levels[difficulty-1]
    # Ανακάτεψε τη λίστα που περιέχει τις κάρτες με βάση τη δυσκολία
    shuffle(gen)
    # Μετέτρεψε τη λίστα σε πίνακα 4 x m
    final = create_final(gen, dif)

    # Πίνακας που περιέχει μόνο Χ διαστάσεων 4 x m
    starting = create_final([['X', ' ']]*(4*dif), dif)

    return [starting, final]


# diff = int(input("Δώστε επίπεδο δυσκολίας Εύκολο (1), Μέτριο (2), Δύσκολο (3): "))
# starting, final = get_arrays(diff)
# print_board(starting, diff)
# print('\n\n')
# print_board(final, diff)
