#!/bin/python3

from turtle import *
from random import randint
from time import sleep

#############################################
# VARIABLES
#############################################

# set up screen
screen = Screen()
screen.setup(450,400)
screen.bgcolor('lightcyan')

# register images to be used for turtles
screen.register_shape('left_paper.gif')
screen.register_shape('left_rock.gif')
screen.register_shape('left_scissors.gif')
screen.register_shape('right_paper.gif')
screen.register_shape('right_rock.gif')
screen.register_shape('right_scissors.gif')
screen.register_shape('no.gif')
screen.register_shape('yes.gif')

#####################
# create turtles
#####################
# turtles for player and computer hands
player = Turtle()
computer = Turtle()

# turtles to choose RPS
choose_rock = Turtle()
choose_paper = Turtle()
choose_scissors = Turtle()

# turtles for yes/no
yes = Turtle()
no = Turtle()

# turtle for labelling
label = Turtle()

# turtle for scoring
scorer = Turtle()

# set common parameters for all turtles
for t in screen.turtles():
  t.hideturtle()
  t.penup()
  t.speed(0)
  t.setheading(90)
  
# lists
player_hands = ['left_rock.gif', 'left_paper.gif', 'left_scissors.gif']
computer_hands = ['right_rock.gif', 'right_paper.gif', 'right_scissors.gif']
results = ["It was a draw", "You won", "You lost"]

# global variables
player_choice = -1

player_score = 0
computer_score = 0

# set shapes for turtles
choose_rock.shape(player_hands[0])
choose_paper.shape(player_hands[1])
choose_scissors.shape(player_hands[2])

yes.shape('yes.gif')
no.shape('no.gif')

# set locations for turtles
choose_rock.goto(-120, 100)
choose_paper.goto(0, 100)
choose_scissors.goto(120, 100)

yes.goto(-50, 130)
no.goto(50, 130)

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

def click_yes(x,y):
  #print('Clicked y')
  yes.hideturtle()
  yes.onclick(None)
  no.hideturtle()
  no.onclick(None)
  make_choice()
  

def click_no(x,y):
  #print('Clicked n')
  screen.bye()
  exit()

def play_game():
  global player_score, computer_score
  # hide the three choose turtles
  choose_rock.hideturtle()
  choose_paper.hideturtle()
  choose_scissors.hideturtle()
  
  # cancel clicking for the choose turtles
  choose_rock.onclick(None)
  choose_paper.onclick(None)
  choose_scissors.onclick(None)
  
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
    label.write(n, font = ("arial", 48, 'bold'), align = "center")
    sleep(1)

  # annotate player and computer turtles
  label.clear()
  label.color('green')
  label.goto(-80, 50)
  label.write('You', font = ("arial", 18, 'normal'), align = "center")
  label.color('blue')
  label.goto(80, 50)
  label.write('Computer', font = ("arial", 18, 'normal'), align = "center")

  # show player and computer hands
  player.showturtle()
  computer.showturtle()
  
  # pause 1 second
  sleep(1)
  
  # work out who won and write result
  result = (player_choice - computer_choice) % 3
  label.goto(0, -80)
  label.color('red')
  label.write(results[result], font = ("arial", 22, 'bold'), align = "center")
  
  # update scores
  if result == 1:
    player_score += 1
  if result == 2:
    computer_score += 1
  show_scores()
  
  # wait a couple of seconds
  sleep(2)
  
  # call play_again function
  play_again()
  
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

def play_again():
  # clear the screen
  label.clear()
  player.hideturtle()
  computer.hideturtle()
  
  # display yes and no turtles with label, and set for clicking
  label.color('black')
  label.goto(-210, 160)
  label.write('Play again? (click y or n)', font = ("arial", 14, 'bold'), align = "left")
  yes.showturtle()
  no.showturtle()
  yes.onclick(click_yes)
  no.onclick(click_no)
  
def show_scores():
  scorer.clear()
  scorer.goto(-140,-115)
  scorer.write("Score:", align = "left", font = ("arial", 18, "bold"))
  scorer.goto(-80,-140)
  scorer.write("You", align = "center", font = ("arial", 14, "normal"))
  scorer.goto(80,-140)
  scorer.write("Computer", align = "center", font = ("arial", 14, "normal"))
  scorer.goto(-70,-165)
  scorer.write(player_score, align = "right", font = ("arial", 14, "normal"))
  scorer.goto(90,-165)
  scorer.write(computer_score, align = "right", font = ("arial", 14, "normal"))

#############################################
# MAIN CODE
#############################################

show_scores()
make_choice()
