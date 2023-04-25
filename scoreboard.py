from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.pencolor("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(0, 260)
        self.write(f"Score: {self.score} | High Score: {self.high_score} ", True, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update()

