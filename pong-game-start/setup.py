from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# SCREEN SETUP
screen = Screen()
screen.setup(width=800, height=600)
screen.title("pong")
screen.bgcolor("black")
screen.tracer(0)

# BALL START
ball = Ball()

#SCOREBARD SETUP
scoreboard = Scoreboard()

# PADDLES START
paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
paddle_left.color('Blue')
paddle_right.color('Red')

# PADDLES MOVE
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")