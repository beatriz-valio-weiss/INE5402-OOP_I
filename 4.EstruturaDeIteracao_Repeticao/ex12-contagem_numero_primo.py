num_inicial = int(input())
num_final = int(input())

divisores_possiveis = 0
qtd_primo = 0

for intervalo in range (num_inicial, num_final + 1):
    for teste in range (1, intervalo + 1):
        if intervalo % teste == 0:
            divisores_possiveis += 1
        else:
            divisores_possiveis += 0
    if divisores_possiveis == 2:
        qtd_primo += 1
    else:
        qtd_primo += 0
    divisores_possiveis = 0

print(qtd_primo)