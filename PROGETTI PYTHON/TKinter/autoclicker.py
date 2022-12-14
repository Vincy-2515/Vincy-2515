import tkinter as tk
from time import sleep
import pyautogui as pt
import keyboard

#window configurations
window = tk.Tk()
window.geometry("266x80")
window.title("Autoclicker >:D")
window.configure(background="#828182")
#window.resizable(False, False)
font_color = "black"
background_color = "#828182"
button_font_color="black"
button_Background_color="#69514D"

#Label
welcome_label = tk.Label(window,
                         text="=====Welcome User=====",
                         fg=font_color,
                         bg=background_color,
                         font=("SimSun", 15))
welcome_label.grid(row=0, column=0, sticky="WE", padx=20, pady=5)


#Commands




def right_click():
   while True:
       pt.rightClick()


def farm_mode():
    pt.mouseDown()


#Buttons
#"LEFT CLICK MODE"
#button_right = tk.Button(text="LEFT CLICK", command=left_click,
                         #bg=button_Background_color, fg=button_font_color)
#button_right.grid(row=2, column=0, sticky="S", pady=10, padx=10)

"RIGHT CLICK MODE"
button_right = tk.Button(text="RIGHT CLICK", command=right_click,
                         bg=button_Background_color, fg=button_font_color)
button_right.grid(row=2, column=0, sticky="E", pady=0, padx=5)

"FARM MODE"
button_farmmode = tk.Button(text="FARM MODE", command=farm_mode,
                            bg=button_Background_color, fg=button_font_color)
button_farmmode.grid(row=2, column=0, sticky="W", pady=5, padx=5)



#---------------------------------------------------------------------
#Test stuff
if __name__ == "__main__":
    window.mainloop()



if keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey')):
    while True:
        pt.doubleClick()