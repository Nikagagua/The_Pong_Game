from time import sleep
from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

paddle = Paddles(screen)
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.r_paddle_up, "Up")
screen.onkey(paddle.r_paddle_down, "Down")
screen.onkey(paddle.l_paddle_up, "w")
screen.onkey(paddle.l_paddle_down, "s")

game_on = True

while game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with r_paddle
    if ball.distance(paddle.paddles[0]) < 50 and ball.xcor() > 340 or ball.distance(
            paddle.paddles[1]) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    elif ball.xcor() > 380:
        ball.move_to_winner('right')
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.move_to_winner('left')
        scoreboard.r_point()

screen.exitonclick()
