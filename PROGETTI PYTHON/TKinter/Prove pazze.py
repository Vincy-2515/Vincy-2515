import tkinter as tk
from tkinter import messagebox

while True:
    window = tk.Tk()
    window.title("-_-")
    window.resizable(False, False)
    window.configure(background="black")
    text = ":D"
    text_output = tk.Label(window, text=text, fg="white", background="black", font=("SimSun", 72))
    text_output.grid(row=0, column=1, padx=30, sticky="W")
    messagebox.showerror("YOU HAS BEEN HACKED", "I DESTROY YOUR PC")

