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
screen.register_shape("yes.gif")
screen.register_shape("no.gif")

you = Turtle()
computer = Turtle()
background = Turtle()
referee = Turtle()
scorer = Turtle()
choose_rock = Turtle()
choose_paper = Turtle()
choose_scissors = Turtle()
choose_yes = Turtle()
choose_no = Turtle()

for i in screen.turtles():
    i.hideturtle()
    i.penup()
    i.speed(0)

you.goto(-150, 20)
computer.goto(150, 20)

you_hands = ["you_rock.gif", "you_paper.gif", "you_scissors.gif"]
computer_hands = ["computer_rock.gif", "computer_paper.gif", "computer_scissors.gif"]
outcomes = ["It was a draw", "You won", "You lost"]

your_choice = -1
your_score = 0
computer_score = 0

choose_rock.shape("you_rock.gif")
choose_paper.shape("you_paper.gif")
choose_scissors.shape("you_scissors.gif")
choose_yes.shape("yes.gif")
choose_no.shape("no.gif")

#############################################
# FUNCTIONS
#############################################

def get_choice():
    referee.goto(-350, 300)
    referee.write("Click on rock, paper or scissors:", font = ("arial", 28, 'bold'), align = "left")  
    choose_rock.goto(-200, 220)
    choose_rock.showturtle()
    choose_paper.goto(-10,220)
    choose_paper.showturtle()
    choose_scissors.goto(210, 220)
    choose_scissors.showturtle()
    choose_rock.onclick(rock_click)
    choose_paper.onclick(paper_click)
    choose_scissors.onclick(scissors_click)

def play_game():
    global your_score, computer_score
    choose_rock.hideturtle()
    choose_rock.onclick(None)
    choose_paper.hideturtle()
    choose_paper.onclick(None)
    choose_scissors.hideturtle()
    choose_scissors.onclick(None)
    referee.clear()
    
    computer_choice = randint(0, 2)

    referee.goto(0,0)
    for i in [3, 2, 1]:
        referee.color("red")
        referee.write(i, font = ("arial", 100, "bold"), align = "center")
        sleep(1)
        referee.clear()
        
    you.shape(you_hands[your_choice])
    computer.shape(computer_hands[computer_choice])
    you.showturtle()
    computer.showturtle()
    
    result = (your_choice - computer_choice) % 3
    sleep(1)
    referee.goto(0,-150)
    referee.write(outcomes[result], font = ("arial", 40, "bold"), align = "center")

    if result == 1:
        your_score += 1
    elif result == 2:
        computer_score += 1
    
    update_score()
    play_again()

def draw_field():
    background.goto(-150, 100)
    background.color("green")
    background.write("You", font = ("arial", 24, "italic"), align = "center")
    background.goto(150, 100)
    background.color("blue")
    background.write("Computer", font = ("arial", 24, "italic"), align = "center")

    background.goto(-300, -220)
    background.color("black")
    background.write("Score", align = "left", font = ("arial", 32, "normal"))
    background.goto(-220, -270)
    background.write("You", align = "left", font = ("arial", 28, "normal"))
    background.goto(-220, -320)
    background.write("Computer", align = "left", font = ("arial", 28, "normal"))    

def play_again():
    choice = "x"
    while choice == "x":
        choice = screen.textinput("Play again?", "yes (y) or no (n)? ")
        if choice == "y":
            you.hideturtle()
            computer.hideturtle()
            referee.clear()
            get_choice()
        elif choice == "n":
            screen.bye()
            exit()
        else:
            choice = "x"

def update_score():
    scorer.clear()
    scorer.goto(160, -270)
    scorer.write(your_score, align = "right", font = ("arial", 28, "normal"))
    scorer.goto(160, -320)
    scorer.write(computer_score, align = "right", font = ("arial", 28, "normal"))    

def rock_click(x,y):
    global your_choice
    your_choice = 0
    play_game()
    
def paper_click(x,y):
    global your_choice
    your_choice = 1
    play_game()

def scissors_click(x,y):
    global your_choice
    your_choice = 2
    play_game()

#############################################
# MAIN CODE
#############################################

draw_field()
update_score()
get_choice()

