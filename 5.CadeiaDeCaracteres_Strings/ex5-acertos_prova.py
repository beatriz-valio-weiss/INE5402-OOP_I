gabarito = input()
respostas = input()
acertos = 0

for n in range(len(gabarito)):
    if gabarito[n] == respostas[n]:
        acertos += 1

print(acertos)