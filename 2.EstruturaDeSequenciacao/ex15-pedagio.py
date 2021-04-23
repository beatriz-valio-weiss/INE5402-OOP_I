# L: comprimento da estrada / D: distancia entre pedagios
L, D = [int(tamanho) for tamanho in input().split()]
# K: custo por km / P: preço pedagio
K, P = [int(valor) for valor in input().split()]

custo_total = (L*K) + (L//D)*P

print(custo_total)