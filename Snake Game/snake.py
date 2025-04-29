from turtle import Turtle, Screen
# screen = Screen()

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVING_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.curr_heading = 0
    
    def create(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.speed("fastest")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create()


    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x_cord = self.segments[seg_num-1].xcor()
            y_cord = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_cord, y_cord)
        self.segments[0].forward(MOVING_DISTANCE)
        self.curr_heading = int(self.segments[0].heading())
        
        
    def upside(self):
        if self.curr_heading != 270:
            self.segments[0].setheading(90)

    def downside(self):
        if self.curr_heading != 90:
            self.segments[0].setheading(270)

    def leftside(self):
        if self.curr_heading != 0:
            self.segments[0].setheading(180)

    def rightside(self):
        if self.curr_heading != 180:
            self.segments[0].setheading(0)
