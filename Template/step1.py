from turtle import *
from random import randint
from time import sleep
from sys import exit

screen = Screen()
setup(800,700)

screen.register_shape("computer_rock.gif")
screen.register_shape("computer_paper.gif")
screen.register_shape("computer_scissors.gif")
screen.register_shape("you_rock.gif")
screen.register_shape("you_paper.gif")
screen.register_shape("you_scissors.gif")

you = Turtle()
computer = Turtle()

for i in screen.turtles():
    i.hideturtle()
    i.penup()
    i.speed(0)

you.shape("you_rock.gif")
you.goto(-150, 20)
you.showturtle()

computer.shape("computer_scissors.gif")
computer.goto(150, 20)
computer.showturtle()


