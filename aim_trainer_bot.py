import sys
import time
from PIL import Image   # image handling
import pyautogui    # for screenshot taking


time.sleep(3)


screenshot_path = r'tmp.png'
target_path = r'target2.png'

for _ in range(31):
    my_screenshot = pyautogui.screenshot(region=(800, 170, 1790 - 700, 680 - 150))
    my_screenshot.save(screenshot_path)

    pos = pyautogui.locateOnScreen(target_path, region=(800, 170, 1790 - 700, 680 - 150), confidence=0.5)
    print(pos)
    center = [pos.left + pos.width / 2 , pos.top + pos.height / 2]
    # center = [pos.left + 20, pos.top + 20]
    print(center)
    pyautogui.click(center[0], center[1])
