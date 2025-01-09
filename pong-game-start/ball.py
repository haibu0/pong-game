from turtle import Turtle

from urllib3.packages.six import moves


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .05

    def move(self):
        self.goto(self.xcor()+ self.x_move, self.ycor()+ self.y_move)

    def bounce(self, x_or_y):
        if x_or_y == 'y':
            self.y_move *= -1
        elif x_or_y == 'x':
            self.x_move *= -1
        else:
            print("invalid bounce input")
    def reset_position(self):
        self.goto(0,0)
        self.bounce('x')
        self.move_speed = .05

