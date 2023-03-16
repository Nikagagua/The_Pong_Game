from turtle import Turtle

BALL_WIDTH = 20
BALL_HEIGHT = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def move_to_winner(self, winner):
        if winner == 'right':
            new_x = 350
            self.bounce_x()
        elif winner == 'left':
            new_x = -350
            self.bounce_x()
        else:
            return
        new_y = 0
        self.goto(new_x, new_y)
        self.goto(0, 0)
        self.move_speed = 0.1

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9
