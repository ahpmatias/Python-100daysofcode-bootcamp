from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)

    def increment_score(self):
        self.score += 1

    def show_scoreboard(self):
        self.write(f'Level: {self.score}', align='left', font=('Comic Sans', 25, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over!', align='center', font=('Arial', 30, 'normal'))