from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/jkreddy/projects/PythonProjects/PycharmProjects/Snake Game/high_score_data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score = {self.score} High Score = {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/jkreddy/projects/PythonProjects/PycharmProjects/Snake Game/high_score_data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 28, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
