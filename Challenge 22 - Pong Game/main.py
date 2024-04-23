from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

# 1. Create the screen
screen = Screen()
screen.title('Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

paddle_1 = Paddle()
paddle_1.goto(-350, 0)

paddle_2 = Paddle()
paddle_2.goto(350, 0)

ball = Ball()

score_1 = Scoreboard()
score_2 = Scoreboard()
score_1.goto(-50, 250)
score_2.goto(50, 250)


screen.listen()
screen.onkeypress(paddle_1.up, 'w')
screen.onkeypress(paddle_1.down, 's')
screen.onkeypress(paddle_2.up, 'Up')
screen.onkeypress(paddle_2.down, 'Down')
screen.onkey(screen.exitonclick, 'BackSpace')

game_is_on = True
while game_is_on:
    score_1.clear()
    score_1.show_scoreboard()
    score_2.clear()
    score_2.show_scoreboard()
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_1) < 50 and ball.xcor() < -330:
        score_1.increment_score()
        ball.paddle_bounce_x()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 330:
        ball.paddle_bounce_x()

    if ball.xcor() < -370:
        ball.home()
        score_2.increment_score()

    if ball.xcor() > 370:
        ball.home()
        score_1.increment_score()





# 4. Create the ball and make it move

# 5. Detect collision with wall and bounce

# 6. Detect collision with paddle

# 7. Detect when paddle misses

# 8. Keep score



screen.exitonclick()