from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from setup import *
from scoreboard import Scoreboard


def reset_on_score():
    ball.reset_position()
    paddle_left.goto(-350, 0)
    paddle_right.goto(350, 0)
    time.sleep(3)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # DETECT COLLISON WITH WALL / PADDLE:
    # WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')
    # PADDLE
    if ball.xcor() > 320 and ball.distance(paddle_right) < 50 or ball.xcor() < -320 and ball.distance(paddle_left) < 50:
        ball.bounce('x')
        ball.move_speed*=.9

    # DETECT WHEN PADDLE MISSED A BALL, OTHER PLAYER WILL GAIN A POINT, AND  THE BALL WILL START MOVING TO THE OPPOSITE SIDE
    if ball.xcor() > 380:
        scoreboard.allocate_point('player_l')
        reset_on_score()
    elif ball.xcor() < -380:
        scoreboard.allocate_point('player_r')
        reset_on_score()

    #WINNING CONDITIONS
    if scoreboard.l_score == 5:
        scoreboard.game_over('Player Blue')
        game_on = False
    elif scoreboard.r_score == 5:
        scoreboard.game_over('Player Red')
        game_on = False


screen.exitonclick()
