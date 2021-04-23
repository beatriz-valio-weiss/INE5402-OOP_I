numero = int(input())

contagem_maria = 0
lista = 0

for n in range (numero):
    nome = input()
    lista = sorted(nome.split())
    contagem_maria += lista.count('Maria')

print(contagem_maria)