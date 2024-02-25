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

# turtles to choose RPS
choose_rock = Turtle()
choose_paper = Turtle()
choose_scissors = Turtle()

for t in screen.turtles():
  t.hideturtle()
  t.penup()
  t.speed(0)
  t.setheading(90)
  
player_hands = ['left_rock.gif', 'left_paper.gif', 'left_scissors.gif']
computer_hands = ['right_rock.gif', 'right_paper.gif', 'right_scissors.gif']

player_choice = -1

choose_rock.shape(player_hands[0])
choose_paper.shape(player_hands[1])
choose_scissors.shape(player_hands[2])

choose_rock.goto(-120, 100)
choose_paper.goto(0, 100)
choose_scissors.goto(120, 100)

choose_rock.showturtle()
choose_paper.showturtle()
choose_scissors.showturtle()

player.goto(-70, 0)
computer.goto(70,0)

#############################################
# FUNCTIONS
#############################################

def click_rock(x,y):
  global player_choice
  player_choice = 0
  print(player_choice)
  
def click_paper(x,y):
  global player_choice
  player_choice = 1
  print(player_choice)

def click_scissors(x,y):
  global player_choice
  player_choice = 2
  print(player_choice)

#############################################
# MAIN CODE
#############################################

choose_rock.onclick(click_rock)
choose_paper.onclick(click_paper)
choose_scissors.onclick(click_scissors)

