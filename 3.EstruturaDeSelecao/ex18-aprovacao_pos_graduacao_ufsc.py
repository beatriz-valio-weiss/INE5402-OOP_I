def equivalente_num(conceito):
    if conceito == "A":
        return 4
    elif conceito == "B":
        return 3
    elif conceito == "C":
        return 2
    elif conceito == "E":
        return 0

conceito_1 = input()
conceito_2 = input()
conceito_3 = input()
conceito_4 = input()

ia = ((equivalente_num(conceito_1)) + (equivalente_num(conceito_2)) + (equivalente_num(conceito_3)) + (equivalente_num(conceito_4))) / 4

if conceito_1 != "E" and conceito_2 != "E" and conceito_3 != "E" and conceito_4 != "E" and ia >= 3:
    aprovacao = True
else:
    aprovacao = False

print(aprovacao)