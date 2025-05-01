from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", align="left" ,font= FONT)

    def level_up(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center" , font=FONT)
