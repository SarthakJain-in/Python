from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        
    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.95

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.95

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.05