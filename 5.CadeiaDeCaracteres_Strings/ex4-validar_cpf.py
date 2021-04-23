numero = input()
digito_verificador_1 = int(numero[-2])
digito_verificador_2 = int(numero[-1])

for n in numero:
    contagem = numero.count(n)
    if contagem % 11 == 0:
        print('false')
        break
    else:
        soma = 0
        ponderamento = 10
        for n in numero[:-2]:
            if n.isalnum():
                soma += int(n) * ponderamento
                ponderamento -= 1
        digito_verificador_calculado_1 = 11 - soma % 11
        if digito_verificador_calculado_1 >= 10:
            digito_verificador_calculado_1 = 0

        soma = 0
        ponderamento = 11
        for n in numero[:-1]:
            if n.isalnum():
                soma += int(n) * ponderamento
                ponderamento -= 1
        digito_verificador_calculado_2 = 11 - soma % 11
        if digito_verificador_calculado_2 >= 10:
            digito_verificador_calculado_2 = 0

        if ((digito_verificador_1, digito_verificador_2) == (digito_verificador_calculado_1, digito_verificador_calculado_2)):
            print('true')
        else:
            print('false')
