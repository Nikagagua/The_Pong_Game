from turtle import Turtle

MOVE_DISTANCE = 20
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
X_POS = [370, -375]


class Paddles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.screen = position
        self.paddles = []

        for paddle_index in range(0, 2):
            new_paddle = Turtle("square")
            new_paddle.color("white")
            new_paddle.shapesize(stretch_wid=5, stretch_len=1)
            new_paddle.penup()
            new_paddle.goto(x=X_POS[paddle_index], y=0)
            self.paddles.append(new_paddle)

    def r_paddle_up(self):
        y = self.paddles[0].ycor() + MOVE_DISTANCE
        if y + PADDLE_HEIGHT / 2 < 300:
            self.paddles[0].sety(y)

    def r_paddle_down(self):
        y = self.paddles[0].ycor() - MOVE_DISTANCE
        if y - PADDLE_HEIGHT / 2 > -300:
            self.paddles[0].sety(y)

    def l_paddle_up(self):
        y = self.paddles[1].ycor() + MOVE_DISTANCE
        if y + PADDLE_HEIGHT / 2 < 300:
            self.paddles[1].sety(y)

    def l_paddle_down(self):
        y = self.paddles[1].ycor() - MOVE_DISTANCE
        if y - PADDLE_HEIGHT / 2 > -300:
            self.paddles[1].sety(y)
