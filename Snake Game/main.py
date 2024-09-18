from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
game_is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() >
            280 or snake.segments[0].ycor() < -280):
        scoreboard.reset()
        snake.reset()

    for i in range(2, len(snake.segments)):
        if snake.segments[0].distance(snake.segments[i]) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
