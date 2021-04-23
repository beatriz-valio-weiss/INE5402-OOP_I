qtd_casos = int(input())

for a in range(qtd_casos):
    qtd_alunos, n_secreto = [int(x) for x in input().split()]
    valores = [int(x) for x in input().split()]
    
    diferenca_comparativa = 100
    
    for n in range(len(valores)):
        if n_secreto == valores[n]:
            ganhador = n + 1
            break
        else:
            diferenca = abs(n_secreto - valores[n])
            if diferenca < diferenca_comparativa:
                diferenca_comparativa = diferenca
                ganhador = n + 1
    print(ganhador)