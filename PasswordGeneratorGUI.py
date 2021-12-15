from tkinter import *
import random

tk = Tk()

tk.title("Password Generator")

tk.geometry("500x200")
tk.maxsize(width=500, height=200)

def generate_password():
    output.delete(0, END)
    length = 10
    symbol = '!@#$%^&*()'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    password = ''
    i = 0
    while i <= length:
        num = random.randint(0,9)
        password += alphabet[num]
        password += symbol[num]
        password += str(num)

        i += 1
        
    return password[:16]

def copy_password():
    tk.clipboard_clear()
    tk.clipboard_append(output.get())
    label1.config(text="Copied to clipboard")


label = Label(tk, text="Password: ")
output = Entry(tk, width=20)
label1 = Label(tk, text="")
copyPassword = Button(tk, text="Copy Password", command=copy_password)
get_password = Button(tk, text="Get Password", command=lambda: output.insert(0, generate_password()), width=20, height=2)

get_password.place(x=175, y=50)
label.place(x=140, y=10)
output.place(x=210, y=10)
copyPassword.place(x=350, y=7)
label1.place(x=175, y=100)
tk.mainloop()
