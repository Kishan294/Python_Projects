from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):

        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)