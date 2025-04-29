from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        x_axis = random.randint(-320, 320)
        y_axis = random.randint(-320, 320)
        self.goto(x_axis, y_axis)