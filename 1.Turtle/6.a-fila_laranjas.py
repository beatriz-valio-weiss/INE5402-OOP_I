# Importar turtle
import turtle
l=turtle.Turtle()

# Definições
l.up()
l.goto(-300,0)
l.down()
x=10
l.color('orange')

# Fila de laranjas
for fila in range (1,9,1):
    l.begin_fill()
    l.circle(fila*x)
    l.end_fill()
    l.up()
    l.fd(((fila+fila)+1)*x)
    l.down()
    
# Fim
turtle.done()