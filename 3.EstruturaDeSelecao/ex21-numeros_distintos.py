n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if n1 != n2 and n1 != n3 and n1 != n4 and n2 != n3 and n2 != n4 and n3 != n4:
    numeros_distintos = 4
elif n1 == n2 == n3 == n4:
    numeros_distintos = 1
elif n1 == n2 == n3 != n4 or n1 == n2 == n4 != n3 or n4 == n2 == n3 != n1 or n4 == n1 == n3 != n2 or (n1 == n2 and n3 == n4) or (n1 == n3 and n2 == n4) or (n1 == n4 and n2 == n3):
    numeros_distintos = 2
else:
    numeros_distintos = 3
    
print(numeros_distintos)