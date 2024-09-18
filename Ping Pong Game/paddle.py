from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def moveup(self):
        new_ycor = self.ycor()+20
        self.goto(self.xcor(), new_ycor)

    def movedown(self):
        new_ycor = self.ycor()-20
        self.goto(self.xcor(), new_ycor)




