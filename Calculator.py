from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

def add_2digit():
    a = askinteger("Number", "Enter first number") 
    b = askinteger("Number", "Enter second number")
    showinfo("Result", f"Addition is {a + b}")

def add_3digit():
    a = askinteger("Number", "Enter first number")
    b = askinteger("Number", "Enter second number")
    c = askinteger("Number", "Enter third number")
    showinfo("Result", f"Addition is {a + b + c}")

def sub_2digit():
    a = askinteger("Number", "Enter first number")
    b = askinteger("Number", "Enter second number")
    result = a - b
    showinfo("Result", f"Subtraction is {result}")

def sub_3digit():
    a = askinteger("Number", "Enter first number")
    b = askinteger("Number", "Enter second number")
    c = askinteger("Number", "Enter third number")
    result = a - b - c
    showinfo("Result", f"Subtraction is {result}")

def mul_2digit():
    a = askinteger("Number", "Enter first number")
    b = askinteger("Number", "Enter second number")
    showinfo("Result", f"Multiplication is {a * b}")

def mul_3digit():
    a = askinteger("Number", "Enter first number")
    b = askinteger("Number", "Enter second number")
    c = askinteger("Number", "Enter third number")
    showinfo("Result", f"Multiplication is {a * b * c}")

def div():
    a = askinteger("Calculator", "Enter a Dividend")
    b = askinteger("Calculator", "Enter a Divisor")
    if b == 0:
        showerror("Error", "Division by zero is not allowed.")
    else:
        showinfo("Result", f"Division result is {a / b:.2f}")


def clear():
    for item in win.winfo_children():
        item.destroy()

def add():
    clear()
    Label(win, text="Select", font="Arial 25 bold",bg="red").pack(pady=20)
    Button(win, text="2 Digit Addition", width=20, command=add_2digit).pack(pady=5)
    Button(win, text="3 Digit Addition", width=20, command=add_3digit).pack(pady=5)
    Button(win, text="Back", width=20, command=mainwindow).pack(pady=10)

def sub():
    clear()
    Label (win, text="Select", font="Arial 25 bold",bg="red").pack(pady=20)
    Button(win, text="2 Digit Subtraction", width=20, command=sub_2digit).pack(pady=5)
    Button(win, text="3 Digit Subtraction", width=20, command=sub_3digit).pack(pady=5)
    Button(win, text="Back", width=20, command=mainwindow).pack(pady=10)

def mul():
    clear()
    Label(win, text="Select", font="Arial 25 bold",bg="red").pack(pady=20)
    Button(win, text="2 Digit Multiplication", width=20, command=mul_2digit).pack(pady=5)
    Button(win, text="3 Digit Multiplication", width=20, command=mul_3digit).pack(pady=5)
    Button(win, text="Back", width=20, command=mainwindow).pack(pady=10)

def mainwindow():
    clear()
    Label(win, text="Basic Calculator", font="Arial 25 bold", bg="red").pack(pady=10)
    Button(win, text="Addition", width=20, command=add).pack(pady=5)
    Button(win, text="Subtraction", width=20, command=sub).pack(pady=5)
    Button(win, text="Multiplication", width=20, command=mul).pack(pady=5)
    Button(win, text="Division", width=20, command=div).pack(pady=5)
    Button(win, text="Close", width=20, command=win.destroy).pack(pady=5)

win = Tk()
win.geometry("300x400")
win.title("Basic Calculator")
win.configure(bg="red")

mainwindow()
win.mainloop()

