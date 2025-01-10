from turtle import Turtle, Screen  

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

# import turtle

# # Setup the turtle screen
# screen = turtle.Screen()
# screen.title("Interactive Button with GIF")
# screen.setup(width=400, height=400)

# # Load the GIF image
# gif_file = "button.gif"  # Ensure this file is in your working directory or provide full path
# screen.addshape(gif_file)

# # Create a turtle for the button
# button = turtle.Turtle()
# button.shape(gif_file)
# button.penup()
# button.goto(0, 0)  # Position the button at the center of the screen

# # Button state
# button_state = 'up'

# def change_button_state(x, y):
#     global button_state
#     # Check if click is on button
#     if button.distance(x, y) < 50:  # Assuming button size; adjust if needed
#         if button_state == 'up':
#             button_state = 'down'
#             # Here, you'd typically change the GIF if you have one for pressed state
#             # For simplicity, we'll just rotate the button slightly to show interaction
#             button.right(5)
#         else:
#             button_state = 'up'
#             button.left(5)

# # Bind click event to the screen
# screen.onclick(change_button_state)

# # Keep the window open
# screen.mainloop()

screen1 = Screen()
screen1.setup(width=600, height=500)    
screen1.title("Trivia Game")
screen1.addshape("./trivia/1.gif")
t1 = Turtle()
t1.shape("./trivia/1.gif")
t1.penup()
screen2 = Screen()
screen2.addshape("button.gif")
t2 = Turtle()
t2.shape("button.gif")
t2.penup()


screen1.mainloop()