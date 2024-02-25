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

# turtle for labelling
label = Turtle()

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

player.goto(-70, 0)
computer.goto(70,0)

#############################################
# FUNCTIONS
#############################################

def click_rock(x,y):
  global player_choice
  player_choice = 0
  play_game()
  
def click_paper(x,y):
  global player_choice
  player_choice = 1
  play_game()

def click_scissors(x,y):
  global player_choice
  player_choice = 2
  play_game()

def play_game():
  # hide the three choose turtles
  choose_rock.hideturtle()
  choose_paper.hideturtle()
  choose_scissors.hideturtle()
  
  # cancel clicking for the choose turtles
  choose_rock.onclick(click_rock)
  choose_paper.onclick(click_paper)
  choose_scissors.onclick(click_scissors)
  
  # set value for computer choice
  computer_choice = randint(0,2)
  
  # set costumes for player and computer
  player.shape(player_hands[player_choice])
  computer.shape(computer_hands[computer_choice])
  
  # Write 3,2,1 in middle of screen
  for n in range(3, 0, -1):
    label.clear()
    label.color('red')
    label.goto(0,0)
    label.write(str(n), font = ("arial", 48, 'bold'), align = "center")
    sleep(1)

  # annotate the player and computer turtles
  label.clear()
  label.color('green')
  label.goto(-80, 50)
  label.write('You', font = ("arial", 18, 'normal'), align = "center")
  label.color('blue')
  label.goto(80, 50)
  label.write('Computer', font = ("arial", 18, 'normal'), align = "center")

  # show player and computer
  player.showturtle()
  computer.showturtle()
  
def make_choice():
  # set onclick functions for the choose turtles
  choose_rock.onclick(click_rock)
  choose_paper.onclick(click_paper)
  choose_scissors.onclick(click_scissors)
  
  # show the choose turtles
  choose_rock.showturtle()
  choose_paper.showturtle()
  choose_scissors.showturtle()
  
  # write Click on shape
  label.clear()
  label.color('black')
  label.goto(-210, 160)
  label.write('Click shape to choose rock, paper or scissors', font = ("arial", 14, 'bold'), align = "left")


#############################################
# MAIN CODE
#############################################

make_choice()

