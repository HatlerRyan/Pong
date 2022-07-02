from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.move_paddle_up, "i")
screen.onkeypress(r_paddle.move_paddle_down, "k")
screen.onkeypress(l_paddle.move_paddle_up, "w")
screen.onkeypress(l_paddle.move_paddle_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.xcor() == 330 and ball.distance(r_paddle) < 75 or ball.xcor() == -330 and ball.distance(l_paddle) < 75:
        ball.return_ball()
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_goal()
        scoreboard.update_score()
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_goal()
        scoreboard.update_score()


































screen.exitonclick()
