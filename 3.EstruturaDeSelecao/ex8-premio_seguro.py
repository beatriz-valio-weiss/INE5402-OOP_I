# Calcular o prêmio (valor a ser pago pelo segurado) de um seguro de automóvel
valor_veiculo = float(input())
classe_desconto = input()
procedencia = input()
idade_segurado = int(input())

if procedencia == "nacional":
    premio = valor_veiculo * 10 / 100
elif procedencia == "estrangeira":
    premio = valor_veiculo * 15 / 100
else:
    print("erro")

if classe_desconto == "A":
    desconto = premio * 30 / 100
elif classe_desconto == "B":
    desconto = premio * 20 / 100
elif classe_desconto == "C":
    desconto = premio * 10 / 100
elif classe_desconto == "D":
    desconto = premio * 5 / 100
elif classe_desconto == "E":
    desconto = premio * 0
else:
    print("erro")
    
if idade_segurado > 24:
    outro_desconto = premio * 10 / 100
else:
    outro_desconto = premio * 0

valor_premio = premio - desconto - outro_desconto

print(valor_premio)