from random import randint
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.refresh()


    def refresh(self):
        random_x = randint(-260, 260)
        random_y = randint(-260, 250)
        self.goto(random_x, random_y)