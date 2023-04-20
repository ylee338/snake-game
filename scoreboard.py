from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score} ", True, align="center", font=('Arial', 24, 'normal'))


    def add_point(self):
        self.score += 1
        self.clear()
        self.update()
