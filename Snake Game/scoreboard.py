from turtle import Turtle


class Display_score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 320)
        self.increase()
        self.off = True
        
    def update_score(self):
        self.clear()
        with open("C:\\Users\\jains\\Downloads\\Python\\Intermediate\\Snake Game\\data.txt") as data:
            self.high_score = int(data.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 18, "bold"))

    def increase(self):
          self.score += 1
          self.clear()
          self.update_score()

    def reset(self):
        if self.score > self.high_score:
            with open("C:\\Users\\jains\\Downloads\\Python\\Intermediate\\Snake Game\\data.txt", "w") as data:
                data.write(f"{self.score}")
                
        self.score = 0
        self.update_score()

    def exit_game(self):
        self.off = False