from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20

class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITION:
            new_turtle = Turtle(shape='square')
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)


    def move(self):
        for num_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num_seg - 1].xcor()
            new_y = self.segments[num_seg - 1].ycor()
            self.segments[num_seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE)

    def up(self):
        self.segments[0].setheading(90)


    def down(self):
        self.segments[0].setheading(270)


    def left(self):
        self.segments[0].setheading(180)


    def right(self):
        self.segments[0].setheading(0)



