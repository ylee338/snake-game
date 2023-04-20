from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_still_playing = True

while game_still_playing:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect contact with food
    if snake.head.distance(food) < 10:
        food.new_food()








screen.exitonclick()