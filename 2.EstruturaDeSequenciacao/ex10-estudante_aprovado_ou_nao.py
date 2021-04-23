# Notas
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

# Pesos
peso1 = int(input())
peso2 = int(input())
peso3 = int(input())

# Média
media = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)

aprovacao = media >= 6
print(aprovacao)