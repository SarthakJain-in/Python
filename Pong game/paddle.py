from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        y_cord = self.ycor() + 20
        x_cord = self.xcor()
        self.goto(x_cord, y_cord)

    def move_down(self):
        y_cord = self.ycor() - 20
        x_cord = self.xcor()
        self.goto(x_cord, y_cord)