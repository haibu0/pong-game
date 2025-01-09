from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(xcor, ycor)
        #FOR RIGHT PADDLE (350, 0)


    def move_up(self):
        y_increment = 70
        self.goto(self.xcor(), self.ycor() + y_increment)
        #self.goto(self.xcor(), 250)

    def move_down(self):
        y_increment = 70
        self.goto(self.xcor(), self.ycor() - y_increment)
        #self.goto(self.xcor(), -250)