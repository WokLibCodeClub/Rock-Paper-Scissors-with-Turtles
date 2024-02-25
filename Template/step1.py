#!/bin/python3

from turtle import *
from random import randint
from time import sleep

#############################################
# VARIABLES
#############################################

screen = Screen()
screen.setup(450,400)
screen.bgcolor('lightcyan')

screen.register_shape('left_paper.gif')
screen.register_shape('left_rock.gif')
screen.register_shape('left_scissors.gif')
screen.register_shape('right_paper.gif')
screen.register_shape('right_rock.gif')
screen.register_shape('right_scissors.gif')
screen.register_shape('no.gif')
screen.register_shape('yes.gif')

player = Turtle()
computer = Turtle()

for t in screen.turtles():
  t.hideturtle()
  t.penup()
  t.speed(0)
  t.setheading(90)

player.shape('left_rock.gif')
player.goto(-70, 0)
player.showturtle()

computer.shape('right_scissors.gif')
computer.goto(70,0)
computer.showturtle()

#############################################
# FUNCTIONS
#############################################

#############################################
# MAIN CODE
#############################################

