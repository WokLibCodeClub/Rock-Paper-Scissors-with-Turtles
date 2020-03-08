from turtle import *
from random import randint
from time import sleep
from sys import exit

#######################################################################
# SETUP SCREEN
#######################################################################
screen = Screen()
setup(800,700)

#######################################################################
# register images
#######################################################################
screen.register_shape("computer_paper.gif")
screen.register_shape("computer_rock.gif")
screen.register_shape("computer_scissors.gif")
screen.register_shape("you_paper.gif")
screen.register_shape("you_rock.gif")
screen.register_shape("you_scissors.gif")

#######################################################################
# make lists for image files
#######################################################################
computer_hands = ["computer_rock.gif", "computer_paper.gif", "computer_scissors.gif"]
you_hands = ["you_rock.gif", "you_paper.gif", "you_scissors.gif"]

#######################################################################
# make Turtles
#######################################################################
you = Turtle()
you.hideturtle()
you.penup()
you.goto(-150, 20)
computer = Turtle()
computer.hideturtle()
computer.penup()
computer.goto(150, 20)
referee = Turtle()
referee.hideturtle()
referee.penup()
scorer = Turtle()
scorer.hideturtle()
scorer.penup()
background = Turtle()
background.hideturtle()
background.penup()

#######################################################################
# list for results
#######################################################################
results = ["It was a draw.", "You won! (-:", "You lost.. )-:"]

#######################################################################
# set scores to zero
#######################################################################
you_score = 0
computer_score = 0


#######################################################################
# DEFINE FUNCTION TO DRAW BACKGROUND
#######################################################################
def draw_field():
    background.goto(-150, 120)
    background.color("green")
    background.write("You",
                  align = "center", font = ('arial', 24, "italic"))
    background.goto(150, 120)
    background.color("blue")
    background.write("Computer",
                  align = "center", font = ('arial', 24, "italic"))
    background.goto(-300, -220)
    background.color("black")
    background.write("Score",
                  align = "left", font = ('arial', 32, "normal"))
    background.goto(-220, -270)
    background.write("You",
                  align = "left", font = ('arial', 28, "normal"))
    background.goto(-220, -320)
    background.write("Computer",
                  align = "left", font = ('arial', 28, "normal"))

#######################################################################
# DEFINE FUNCTION TO UPDATE THE SCORE
#######################################################################
def update_score():
    scorer.clear()
    scorer.goto(160, -270)
    scorer.write(you_score,
                  align = "right", font = ('arial', 28, "normal"))
    scorer.goto(160, -320)
    scorer.write(computer_score,
                  align = "right", font = ('arial', 28, "normal"))

#######################################################################
# DEFINE FUNCTION TO PLAY THE GAME
#######################################################################
def play_game():
    global you_score, computer_score
    # get your choice and convert to numeric value
    rps = "x"
    while rps == "x":
        rps = screen.textinput("Your choice!", "rock (r), paper (p) or scissors (s)? ")
        if rps == "r":
            your_choice = 0
        elif rps == "p":
            your_choice = 1
        elif rps == "s":
            your_choice = 2
        else:
            rps = "x"

    # referee starts game
    referee.color("black")
    referee.goto(0, -60)
    referee.write("Ready?", align = "center", font = ('arial', 60, "bold"))
    sleep(1.2)
    
    for i in [3, 2, 1]:
        referee.clear()
        referee.color("red")
        referee.write(i, align = "center", font = ('arial', 100, "bold"))
        sleep(1)
    
    referee.clear()

    # assign images, with computer random choice

    computer_choice = randint(0, 2)
    you.shape(you_hands[your_choice])
    computer.shape(computer_hands[computer_choice])
    you.showturtle()
    computer.showturtle()

    # write result to screen
    sleep(1)
    referee.color("black")
    referee.goto(0, -150)
    referee.write(results[(your_choice - computer_choice)%3],
                  align = "center", font = ('arial', 40, "bold"))

    you_score = you_score + ((your_choice - computer_choice)%3)%2
    #print(computer_score)
    computer_score = computer_score + int(((your_choice - computer_choice)%3)/2)
    #print("new computer score", computer_score)
    update_score()
    sleep(2)

    # play again question?
    play_again()
    
#######################################################################
# DEFINE FUNCTION TO ASK TO PLAY AGAIN
#######################################################################
def play_again():
    referee.clear()
    choice = "x"
    while choice == "x":
        choice = screen.textinput("Play again?", "Yes (y) or No (n)? ")
        if choice == "y":
            you.hideturtle()
            computer.hideturtle()
            play_game()
        elif choice == "n":
            screen.bye()
            exit()
        else:
            choice = "x"

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MAIN PROGRAMME LOOP
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
draw_field()
update_score()
play_game()




