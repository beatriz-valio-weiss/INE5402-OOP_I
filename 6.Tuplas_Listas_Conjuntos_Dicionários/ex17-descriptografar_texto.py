alfabeto_normal = input()
alfabeto_cifragem = input()
mensagem_cifrada = input()

mensagem_normal = ''
mapeamento = dict()

for i in range(len(alfabeto_normal)):
    a_n = alfabeto_normal[i]
    a_c = alfabeto_cifragem[i]
    mapeamento[a_c] = a_n
for letra in mensagem_cifrada:
    if letra in mapeamento:
        mensagem_normal += mapeamento[letra]
    else:
        mensagem_normal += letra

print(mensagem_normal)