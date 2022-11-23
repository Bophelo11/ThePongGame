from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.score_keeper_update()

    def score_keeper_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Helivetica", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Helivetica", 80, "normal"))

    def left_point(self):
        self.left_score += 1
        self.score_keeper_update()

    def right_point(self):
        self.right_score += 1
        self.score_keeper_update()