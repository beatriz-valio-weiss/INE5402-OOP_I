x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Possibilidade de movimento do cavalo no xadrez
if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
    movimento = True
elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
    movimento = True
else:
    movimento = False

print(movimento)