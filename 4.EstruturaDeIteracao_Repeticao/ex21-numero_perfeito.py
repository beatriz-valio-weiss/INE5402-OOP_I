qtd_casos = int(input())

for i in range (qtd_casos):
    numero = int(input())
    soma = 0
    for n in range (1, numero):
        if numero % n == 0:
            soma += n
    if soma == numero:
        print(numero, "eh perfeito")
    else:
        print(numero, "nao eh perfeito")