# Programa em Python para traçar Fibonacci
# fractal espiral usando Turtle
import turtle
import math


def fibo_plot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Mudando a cor do tracejado da caneta para azul
    x.pencolor("blue")

    # Desenhando o primeiro quadrado
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # Prosseguindo com a Sequência de Fibonacci
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Desenhando o resto dos quadrados
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        # Prosseguindo com a Sequência de Fibonacci
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Levando a caneta para o ponto inicial do espiral
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Mundando a cor do tracejado da caneta para vermelho
    x.pencolor("red")

    # Traço do espiral de Fibonacci
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b


# Aqui 'factor' significa o multiplicativo
# fator que expande ou encolhe a escala
# do traço por um certo fator.
factor = 1

# Adiquirindo o numero de
# interações que nosso algoritmo irá rodar
interacoes = int(input('Coloque o numero de interações (Precisa ser > 1): '))

# Criando uma tela
tela = turtle.Screen()

# Tracejando o fractal espiral de Fibonacci
# e dando print nos respectivos valores de Fibonacci
if interacoes > 0:
    print("Sequência de Fibonacci para", interacoes, "elementos :")
    x = turtle.Turtle()
    x.speed(100)
    fibo_plot(interacoes)
    turtle.done()
else:
    print("Numero de interações precisam ser > 0")
