from turtle import Screen
from Paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(paddle_right.go_up, "Up")
screen.onkeypress(paddle_right.go_down, "Down")
screen.onkeypress(paddle_left.go_up, "w")
screen.onkeypress(paddle_left.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 60 and ball.xcor() > 320 or ball.distance(paddle_left) < 60 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 400:
        scoreboard.clear()
        ball.reset_pos()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -400:
        scoreboard.clear()
        ball.reset_pos()
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()