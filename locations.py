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


# screen.mainloop()

from turtle import Screen, Turtle

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

def draw_onclick(x, y):
    turtle.dot(100, 'cyan')

button = Turtle()
button.hideturtle()
button.shape('circle')
button.fillcolor('red')
button.penup()
button.goto(150, 150)
button.write("Click me!", align='center', font=FONT)
button.sety(150 + CURSOR_SIZE + FONT_SIZE)
button.onclick(draw_onclick)
button.showturtle()

turtle = Turtle()
turtle.hideturtle()

screen = Screen()
screen.mainloop()