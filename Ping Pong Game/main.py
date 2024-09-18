from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)
positions = [(0, 55), (0, 135), (0, 215), (0, 295), (0, -55), (0, -135), (0, -215), (0, -295)]
for position in positions:
    line = Turtle()
    line.penup()
    line.shape("square")
    line.shapesize(2.5, 0.5)
    line.color("white")
    line.goto(position)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(r_paddle.moveup, "Up")
screen.onkey(r_paddle.movedown, "Down")

screen.onkey(l_paddle.moveup, "w")
screen.onkey(l_paddle.movedown, "s")

game_is_on = True

speed = 0.05

while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        speed -= 0.001

    if ball.xcor() > 380:
        ball.new_start()
        scoreboard.l_score += 1
        scoreboard.update_score()

    if ball.xcor() < -380:
        ball.new_start()
        scoreboard.r_score += 1
        scoreboard.update_score()
screen.exitonclick()
