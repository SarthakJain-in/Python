from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_point = 0
        self.r_point = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_point, align="center", font=("Courier", 60, "bold"))
        self.goto(100, 200)
        self.write(self.r_point, align="center", font=("Courier", 60, "bold"))

    def l_score(self):
        self.l_point += 1
        self.display_score()

    def r_score(self):
        self.r_point += 1
        self.display_score()