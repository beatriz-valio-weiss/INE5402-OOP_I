escala_inicial = input()
temperatura = float(input())
escala_final = input()

# conversão de c para ...
if escala_inicial == "c" and escala_final == "f":
    conversao = temperatura * 1.8 + 32
elif escala_inicial == "c" and escala_final == "k":
    conversao = temperatura + 273.15
elif escala_inicial == "c" and escala_final == "r":
    conversao = temperatura * 9 / 5 + 491.67
# conversão de f para ...
elif escala_inicial == "f" and escala_final == "c":
    conversao = (temperatura - 32) / 1.8 
elif escala_inicial == "f" and escala_final == "k":
    conversao = (temperatura - 32) * 5 / 9 + 273.15
elif escala_inicial == "f" and escala_final == "r":
    conversao = temperatura + 459.67
# conversão de k para ...
elif escala_inicial == "k" and escala_final == "c":
    conversao = temperatura - 273.15
elif escala_inicial == "k" and escala_final == "f":
    conversao = (temperatura - 273.15) * 1.8 + 32
elif escala_inicial == "k" and escala_final == "r":
    conversao = temperatura * 1.8
# conversão de r para ...
elif escala_inicial == "r" and escala_final == "c":
    conversao = (temperatura - 491.67) * 5 / 9 
elif escala_inicial == "r" and escala_final == "f":
    conversao = temperatura - 459.67
elif escala_inicial == "r" and escala_final == "k":
    conversao = temperatura * 5 / 9

print(conversao)