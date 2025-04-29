from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Display_score

screen = Screen()
screen.setup(700, 700)
screen.title("Snake Game")
screen.tracer(0)

screen.bgcolor("black")

snake = Snake()
snake.create()
food = Food()
score_board = Display_score()

screen.onkey(snake.upside, "Up")
screen.onkey(snake.downside, "Down")
screen.onkey(snake.leftside, "Left")    
screen.onkey(snake.rightside, "Right")
screen.onkey(score_board.exit_game, "e")
screen.listen()
    

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.07)

    is_game_on = score_board.off

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase()

    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.ycor() < -340 :
        score_board.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()