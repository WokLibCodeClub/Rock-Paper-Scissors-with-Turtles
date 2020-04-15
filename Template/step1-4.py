from turtle import *
from random import randint
from time import sleep
from sys import exit

#############################################
# VARIABLES
#############################################

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
background = Turtle()
referee = Turtle()

for i in screen.turtles():
    i.hideturtle()
    i.penup()
    i.speed(0)

you.goto(-150, 20)
computer.goto(150, 20)

you_hands = ["you_rock.gif", "you_paper.gif", "you_scissors.gif"]
computer_hands = ["computer_rock.gif", "computer_paper.gif", "computer_scissors.gif"]

your_choice = -1

#############################################
# FUNCTIONS
#############################################

def get_choice():
    global your_choice
    rps = "x"
    
    while rps =="x":
        rps = screen.textinput("Your choice!", "rock (r), paper (p) or scissors (s)? ")    
        if rps == "r":
            your_choice = 0
        elif rps == "p":
            your_choice = 1
        elif rps == "s":
            your_choice = 2
        else:
            rps = "x"

    play_game()

def play_game():
    computer_choice = randint(0, 2)

    for i in [3, 2, 1]:
        referee.color("red")
        referee.write(i, font = ("arial", 100, "bold"), align = "center")
        sleep(1)
        referee.clear()
        
    you.shape(you_hands[your_choice])
    computer.shape(computer_hands[computer_choice])
    you.showturtle()
    computer.showturtle()
    play_again()

def draw_field():
    background.goto(-150, 100)
    background.color("green")
    background.write("You", font = ("arial", 24, "italic"), align = "center")
    background.goto(150, 100)
    background.color("blue")
    background.write("Computer", font = ("arial", 24, "italic"), align = "center")

def play_again():
    choice = "x"
    while choice == "x":
        choice = screen.textinput("Play again?", "yes (y) or no (n)? ")
        if choice == "y":
            you.hideturtle()
            computer.hideturtle()
            get_choice()
        elif choice == "n":
            screen.bye()
            exit()
        else:
            choice = "x"        

#############################################
# MAIN CODE
#############################################

draw_field()
get_choice()

