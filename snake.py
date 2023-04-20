from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

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
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



