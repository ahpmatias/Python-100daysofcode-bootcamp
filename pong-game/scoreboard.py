from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)

    def increment_score(self):
        self.score += 1

    def show_scoreboard(self):
        self.write(self.score, align='center', font=('Arial', 30, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write('Game over!', align='center', font=('Arial', 30, 'normal'))
