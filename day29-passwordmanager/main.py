from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letters = [random.choice(letters) for _ in range(nr_letters)]
    pw_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pw_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pw_numbers + pw_symbols + pw_letters
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_input.insert(0, f'{password}')
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': username,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

        messagebox.showinfo(title='Success!', message='Data saved successfully.')


def search():
    with open('data.json') as json_file:
        data = json.load(json_file)
        print(data)
        search_website = website_input.get()
        if search_website in data.keys():
            messagebox.showinfo(title=f'"{search_website}" already exists.', message=f'Email: '
                                      f'{data["654654654"]["email"]} \nPassword: '
                                      f'{data["654654654"]["password"]}')
        else:
            messagebox.showinfo(title='Oops', message=f'{search_website} not found.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website: ')
website_label.grid(column=0, row=1)
username_label = Label(text='Email/Username: ')
username_label.grid(column=0, row=2)
password_label = Label(text='Password: ')
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=20)
website_input.grid(column=1, row=1, sticky='w')
website_input.focus()
username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2, sticky='w')
username_input.insert(0, 'abc@123.com')
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky='w')

# Buttons
gen_password_button = Button(text='Generate Password', width=15, command=generate_password)
gen_password_button.grid(column=2, row=3, sticky='w')
add_button = Button(text='Add', width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')
search_button = Button(text='Search', width=10, command=search)
search_button.grid(column=2, row=1, sticky='w')

window.mainloop()
