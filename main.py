from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboad import Scoreboard
import time


screen = Screen()

screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    #Detection of wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect the both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect the ball out of the screen for both paddles
    #r_paddle
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()
    #l_paddle
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()