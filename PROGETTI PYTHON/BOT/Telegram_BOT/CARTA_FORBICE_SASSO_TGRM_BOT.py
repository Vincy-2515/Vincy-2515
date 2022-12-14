#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

#sostituire input con message.text
#sostituire print con bot.reply_to(message, '<messaggio>')
import random
import time
import telebot

API_TOKEN = '5588793568:AAFz3rhqiqaoMwwkkvjAET0WqkmD7P_mxvs'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ciao io sono un bot e sono qui per farti giocare a carta forbice sasso""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):


    def start_program():
        bot.reply_to(message, "Benvenuto utente questa è la versione digitale di Carta, Forbice, Sasso.")
        bot.reply_to(message,
                     "Per giocare scrivere 'play' e inviare per mostrare ulteriori info digitare 'info' e inviare, dopo la rivelazione delle info  il gioco partirà automaticamente")
        start = message.text

        if start == "play":
            print_iniziali()
        elif start == "info":
            bot.reply_to(message, "Versione: relase - 1.1")
            time.sleep(1)
            bot.reply_to(message, "developer: V S")
            time.sleep(2)
            bot.reply_to(message, "START")
            time.sleep(1)
            print_iniziali()

        else:
            bot.reply_to(message, "Scusa non ho capito")
            bot.reply_to(message, "Avvio del programma...")
            time.sleep(2)
            bot.reply_to(message, "START")
            time.sleep(1)
            print_iniziali()

    def print_iniziali():
        # serie di print
        bot.reply_to(message, "Ciao")
        time.sleep(1)
        bot.reply_to(message, "come ti chiami?")
        risposta = message.text
        bot.reply_to(message, "Bene " + risposta + "giochiamo!!!")
        time.sleep(2)
        programma()

    def programma():
        bot.reply_to(message, "Per giocare scegli tra carta=1 sasso=2 forbice=3")
        cfs = message.text
        time.sleep(1)
        bot.reply_to(message, "bene hai fatto la tua scelta")
        time.sleep(1)
        bot.reply_to(message, "ora tocca a me :)")
        time.sleep(1)

        # randomizzatore di numeri
        a = range(1, 4)
        combinazione = random.sample(a, 1)

        # vincita
        if combinazione == [1] and cfs == 2:
            bot.reply_to(message, "HO VINTO!!! io ho scelto carta")
            final()

        if combinazione == [2] and cfs == 3:
            bot.reply_to(message, "HO VINTO!!! io ho scelto sasso")
            final()

        if combinazione == [3] and cfs == 1:
            bot.reply_to(message, "HO VINTO!!! io ho scelto forbice")
            final()

        # perdita
        if combinazione == [2] and cfs == 1:
            bot.reply_to(message, "ho perso :( io ho scelto sasso")
            final()

        if combinazione == [3] and cfs == 2:
            bot.reply_to(message, "ho perso :( io ho scelto forbice")
            final()

        if combinazione == [1] and cfs == 3:
            bot.reply_to(message, "ho perso :( io ho scelto carta")
            final()

        # input_errato
        if cfs > 3:
            bot.reply_to(message, "Scusa non ho capito!")
            programma()

        if cfs < 1:
            bot.reply_to(message, "Scusa non ho capito!")
            programma()

    def final():
        bot.reply_to(message, "Bene il gioco è ora terminato si desidera continuare a giocare oppure ricominciare?")
        bot.reply_to(message, "Nota: continuando verrà usato lo stesso nickname.")
        bot.reply_to(message, "Se si preferisce uscire premere qualsiasi altra lettera e inviare.")
        bot.reply_to(message, "[C]ontinuare o [R]icominciare")
        stay_leave = message.text

        if stay_leave == "C":
            programma()

        if stay_leave == "R":
            print_iniziali()

    # ___STARTER___
    start_program()



bot.infinity_polling()