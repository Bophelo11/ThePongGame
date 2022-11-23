from turtle import Screen, Turtle
from paddles import Paddle
from PongBall import Ball
from ScoreKeeper import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Lets Play Thuli PONGolo")
screen.tracer(1)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()





screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_down, "z")
screen.onkey(left_paddle.go_up, "w")


game_is_on = True
while game_is_on:
    ball.move_ball()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ycor()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_xcor()

    if ball.xcor() > 380:
        ball.cor_reset()
        scoreboard.left_point()
        screen.update(0.1)

    if ball.xcor() < -380:
        ball.cor_reset()
        scoreboard.right_point()
        screen.update(0.1)




screen.exitonclick()

