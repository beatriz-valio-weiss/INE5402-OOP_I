# Importar Turtle
import turtle
r = turtle.Turtle()

# Parametro
raio = 100

# Circunferencia do Relogio
r.width(2)
r.begin_fill()
r.fillcolor('snow')
r.circle(raio)
r.end_fill()

# Posicionamento
r.up()
r.left(90)
r.fd(raio)

# Pontos do Relogio
for p in range(12):
    r.fd(4*raio/5)
    r.down()
    r.dot(4)
    r.up()
    r.bk(4*raio/5)
    r.right(30)
    

# Ponteiro minutos
r.width(2)
r.down()
r.color('black')
r.width(2)
r.right(80)
r.fd(8*raio/12)
r.up()
r.bk(8*raio/12)

# Ponteiro horas
r.down()
r.width(3)
r.right(220)
r.fd(6*raio/12)
r.up()
r.bk(6*raio/12)

# Ponteiro segundos
r.width(1)
r.down()
r.color('red')
r.right(50)
r.fd(9*raio/12)
r.up()
r.bk(9*raio/12)

# Fim
turtle.done()