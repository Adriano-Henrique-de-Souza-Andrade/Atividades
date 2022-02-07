import turtle

# metodo Screen() para obter uma tela
tela = turtle.Screen()

# criando objeto seta
seta = turtle.Turtle()


def triangle(x, y):
    # isso é utilizado para não utilizar a caneta (evitar fazer linhas)
    seta.penup()
    # Isso é utilizado para mover o cursor para a posição x e y
    seta.goto(x, y)
    # isso é utilizado para não utilizar a caneta (e fazer as linhas)
    seta.pendown()

    for i in range(3):

        # mover o cursor 100 unidades
        # para frente
        seta.forward(100)

        # rodar 120 graus à esquerda
        seta.left(120)

        # mover o cursor novamente 100 unidades
        # para frente
        seta.forward(100)

# função built in especial para enviar a atual


# posição do cursor para o triangulo
turtle.onscreenclick(triangle, 1)

turtle.listen()

# manter a tela 
turtle.done()
