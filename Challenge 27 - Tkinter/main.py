from tkinter import *


#
# window = Tk()
# window.title('My first GUI Program')
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)
#
# # Label
#
# my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
# my_label.grid(column=0, row=0)
#
#
# def button_clicked():
#     new_text = input.get()
#     my_label.config(text=new_text)
#     my_label.pack()
#
#
# button = Button(text='Click here', command=button_clicked)
# button.grid(column=1, row=1)
#
# button2 = Button(text='Click here', command=button_clicked)
# button2.grid(column=2, row=0)

#
# input = Entry(width=10)
# input.grid(column=3, row=2)

def convert_miles_to_km():
    new_text = input.get()
    miles_to_km = round(float(new_text) * 1.60934, 2)
    result.config(text=f'{miles_to_km}')


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=100, height=100)
window.config(padx=30, pady=30)

miles_label = Label(text='Miles', font=('Arial', 20))
miles_label.grid(column=2, row=0)

km_label = Label(text='Km', font=('Arial', 20))
km_label.grid(column=2, row=1)

equal_to_label = Label(text='is equal to', font=('Arial', 20))
equal_to_label.grid(column=0, row=1)

calc_button = Button(text='Calculate', command=convert_miles_to_km)
calc_button.grid(column=1, row=2)

input = Entry(width=20)
input.grid(column=1, row=0)

result = Label(text='', font=('Arial', 20))
result.grid(column=1, row=1)

window.mainloop()  # always in the end of the program
