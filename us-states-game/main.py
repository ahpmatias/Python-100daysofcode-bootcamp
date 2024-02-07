import turtle as t
import pandas as pd

screen = t.Screen()
screen.title('US States Game')
screen.setup(720, 480)
t.bgpic('blank_states_img.gif')
df = pd.read_csv('50_states.csv')

def all_lower(list):
    return [x.lower() for x in list]

guessed_states = []
states = df.state.tolist()
score = 0

while len(guessed_states) < 50:
    guess = t.textinput(f'{score}/50 States correct', 'Guess a US state: ').title()
    if guess == 'Exit':
        break
    if guess in states:
        guessed_states.append(guess)
        state = t.Turtle()
        state.penup()
        state.hideturtle()
        state_data = df[df.state == guess]
        state.goto(int(state_data.x), int(state_data.y))
        state.write(guess)
        score += 1



