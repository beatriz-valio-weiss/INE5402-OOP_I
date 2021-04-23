qtd_valores = int(input())

soma_valores = 0

for quantidade in range(qtd_valores):
    soma_valores += float(input())

media = soma_valores / qtd_valores

print(media)