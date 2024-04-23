import json
from tkinter import *
from tkinter import messagebox
def search():
    with open('data.json') as json_file:
        data = json.load(json_file)
        print(data)

        if '654654654' in data.keys():
            messagebox.showinfo(title='Success!', message=f'Email: {data["654654654"]["email"]} Password: {data["654654654"]["password"]}')


search()