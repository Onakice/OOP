import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename='superhero')
root.geometry('500x350')

def checker():
    pass

# Toolbutton
var2 = ttk.BooleanVar()
my_check2 = ttk.Checkbutton(bootstyle="danger, toolbutton",
                            text="Toolbutton!!",
                            variable=var2,
                            onvalue=1,
                            offvalue=0,
                            command=checker)
my_check2.pack(pady=10)

# Toolbutton outlined
var3 = ttk.BooleanVar()
my_check3 = ttk.Checkbutton(bootstyle="success, toolbutton, outline",
                            text="Outlined Toolbutton!!",
                            variable=var3,
                            onvalue=1,
                            offvalue=0,
                            command=checker)
my_check3.pack(pady=10)

# Round Toggle
var4 = ttk.BooleanVar()
my_check4 = ttk.Checkbutton(bootstyle="info, round-toggle",
                            text="Round-Toggle!!",
                            variable=var4,
                            onvalue=1,
                            offvalue=0,
                            command=checker)
my_check4.pack(pady=10)

# Square Toggle
var5 = ttk.BooleanVar()
my_check5 = ttk.Checkbutton(bootstyle="info, square-toggle",
                            text="Square-Toggle!!",
                            variable=var5,
                            onvalue=1,
                            offvalue=0,
                            command=checker)
my_check5.pack(pady=10)

root.mainloop()