# Importar Turtle
import turtle
estrela = turtle.Turtle()

# Posicionamento e Distancia
d = 50
estrela.left(72)

# Colorir
estrela.color('gold')
estrela.begin_fill()
estrela.fillcolor('yellow')

# Estrela
for e in range(5):
    estrela.fd(d)
    estrela.right(72)
    estrela.fd(d)
    estrela.left(144)
    
estrela.end_fill()

# Fim
turtle.done()