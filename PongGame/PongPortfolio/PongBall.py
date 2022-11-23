from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.xcor_move = 3
        self.ycor_move = 3
        self.move_speed = 0.1


    def move_ball(self):
        new_xcor = self.xcor() + self.xcor_move
        new_ycor = self.ycor() + self.ycor_move
        self.goto(new_xcor, new_ycor)

    def bounce_ycor(self):
        self.ycor_move *= -1


    def bounce_xcor(self):
        self.xcor_move *= -1
        self.move_speed *= 0.9

    def cor_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_xcor()

