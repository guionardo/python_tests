def tabela_verdade():


    # var = int(input('Digite a quantidade de variáveis da expressão booleana: '))
    var = 3
    if var == 1:
        print('| A |')
        for a in False, True:
            print('| {0} |'.format(int(a)))

    elif var == 2:
        print('| A | B |')
        for a in False, True:
            for b in False, True:
                print('|{0} | {1} |'.format(int(a), int(b)))
    elif var == 3:
        print('| A | B | C |')
        for a in False, True:
            for b in False, True:
                for c in False, True:
                    print('| {0} | {1} | {2} |'.format(int(a), int(b), int(c)))
    elif var == 4:
        print('| A | B | C | D |')
        for a in False, True:
            for b in False, True:
                for c in False, True:
                    for d in False, True:
                        print('| {0} | {1} | {2} | {3} |'.format(int(a), int(b), int(c), int(d)))
    elif var == 5:
        print('| A | B | C | D | E |')
        for a in False, True:
            for b in False, True:
                for c in False, True:
                    for d in False, True:
                        for e in False, True:
                            print('| {0} | {1} | {2} | {3} | {4} |'.format(int(a), int(b), int(c), int(d), int(e)))
    elif var == 6:
        print('| A | B | C | D | E | F |')
        for a in False, True:
            for b in False, True:
                for c in False, True:
                    for d in False, True:
                        for e in False, True:
                            for f in False, True:
                                print('| {0} | {1} | {2} | {3} | {4} | {5} |'.format(int(a), int(b), int(c), int(d), int(e), int(f)))
    elif var == 7:
        print('| A | B | C | D | E | F | G |')
        for a in False, True:
            for b in False, True:
                for c in False, True:
                    for d in False, True:
                        for e in False, True:
                            for f in False, True:
                                for g in False, True:
                                    print('| {0} | {1} | {2} | {3} | {4} | {5} | {6} |'.format(int(a), int(b), int(c), int(d), int(e), int(f), int(g)))
    else:
        print('Digite valores entre 1 e 7, por favor')
        tabela_verdade()


tabela_verdade()