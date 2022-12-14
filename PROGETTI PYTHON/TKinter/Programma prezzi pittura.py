#import time
import tkinter as tk


window = tk.Tk()
window.geometry("445x550")
window.title("Calculator")
window.configure(background="#CFFFFF")
window.resizable(False, False)
font_color = "black"
background_color = "#CFFFFF"



#welcome label
welcome_label = tk.Label(window,
                         text="Aggiungere il valore in entrami i campi!",
                         fg=font_color,
                         bg=background_color,
                         font=("SimSun", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)


#text input metri
text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)
user_input = text_input.get()


#prezzo_pittura =  3 * user_input
#prezzo_cartone =  4 * user_input

#calcolo_finale = prezzo_pittura + prezzo_cartone


def calcolate():
    if text_input.get():
        risposta = 7.50 * 2

        # label risposta vero
        response_label = tk.Label(window,
                                  text=risposta,
                                  fg=font_color,
                                  bg=background_color,
                                  font=("SimSun", 15))
        response_label.grid(row=3, column=0, sticky="WE")

    else:
        response_label = tk.Label(window,
                                  text="Per favore aggiungere un VALORE!",
                                  fg=font_color,
                                  bg=background_color,
                                  font=("SimSun", 15))
        response_label.grid(row=3, column=0, sticky="WE")


#pulsanti
bottone_calcolo = tk.Button(text="CALCOLARE", command=calcolate)
bottone_calcolo.grid(row=2, column=0, sticky="WE", pady=10, padx=10)


if __name__ == "__main__":
    window.mainloop()