# from turtle import Turtle, Screen  

# screen = Screen()
# screen.setup(width=600, height=500)
# screen.title("Trivia Game")
# screen.addshape("./trivia/3.gif")
# turtle = Turtle()
# turtle.shape("./trivia/3.gif")

# def screen_input(x, y):
#     print(x, y)

# screen.onclick(screen_input)

# t = Turtle()
# t.penup()
# t.goto(-74.0, -45.0)
# t.pendown()
# t.hideturtle()
# t.write(">Hello World\n>Colour pops\n>Sugar Candies", font=("Jua", 16, "normal"))


import turtle

# import pandas

# def n2():
#     t2.hideturtle()
#     screen1.addshape("./trivias/3.gif")
#     t1.shape("./trivias/3.gif")
#     t1.showturtle()
#     screen1.update()

# # Create one screen for the game
# screen1 = turtle.Screen()
# screen1.setup(width=1.0, height=1.0)    
# screen1.title("Trivia Game")
# screen1.tracer(0)
# # Load shapes
# screen1.addshape("./trivias/1.gif")
# screen1.addshape("button.gif")

# # Create turtles
# t1 = turtle.Turtle()
# t1.shape("./trivias/1.gif")
# t1.penup()


# t2 = turtle.Turtle()
# t2.shape("button.gif")
# t2.penup()

# screen1.update()

# # Function to handle button click
# def button_click(x, y):
#     print("Button clicked!")
#     # Call n2 function when clicking anywhere on the screen
#     n2()

# # Register click event on the entire screen to trigger n2
# t2.onclick(button_click)

# # Keep the window open
# screen1.mainloop()
import pandas as pd

data_dict = {"Artist Names": ["Dua Lipa", "Billie Eilish", "Harry Styles", "Olivia Rodrigo",  "The Weeknd", "Post Malone", "Doja Cat", "Lizzo", "SZA", "Lil Nas X"], 
             "Songs1":["Levitating", "Bad Guy", "As It Was", "Drivers License", "Blinding Lights", "Circles", "Say So", "Truth Hurts", "Kill Bill", "Old Town Road"],
             "Songs2": ["Don't Start Now", "Therefore I Am", "Adore You", "Good 4 U", "Can't Feel My Face", "Rockstar","Streets", "Good as Hell", "The Weekend", "Montero"], 
             "Songs3": ["New Rules", "When The Party's Over", "Watermelon Sugar",  "Deja Vu", "Starboy", "Sunflower", "Woman","About Damn Time","Good Days", "Industry Baby"]}

df = pd.DataFrame(data_dict)
df.to_csv("Artist_name.csv")