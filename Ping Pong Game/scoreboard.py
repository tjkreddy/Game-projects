from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-125, 200)
        self.write(f"{self.l_score}", font=("Arial", 75, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", font=("Arial", 75, "normal"))



