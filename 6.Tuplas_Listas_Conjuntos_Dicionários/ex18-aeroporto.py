qtd_aeroportos, qtd_voos = [int(x) for (x) in input().split()]
teste = 1

while qtd_aeroportos != 0 and qtd_voos!= 0:
    locais = []
    contador = dict()

    for q in range(qtd_voos):
        locais += [int(y) for (y) in input().split()]

    for n in (locais):
        if n not in contador:
            contador[n] = locais.count(n)

    n_comparacao = 0
    comparador = 0
    maior_trafego = ''
    for c in contador:
        n_comparacao = contador[c]
        if n_comparacao > comparador:
            comparador = n_comparacao
            maior_trafego = str(c)
        elif n_comparacao == comparador:
            maior_trafego += ' ' + str(c)
        
    print('Teste {}'.format(teste))
    print(maior_trafego)
    print()
    qtd_aeroportos, qtd_voos = [int(x) for (x) in input().split()]
    teste += 1