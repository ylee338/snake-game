from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
position = [(0, 0), (-20, 0), (-40, 0)]

for turtle in range(0,3):
    new_turtle = Turtle(shape='square')
    new_turtle.color("white")
    new_turtle.goto(position[turtle])








screen.exitonclick()