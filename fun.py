import turtle
from random import randint

myt = turtle.Turtle()

turtle.bgcolor("black")

turtle.title("fun")



n = 4

for i in range(1000):
    color = ['magenta', 'red', 'yellow' , 'green' , 'pink' , 'purple']

    myt.color(color[randint(0,5)])

    myt.forward(n)

    myt.left(80)

    n +=1
input()

