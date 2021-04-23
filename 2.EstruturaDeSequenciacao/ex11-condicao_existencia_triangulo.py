# Vertice v
v_a = float(input())
v_b = float(input())
v_c = float(input())

# Condição de existência de um triângulo

triangulo = abs(v_b - v_c) < v_a < v_b + v_c

print(triangulo)