import pandas as pd
from trivia_brain import TriviaBrain


def click_instruction(x, y): #setting button function
    print("clicked on instruction")
    trivia.instructions()

def click_trivia(x, y):
    print("Clicked on Trivia")

#setting object for screen
trivia = TriviaBrain()

trivia.welcome() #calling welcome screen function

trivia.t2.onclick(click_instruction) #registering button function


#setting up pandas

trivia.main_screen.mainloop()