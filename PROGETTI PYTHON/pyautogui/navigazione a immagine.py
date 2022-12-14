from time import sleep
import pyautogui as pt

from pynput.mouse import Controller
pt.FAILSAFE = True
mouse = Controller()

# Localizzatore di punti nello schermo
def nav_to_image(image, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.8)
    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=.5)
        pt.moveRel(off_x, off_y, duration=.2)
        pt.click()

#Navigazione del cursore verso l'immagine
sleep(1)
nav_to_image('C:/Users/vince/PycharmProjects/PROGETTI PYTHON/.png')
#----------------------------------------------------------------------------