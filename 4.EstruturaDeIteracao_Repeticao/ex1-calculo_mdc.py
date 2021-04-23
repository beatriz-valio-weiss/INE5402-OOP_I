numero_1 = int(input())
numero_2 = int(input())

a = numero_1
b = numero_2

while b > 0:
    resto = a % b;
    a = b
    b = resto    
mdc = a

print(mdc)