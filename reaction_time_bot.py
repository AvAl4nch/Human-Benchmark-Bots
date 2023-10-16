import pyautogui
import time

time.sleep(3)
c = 0

while True:
    x, y = 300, 600
    pixel = pyautogui.pixel(300, 600)
    if pixel == (75, 219, 106): # the RGB values for the  green color 
        pyautogui.click(x, y)
        pyautogui.click(x, y)
        c = c + 1
        if c == 5: break
