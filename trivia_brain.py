from turtle import Turtle, Screen
import pandas as pd

class TriviaBrain:
    def __init__(self):
        pass

    def welcome(self):
        #set mainscreen
        self.main_screen = Screen()
        self.main_screen.setup(width=1.0, height=1.0)
        self.main_screen.title("Trivia Game")
        self.main_screen.tracer(0)
        #set shapes
        self.main_screen.addshape("./trivias/1.gif")
        self.main_screen.addshape("button.gif")

        self.t1 = Turtle() #first turlte for screen object
        self.t1.shape("./trivias/1.gif")
        self.t1.penup()

        self.t2 = Turtle() #second for button object
        self.t2.shape("button.gif")
        self.t2.penup()
        self.t2.goto(-7, -122.0)

        self.t3 = Turtle() #third turtle for writing
        self.t3.hideturtle()
        self.t3.penup()

        self.main_screen.update()


    def instructions(self):
        self.main_screen.addshape("./trivias/2.gif")
        self.t1.shape("./trivias/2.gif")
        self.t2.goto(400, -178)
        self.main_screen.update()

    def trivia_game(self):
        self.main_screen.addshape("./trivias/3.gif")
        self.t1.shape("./trivias/3.gif")
        

        
        
        
        