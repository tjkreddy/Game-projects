from turtle import Turtle, Screen
import pandas
tim = Turtle()
tim.hideturtle()
screen = Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []
count = 0
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{count}/50 States", prompt="Enter the name of the State").title()
    if answer != "Exit":
        if answer in states_list:
            tim.penup()
            answer_ = data[data.state == answer]
            print(answer_)
            x_cor = int(answer_.x)
            y_cor = int(answer_.y)
            tim.goto(x_cor, y_cor)
            tim.write(answer)
            guessed_states.append(answer)
            count += 1
    else:
        break

missed_states = [state for state in states_list if state not in guessed_states]

List = pandas.DataFrame(missed_states)
List.to_csv("states_missed.csv")

screen.exitonclick()
