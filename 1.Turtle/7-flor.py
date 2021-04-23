# Importar Turtle
import turtle

# Definições
flor=turtle.Turtle()
flor.color('magenta')
flor.fillcolor('pink')

caule=turtle.Turtle()
caule.width(4)
caule.color('dark green')

folha=turtle.Turtle()
folha.width(2)
folha.color('dark green')

# Funções
'Definição da função de uma pétala'
def desenhar_petala(tart,tamanho,angulo):
    tart.circle(tamanho,angulo)
    tart.left(180-angulo)
    tart.circle(tamanho,angulo)
    tart.left(180-angulo)

'Definição da função de uma flor com várias pétalas'
def desenhar_petalas(tart,quantidade,tamanho,angulo):
    for p in range(quantidade):
        tart.begin_fill()
        desenhar_petala(tart,tamanho,angulo)
        tart.end_fill()
        tart.right(360/quantidade)

'Definição da função do caule com uma folha'
def desenhar_caule(tart,tamanho):
    tart.fd(tamanho)
def desenhar_folha(tart,tamanho,angulo):
    tart.circle(tamanho,angulo)
    tart.left(180-angulo)
    tart.circle(tamanho,angulo)
    tart.left(180-angulo)

# Desenhos
desenhar_petalas(flor,7,100,75)
flor.color('yellow')
flor.dot(25)

caule.right(90)
desenhar_caule(caule,300)

folha.up()
folha.right(90)
folha.fd(200)
folha.down()
folha.left(90)
folha.fillcolor('green')
folha.begin_fill()
desenhar_folha(folha,50,60)
folha.end_fill()
folha.left(30)
folha.fd(50)

# Fim
turtle.done()