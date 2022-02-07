from turtle import *


speed('fastest')

# rodando a seta para apontar para cima
rt(-90)

# o ângulo agudo entre
# a base e ramo do Y
angle = 30


# Função para traçar um Y
def y(tamanho, nivel):

    if nivel > 0:
        colormode(255)

        # dividindo a faixa rgb para verde
        # em intervalos iguais para cada nível
        # definindo a cor de acordo
        # para o nível atual
        pencolor(0, 255//nivel, 0)

        # Desenhando a base
        fd(tamanho)

        rt(angle)

        # chamada recursiva para
        # a sub-arvore da direita
        y(0.8 * tamanho, nivel-1)

        pencolor(0, 255//nivel, 0)

        lt(2 * angle)

        # chamada recursiva para
        # a subarvore da esquerda
        y(0.8 * tamanho, nivel-1)

        pencolor(0, 255//nivel, 0)

        rt(angle)
        fd(-tamanho)


# arvore do tamanho 80 e nivel 7
y(80, 7)
