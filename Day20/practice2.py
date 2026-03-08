'''Question
Create a GUI program that asks the user to enter a number and tells whether the number is even or odd.'''

import tkinter as tk
window = tk.Tk()
window.geometry("400x400")
window.config(bg="green")
window.title("Even Odd Checker")
def check():
    number = int(entry.get())
    if number % 2 == 0:
        result.config(text="Even Number")
    else:
        result.config(text="Odd Number")
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Check", command=check)
button.pack()
result = tk.Label(window, text="")
result.pack()
window.mainloop()
