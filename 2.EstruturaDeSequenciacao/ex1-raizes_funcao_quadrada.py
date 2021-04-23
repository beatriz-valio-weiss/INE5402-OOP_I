import math

print("Cálculo das raízes reais de uma função quadrática!")

# Valores
a = int(input(" Qual o valor de a? "))
b = int(input(" Qual o valor de b? "))
c = int(input(" Qual o valor de c? "))

# Calculo
delta = (b**2)-(4*a*c)
x1 = ((-b + math.sqrt(delta) )/(2*a))
x2 = ((-b - math.sqrt(delta) )/(2*a))

# Resultado
print("As raízes da função são ", x1, "e ", x2)