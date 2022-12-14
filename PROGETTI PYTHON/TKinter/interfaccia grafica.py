import tkinter as tk

window = tk.Tk()
window.geometry("650x600")
window.title("Hello TkInter!")
window.resizable(False, False)
window.configure(background='black')


def first_print():
    text = "Hello!"
    text_output = tk.Label(window, text=text, fg="white", background="black", font=("SimSun", 16))
    text_output.grid(row=0, column=1, padx=30, sticky="W")
    # Nella funzione sticky la "W" sta per ovest che dice
    # al programma di appiccicare testo o bottone in queldeterminato punto

def first_function():
    text = "Salve io sono un programma creato da Vincenzo."
    text_output = tk.Label(window, text=text, fg="white", background="black", font=("SimSun", 16))
    text_output.grid(row=1, column=1, padx=30, sticky="W")

first_button = tk.Button(text="Saluta!", background="gray", fg="white", command=first_print)
first_button.grid(row=0, column=0, sticky="W")

second_button = tk.Button(text="Presentati!", background="gray", fg="white", command=first_function)
second_button.grid(row=1, column=0, pady=20, sticky="W")

if __name__ == "__main__":
    window.mainloop()