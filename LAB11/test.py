import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# root = ttk.Window()
root = ttk.Window(themename="darkly")

b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()