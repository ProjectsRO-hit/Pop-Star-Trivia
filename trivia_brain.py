from turtle import Turtle, Screen
import pandas as pd

class TriviaBrain:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1.0, height=1.0)
        self.screen.title("Trivia Game")
        self.image = ["./trivias/1.gif", "./trivias/2.gif", "./trivias/3.gif", "./trivias/4.gif", "./trivias/5.gif"]
        self.t1 = Turtle()
        self.questions_count = 0
        self.screen.tracer(0)
    
    def welcome(self):
        self.screen.addshape(self.image[0])
        self.t1.shape(self.image[0]) 
        self.screen.update()
        self.continue_game = self.screen.textinput("Welcome to Trivia Game", "Do you want to play the game? Type 'yes' to continue else 'no' to exit")
        if self.continue_game.lower() == "yes":
            self.instructions()
        else:
            self.screen.bye()
            exit()

    def instructions(self):
        pass
    
    def trivia(self):
        pass