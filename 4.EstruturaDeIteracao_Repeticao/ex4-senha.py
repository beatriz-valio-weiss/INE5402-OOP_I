# Valor da senha fixa
senha = 2002

# Tentativas de senhas
tentativa_senha = int(input())

while tentativa_senha != senha:
    print ("Senha Invalida")
    tentativa_senha = int(input())

print("Acesso Permitido")