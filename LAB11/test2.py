import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()

# default label style
l1 = ttk.Label(root, text = "primary", bootstyle="PRIMARY.Inverse")
l1.pack(side=LEFT, padx=5, pady=5)

l2 = ttk.Label(root, text = 'secondary', bootstyle="SECONDARY.Inverse")
l2.pack(side=LEFT, padx=5, pady=5)

l3 = ttk.Label(root, text = 'success', bootstyle="SUCCESS.Inverse")
l3.pack(side=LEFT, padx=5, pady=5)

l4 = ttk.Label(root, text = 'info', bootstyle="INFO.Inverse")
l4.pack(side=LEFT, padx=5, pady=5)

root.mainloop()