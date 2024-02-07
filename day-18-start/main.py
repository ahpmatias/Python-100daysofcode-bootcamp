import turtle as t
import random

tim = t.Turtle()

t.colormode(255)
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# colors = ['blue', 'red', 'green', 'cyan', 'DeepPink', 'gold', 'gray', 'PaleGreen', 'magenta', 'LightSlateBlue','OliveDrab']
#
# for sides in range(4,10):
#     tim.color(random.choice(colors))
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)

random_movements = ['left','right']
tim.pensize(15)
tim.speed('fastest')
for moves in range(200):
    tim.color(random_color())

    movement = random.choice(random_movements)
    if movement == 'left':
        tim.left(90)
    else:
        tim.right(90)
    tim.forward(random.randint(50,300))

# def draw_spriograph(gap):
#     for item in range(int(360/gap)):
#         tim.color(random_color())
#         tim.circle(90)
#         tim.left(gap)
#
# draw_spriograph(1)
screen = t.Screen()
screen.exitonclick()
