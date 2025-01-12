import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

root = ttk.Window(themename='superhero')
root.title("Resize Button")
root.geometry('500x350')

# Style
my_style = ttk.Style()
my_style.configure('my.TButton', font=("Helvetica",18), width=10)
my_style.configure('success.Outline.TButton', font=("Helvetica",24))

my_button = ttk.Button(text="Click Me!", bootstyle="info", style="my.TButton")
my_button.pack(pady=40)

my2_button = ttk.Button(text="Click Me!", bootstyle="info", style="success.Outline.TButton")
my2_button.pack(pady=40)

root.mainloop()