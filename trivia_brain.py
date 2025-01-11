from turtle import Turtle, Screen
import pandas as pd

class TriviaBrain:
    def __init__(self):
        main_screen = Screen()
        main_screen.setup(width=1.0, height=1.0)
        t1 = Turtle() #first turlte for screen object
        t1.penup()
        t2 = Turtle() #second for button object
        t2.penup()
        main_screen.tracer(0)

        main_screen.mainloop()

    def welcome():
        main