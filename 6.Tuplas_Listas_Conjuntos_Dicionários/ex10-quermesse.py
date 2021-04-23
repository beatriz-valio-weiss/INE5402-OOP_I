n_teste = 1

n_participantes = int(input())

while n_participantes != 0:
    n_ingresso = [int(n_participantes) for n_participantes in input().split()]
    for a in range(1, len(n_ingresso)+1):
        if a == n_ingresso[a - 1]:
            print("Teste", n_teste)
            print(a)
            print("")
            break
    n_teste += 1
    n_participantes = int(input())