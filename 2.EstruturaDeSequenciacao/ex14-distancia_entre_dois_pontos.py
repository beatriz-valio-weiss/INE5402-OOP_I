import math

# Distancia entre p1 e p2
x1, y1 = [float(p1) for p1 in input().split()]
x2, y2 = [float(p2) for p2 in input().split()]

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("{:.4f}".format(d))