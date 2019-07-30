def tab_verdade(n, funcao, nome_funcao):
    if (n < 2):
        print("Erro no parâmetro!")
        return

    print('|', end='')
    for i in range(n):
        print(' ' + chr(i+65) + ' |', end='')
    print(' '+nome_funcao)

    def print_valores(valores, funcao):
        print('|', end='')
        vant = False
        i = 0
        for c in valores:
            print(' {0} |'.format(int(c)), end='')
            if (i == 0):
                vant = c
            else:
                vant = funcao(vant, c)
            i += 1

        print(' {0}'.format(int(vant)))

    for i in range(pow(2, n)):
        x = "{0:b}".format(i).rjust(n, '0')
        valores = []
        for c in x:
            valores.append(c == '1')

        print_valores(valores, funcao)


tab_verdade(5, lambda x, y: x and y, 'AND')
print()
tab_verdade(3, lambda x, y: x or y, 'OR')
