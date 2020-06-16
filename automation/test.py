import pyautogui as pag
import time

keys = pag.KEYBOARD_KEYS

file_loc = pag.locateOnScreen('stock/one.png')
download_loc = pag.locateOnScreen('stock/two.png')
pic_loc = pag.locateOnScreen('stock/three.png')

# pag.click(file_loc)
# time.sleep(4)
pag.doubleClick(pic_loc)
# pag.doubleClick(download_loc)
# time.sleep(2)
# pag.doubleClick(pic_loc)

