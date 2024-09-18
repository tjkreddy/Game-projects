from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            y_coordinate = self.random_y_axis()
            if self.cars:
                while abs(self.cars[-1].ycor() - y_coordinate) < 20:
                    y_coordinate = self.random_y_axis()

            car.goto(300, y_coordinate)
            self.cars.append(car)

    def random_y_axis(self):
        return random.randint(-250, 250)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



