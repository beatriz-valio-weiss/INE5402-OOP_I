valor_veiculo = float(input())
sexo = input()
idade = int(input())

premio_seguro = valor_veiculo * 10 / 100

if sexo == "M" and idade <= 24:
    desconto = premio_seguro * 0
elif sexo == "M" and idade <= 33:
    desconto = premio_seguro * 10 / 100
elif sexo == "M" and idade > 33:
    desconto = premio_seguro * 20 / 100
elif sexo == "F" and idade <= 24:
    desconto = premio_seguro * 5 / 100
elif sexo == "F" and idade <= 33:
    desconto = premio_seguro * 20 / 100
elif sexo == "F" and idade > 33:
    desconto = premio_seguro * 35 / 100
    
valor_seguro = premio_seguro - desconto

print(valor_seguro)