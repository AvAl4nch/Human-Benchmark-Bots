import sys
import time
from PIL import Image   # image handling
import pyautogui    # for screenshot taking


def main():
    x1, y1, x2, y2 = 800, 170, 1790 - 700, 680 - 150


    if len(sys.argv) == 6:
        delay = sys.argv[1]
        x1 = int(sys.argv[2])
        y1 = int(sys.argv[3])
        x2 = int(sys.argv[4]) - int(sys.argv[2])
        y2 = int(sys.argv[5]) - int(sys.argv[3])
    elif len(sys.argv) == 2:
        delay = sys.argv[1]
    elif len(sys.argv) == 1:
        delay = 4.0
    else:
        print('invalid number of arguments! \ncommand must be like:\npython typing_speed_bt.py [delay] [x1 y1 x2 y2]')
        exit()

    time.sleep(float(delay))

    screenshot_path = r'tmp.png'
    target_path = r'target2.png'

    for _ in range(31):
        my_screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
        my_screenshot.save(screenshot_path)

        pos = pyautogui.locateOnScreen(target_path, region=(x1, y1, x2, y2), confidence=0.5)

        center = [pos.left + pos.width / 2, pos.top + pos.height / 2]

        pyautogui.click(center[0], center[1])


if __name__ == '__main__':
    main()
