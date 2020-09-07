import pyautogui as pag
import time
import pyperclip as pc

delay = 0.5
add_noteXY = 829, 334
doneXY = 933, 584
fixed_location = 1325, 150


def click_connect(location):
    pag.click(location)
    
    time.sleep(1)
    pag.click(add_noteXY)
    time.sleep(delay) 
    pag.hotkey('ctrl','v')
    pag.click(doneXY)
    


def connect():
    connectXY = pag.locateOnScreen('img/connectBtn.png')
    nextXY = pag.locateOnScreen('img/next.png')
    
    pag.click(fixed_location)
    
    if connectXY:
        click_connect(connectXY)
    
    if(nextXY):
        pag.click(nextXY)
        time.sleep(3)
    else:
        pag.press('down')
        pag.press('down')


def process():
    pass
