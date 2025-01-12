import tkinter as tk
from tkinter import *
import requests
import json

API_ENDPOINT1 = "http://127.0.0.1:8000/basket/"

def on_click():

    payload = {
        "user_id": user1_id.get(),
        "face": face.get(),
        "price": price.get(),
        "size": size.get(),
        "quantity": quantity.get()
    }
    response = requests.post(API_ENDPOINT1, json=payload)
    
    # if response.ok:
    #     try:
    #         data = response.json()
    #         Label(root, text="Order Complete: " + str(data)).grid(row=8, column=1, padx=5, pady=5)
    #     except json.decoder.JSONDecodeError:
    #         Label(root, text="Order Complete: No data returned").grid(row=8, column=1, padx=5, pady=5)
    # else:
    #     Label(root, text="Failed to place order").grid(row=8, column=1, padx=5, pady=5)

    if response.ok:
        data = response.json()
        Label(root, text="Order Complete: " + str(data)).grid(row=8, column=1, padx=5, pady=5)
        

root = tk.Tk()
root.option_add("*Font", "impact 20")
root.title("App Pizza")
root.geometry('500x200')

user1_id = StringVar()
face = StringVar()
price = StringVar()
size = StringVar()
quantity = StringVar()

Label(root, text="User_ID : ").grid(row=0, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=user1_id, width=12, justify="left").grid(row=0, column=1, padx=10)

Label(root, text="Face : ").grid(row=1, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=face, width=12, justify="left").grid(row=1, column=1, padx=10)

Label(root, text="Price : ").grid(row=2, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=price, width=12, justify="left").grid(row=2, column=1, padx=10)

Label(root, text="Size(S,M,L) : ").grid(row=3, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=size, width=12, justify="left").grid(row=3, column=1, padx=10)

Label(root, text="Quantity : ").grid(row=4, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=quantity, width=12, justify="left").grid(row=4, column=1, padx=10)

Button(root, text=" Order!!! ", bg="green", command=on_click).grid(row=5, column=0, columnspan=2)

# r = requests.get('http://127.0.0.1:8000/docs#/Basket/add_to_basket_basket__user_id__post')
# print(r)

root.mainloop()