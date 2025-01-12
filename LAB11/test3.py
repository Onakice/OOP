import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename='superhero')
root.geometry('500x350')

counter = 0

def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text="Hello World!")
    else:
        my_label.config(text="Goodbye World!")

my_label = ttk.Label(root, text="Hello World", font=("Helvetica", 28), bootstyle="danger,inverse")
my_label.pack(pady=50)

my_button = ttk.Button(text="Click Me!", bootstyle="info, outline", command=changer)
my_button.pack(pady=20)

root.mainloop()