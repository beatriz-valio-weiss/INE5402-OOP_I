# Importar turtle
import turtle

l=turtle.Turtle()
l.color('orange')
l.fillcolor('orange')

# Valor
x=50
l.left(45)

# Laranjas
for pilha in range(1,7,1):
    for laranja in range(pilha):
        l.dot(x)
        l.up()
        l.fd(x)
    # Reposicionamento
    l.right(45)
    l.fd(x)
    l.right(135)
    l.down()
    
