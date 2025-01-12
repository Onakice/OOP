import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *

# root = ttk.Window(themename='superhero')
root = tk.Tk()
root.title("Radio Button")
root.geometry('500x200')

def clicker():
    my_label.config(text=my_topping.get())

toppings = ["pepperoni","Cheese","Veggie"]
my_topping = tk.StringVar()

for topping in toppings:
    ttk.Radiobutton(root, bootstyle="danger", variable=my_topping, text=topping,
                    value=topping).pack(side="left",padx=5,pady=5)
    
my_button = ttk.Button(root, text="select", bootstyle="info", command=clicker)
my_button.pack(side="left",padx=10,pady=5)

my_label = ttk.Label(root, text="", font=("Helvetica",14))
my_label.pack(side="left",padx=10)

root.mainloop()