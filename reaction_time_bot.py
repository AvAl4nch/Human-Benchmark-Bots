import pyautogui
import time

time.sleep(3)
c = 0

while True:

    pixel = pyautogui.pixel(300, 600)
    if pixel == (75, 219, 106):
        pyautogui.click(100, 600)
        pyautogui.click(100, 600)
        c = c + 1
        if c == 5: break
