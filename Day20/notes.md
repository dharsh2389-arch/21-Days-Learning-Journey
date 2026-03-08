Graphical User Interface using Tkinter

Tkinter is Python’s built-in library for creating desktop graphical user interfaces (GUI).
It allows you to create:
Windows
Buttons
Forms
Input fields
Dialog boxes
Simple desktop applications

1. Importing Tkinter

import tkinter as tk

2. Creating the Main Window
Every GUI program starts with a main window.

import tkinter as tk
window = tk.Tk()
window.title("My Application")
window.mainloop()

Explanation:
Tk() - create window
title() - set window title
mainloop() - start GUI program

3. Window Properties
You can customize the window.

import tkinter as tk
window = tk.Tk()
window.title("My App")
window.geometry("400x300")
window.mainloop()

Common window properties:

Property	  Example
Title	      window.title("App")
Size	      window.geometry("400x300")
Background	window.config(bg="lightblue")

4. Label Widget
Displays text in the window.

import tkinter as tk
window = tk.Tk()
label = tk.Label(window, text="Hello Python")
label.pack()
window.mainloop()

5. Button Widget
Buttons trigger actions.

import tkinter as tk
window = tk.Tk()
button = tk.Button(window, text="Click Me")
button.pack()
window.mainloop()

6. Button with Function
   
import tkinter as tk
window = tk.Tk()
def greet():
    print("Hello")
button = tk.Button(window, text="Click", command=greet)
button.pack()
window.mainloop()

7. Entry Widget (Input Field)
Allows user input.

import tkinter as tk
window = tk.Tk()
entry = tk.Entry(window)
entry.pack()
window.mainloop()

8. Getting Input from Entry

import tkinter as tk
window = tk.Tk()
def show_text():
    print(entry.get())
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Submit", command=show_text)
button.pack()
window.mainloop()

9. Layout Managers
Tkinter provides three layout systems.

pack()
Places widgets vertically.

label.pack()
button.pack()

grid()
Places widgets in rows and columns.

import tkinter as tk
window = tk.Tk()
tk.Label(window,text="Name").grid(row=0,column=0)
tk.Entry(window).grid(row=0,column=1)
window.mainloop()

place()
Places widgets using exact coordinates.

button.place(x=50,y=100)

10. Text Widget
Used for multi-line input.

import tkinter as tk
window = tk.Tk()
text = tk.Text(window)
text.pack()
window.mainloop()

11. Checkbutton
Allows selecting options.

import tkinter as tk
window = tk.Tk()
var = tk.IntVar()
check = tk.Checkbutton(window,text="Accept",variable=var)
check.pack()
window.mainloop()

12. Radiobutton
Allows selecting one option from multiple choices.

import tkinter as tk
window = tk.Tk()
var = tk.IntVar()
tk.Radiobutton(window,text="Male",variable=var,value=1).pack()
tk.Radiobutton(window,text="Female",variable=var,value=2).pack()
window.mainloop()

13. Listbox
Displays a list of items.

import tkinter as tk
window = tk.Tk()
listbox = tk.Listbox(window)
listbox.insert(1,"Python")
listbox.insert(2,"Java")
listbox.pack()
window.mainloop()

14. Message Boxes
Used for popup messages.

import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
messagebox.showinfo("Info","Hello")
window.mainloop()

15. File Dialog
Used to select files.

from tkinter import filedialog
file = filedialog.askopenfilename()
print(file)

16. Menu Bar
Menus organize commands.

import tkinter as tk
window = tk.Tk()
menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Exit",command=window.quit)
window.mainloop()

17. Event Handling
Events trigger actions.

Example events:
Button click
Key press
Mouse click

Example:
button = tk.Button(window,text="Click",command=my_function)

18. Example (Calculator)

import tkinter as tk
window = tk.Tk()
entry = tk.Entry(window)
entry.pack()
def calculate():
    result = eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(0,result)
button = tk.Button(window,text="Calculate",command=calculate)
button.pack()
window.mainloop()

19. Common Tkinter Widgets
Widget	     Purpose
Label	       display text
Button	     click action
Entry	       input field
Text         multi-line text
Checkbutton  checkbox
Radiobutton	 option select
Listbox	     list display
Menu	       application menu
