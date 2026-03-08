'''Question
Create a GUI login form where the user enters username and password.
When the user clicks Login, the program should display the entered details in the terminal.'''

import tkinter as tk
window = tk.Tk()
window.geometry("400x400")
window.title("Login Form")
tk.Label(window, text="Username").pack()
username = tk.Entry(window)
username.pack()
tk.Label(window, text="Password").pack()
password = tk.Entry(window, show="*")
password.pack()
def login():
    print("Username:", username.get())
    print("Password:", password.get())
button = tk.Button(window, text="Login", command=login)
button.pack()
window.mainloop()
