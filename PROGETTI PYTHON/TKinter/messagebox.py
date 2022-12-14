from tkinter import messagebox

# tipi di message box:
# showinfo , showwarning , showerror , askquestion , askokcancel , askyesno


def Popup():
    response = messagebox.askokcancel("This is my Popup!", "Hello World!")
    print(response)
    if response == 1:
        print("You Clicked Yes!")
    else:
        print("You Clicked No!")

Popup()