from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", align=ALIGN, font=FONT)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

