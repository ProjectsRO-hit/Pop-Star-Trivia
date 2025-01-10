from turtle import Turtle, Screen
import pandas as pd

class TriviaBrain:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=500)
        self.screen.title("Trivia Game")
        self.image = ["./trivia/1.gif", "./trivia/2.gif", "./trivia/3.gif", "./trivia/4.gif", "./trivia/5.gif"]
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.questions_count = 0
    
    def welcome(self):
        self.screen.addshape(self.image[0])
        self.turtle.shape(self.image[0])
        self.turtle.showturtle()  
        self.continue_game = self.screen.textinput("Welcome to Trivia Game", "Do you want to play the game? Type 'yes' to continue else 'no' to exit")
        if self.continue_game.lower() == "yes":
            self.turtle.hideturtle()
            self.instructions()
        else:
            self.screen.bye()
            exit()

    def instructions(self):
        self.screen.addshape(self.image[1])
        self.turtle.shape(self.image[1])
        self.turtle.showturtle()  # Ensure showturtle() is called properly
        self.continue_game = self.screen.textinput("Instructions", "Did you read the instructions? Type 'yes' to continue else 'no' to exit")
        if self.continue_game.lower() == "yes":
            pass
        else:
            self.screen.bye()
            exit()
    
    def trivia(self):
        self.screen.addshape(self.image[2])
        self.turtle.shape(self.image[2])
        self.turtle.showturtle()  # Ensure showturtle() is called properly