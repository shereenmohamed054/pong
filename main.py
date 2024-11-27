from turtle import Screen
from paddles import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    while ball.xcor() != 360 and ball.ycor() != 260:
        ball.move()
    while ball.xcor() != 375:
        ball.bounce()


screen.exitonclick()
