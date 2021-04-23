# Importar Turtle
import turtle

p=turtle.Turtle()
p.width(2)


# Definição de valores
x = 10

# Definir função desenho dos Olhos
def olhos(tart):
    "Desenho Pupila"
    tart.left(90)
    tart.color('black')
    tart.begin_fill()
    tart.fillcolor('black')
    tart.circle(x)
    tart.end_fill()
    "Desenho Contorno"
    tart.color('blue')
    tart.circle(2*x)
    tart.circle(3*x)
    tart.circle(4*x)

# Olhos
"Olho 1"
olhos(p)
"Olho 2"
p.right(-90)
olhos(p)

# Nariz
p.up()
p.fd(6*x)
p.down()
p.width(1)
p.color('magenta')

for n in range(60):
    p.fd(2*x)
    p.bk(2*x)
    p.right(6)
    
# Boca
p.up()
p.fd(3*x)
p.right(90)

    # Inicio do sorriso
p.fd(40)
p.down()
p.width(6)
p.color('red')
p.left(120)

for b in range(120):
    p.fd(x/12)
    p.left(1)

# Fim
turtle.done()