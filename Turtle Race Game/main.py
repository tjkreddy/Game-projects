from turtle import Turtle, Screen
import random
race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? and"
                                                          " enter the color of the turtle?")
colors = ["red", "orange", "CornflowerBlue", "green", "blue", "purple"]
list_of_turtles = []
i = 30
for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=-230, y=-100+i)
    tim.pendown()
    list_of_turtles.append(tim)
    i = i+30
if user_bet:
    race_is_on = True
while race_is_on:
    for tim in list_of_turtles:
        if tim.xcor() > 230:
            win_color = tim.pencolor()
            if win_color == user_bet:
                print(f"you've won! The {win_color} turtle is the winner")
            else:
                print(f"you've lost! The {win_color} turtle is the winner")
            race_is_on = False
        move_num = random.randint(0, 10)
        tim.forward(move_num)


screen.exitonclick()
