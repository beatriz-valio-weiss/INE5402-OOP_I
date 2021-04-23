numero_saltadores = int(input())
melhor_salto = -1
melhor_saltador = ''

for n in range (numero_saltadores):
    distancia_1, distancia_2, distancia_3, nome = input().split()
    distancia_1 = float(distancia_1)
    distancia_2 = float(distancia_2)
    distancia_3 = float(distancia_3)
    maior_distancia = max(distancia_1, distancia_2, distancia_3)
    if maior_distancia > melhor_salto:
        melhor_salto = maior_distancia
        melhor_saltador = nome
    
print(melhor_saltador)