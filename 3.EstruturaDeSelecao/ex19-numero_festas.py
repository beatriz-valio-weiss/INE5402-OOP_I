dia_aniversariante1 = int(input())
dia_aniversariante2 = int(input())
dia_aniversariante3 = int(input())

if dia_aniversariante1 != dia_aniversariante2 and dia_aniversariante1 != dia_aniversariante3 and dia_aniversariante2 != dia_aniversariante3:
    numero_de_festas = 3
elif dia_aniversariante1 != dia_aniversariante2 or dia_aniversariante1 != dia_aniversariante3 or dia_aniversariante3 != dia_aniversariante2:
    numero_de_festas = 2
else:
    numero_de_festas = 1
    
print(numero_de_festas)