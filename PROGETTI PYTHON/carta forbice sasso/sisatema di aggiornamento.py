from update_check import isUpToDate
from tkinter import messagebox
from update_check import checkForUpdates




# tipi di message box:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

directory = "C:/Users/vince/PycharmProjects/PROGETTI PYTHON/carta forbice sasso/CARTA FORBICE SASSO copia prova.py"

sito_aggiornamento = "https://raw.githubusercontent.com/Vhincy/carta_forbice_sasso_update/main" \
                     "/Carta%2C%20Forbice%2C%20Sasso%201.1.py?token=GHSAT0AAAAAABYU55NV44FRKF6ADQHQSUFOYZHJHZA"


#Procedura di aggiornamento
def Popup():
    response = messagebox.askokcancel("Update checker", "Un nuovo aggiornamento è stato trovato "
                                                       "premere <OK> per aggiornare")
    if response == 1:
        checkForUpdates(directory, sito_aggiornamento)
    else:
        pass


#Verifica aggiornamento
if isUpToDate(directory, sito_aggiornamento) == False:
    Popup()