# Importar Turtle
import turtle

espiral = turtle.Turtle()

# Espiral

for distancia in range(30,150,1):
    espiral.fd(distancia)
    espiral.right(93)
    
# Fim
turtle.done()