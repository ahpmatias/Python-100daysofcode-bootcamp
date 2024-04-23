from turtle import *
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt=
"Which turtle will win the race? Pick a color (blue, red, green, orange, violet): ")

# Create Turtles
tim = Turtle()
tom = Turtle()
john = Turtle()
bob = Turtle()
jan = Turtle()

# Change turtles colors
tim.color('blue')
tom.color('red')
john.color('green')
bob.color('orange')
jan.color('violet')

# Change turtles shapes
tim.shape('turtle')
tom.shape('turtle')
john.shape('turtle')
bob.shape('turtle')
jan.shape('turtle')

# Draw finish line
finish = Turtle()
finish.penup()
finish.goto(x=250, y=150)
finish.setheading(270)
finish.pendown()
finish.goto(x=250, y=-150)

# Move Turtles to Start Line
tim.penup()
tom.penup()
john.penup()
bob.penup()
jan.penup()
tim.goto(x=-230, y=50)
tom.goto(x=-230, y=25)
john.goto(x=-230, y=0)
bob.goto(x=-230, y=-25)
jan.goto(x=-230, y=-50)

positions = [0, 0, 0, 0, 0]

while max(positions) <= 470:  # race is done at this point through random movements for each turtle until one crosses
    # the finish line.
    tim_move = random.randint(10, 30)
    tom_move = random.randint(10, 30)
    john_move = random.randint(10, 30)
    bob_move = random.randint(10, 30)
    jan_move = random.randint(10, 30)

    turtles_moves = [tim_move, tom_move, john_move, bob_move, jan_move]
    turtles_names = [tim, tom, john, bob, jan]

    for num in range(0, len(positions)):
        positions[num] += turtles_moves[num]
        turtles_names[num].forward(turtles_moves[num])

first_place_index = positions.index(max(positions))  # get winner index position
turtles_dict = {0: 'blue', 1: 'red', 2: 'green', 3: 'orange', 4: 'violet'}
print(f'The {turtles_dict[first_place_index]} turtle has won!')

if user_bet == turtles_dict[first_place_index]:
    print("Congratulations! You've won the bet.")
else:
    print("Sorry, you've lost the bet.")

screen.exitonclick()
