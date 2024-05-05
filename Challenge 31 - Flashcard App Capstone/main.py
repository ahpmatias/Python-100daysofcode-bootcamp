from tkinter import *
import json
import random
import csv
import time
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
SEC_DURATION = 3
current_card = {}


def get_new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(random_word, text=current_card['French'], fill='black')
    canvas.itemconfig(img_container, image=front_card_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(img_container, image=back_card_image)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(random_word, text=current_card['English'], fill='white')


def is_known():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv('data/words_to_learn.csv', index=False)


df = pd.read_csv('./data/french_words.csv')
data_dict = df.to_dict(orient='records')

window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# Buttons
wrong_button_image = PhotoImage(file='./static/static/images/wrong.png')
wrong_button = Button(image=wrong_button_image, highlightthickness=0, relief='flat', borderwidth=0,
                      command=get_new_card)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file='./static/static/images/right.png')
right_button = Button(image=right_button_image, highlightthickness=0, relief='flat', borderwidth=0,
                      command=is_known)
right_button.grid(column=1, row=1)

front_card_image = PhotoImage(file='./static/static/images/card_front.png')
back_card_image = PhotoImage(file='./static/static/images/card_back.png')

canvas = Canvas(width=800, height=526, relief='flat', borderwidth=0, bg=BACKGROUND_COLOR, highlightthickness=0)
img_container = canvas.create_image(400, 263, image=front_card_image)
language_text = canvas.create_text(400, 150, text='French', fill='black', font=('Arial', 40, 'italic'))
random_word = canvas.create_text(400, 263, text=random.choice(df.French), fill='black', font=('Arial',
                                                                                              60,
                                                                                              'bold'))

canvas.grid(column=0, row=0, columnspan=2)

get_new_card()

window.mainloop()
