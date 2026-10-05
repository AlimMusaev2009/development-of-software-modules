import tkinter as tk

number = 0
root = tk.Tk()

def start():
    global number, counter
    number += 1
    counter.config(text=number)

root.geometry('500x500')
root.iconbitmap('../assets/favicon.ico')
root.title('Менеджер ДВИЖУХИ')

counter = tk.label(text=f"{number}")
counter.pack


tk.Button(text="start", background="blue", width=50, height=16).pack(padx=5, pady=20)

root.mainloop()