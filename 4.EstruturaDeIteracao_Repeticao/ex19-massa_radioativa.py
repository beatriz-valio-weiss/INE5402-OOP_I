massa = float(input())
segundos = 0

while massa >= 0.5:
    massa -= massa / 2
    segundos += 50
    
print(segundos)