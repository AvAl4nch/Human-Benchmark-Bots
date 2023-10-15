import sys
import time
import pytesseract
from PIL import Image
import keyboard
import pyautogui

def main(delay, x1=800, y1=370, x2=1000, y2=160):
    time.sleep(float(delay))
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    screenshot_path = r'tmp.png'
    my_screenshot = pyautogui.screenshot(region=(800, 370, 1000, 160))
    my_screenshot.save(screenshot_path)

    image = Image.open(screenshot_path)
    text = pytesseract.image_to_string(image)

    lines = text.split('\n')

    for line in lines:
        keyboard.write(line)
        keyboard.press_and_release('space')

if __name__ == "__main__":
    delay = float()
    x1 = int()
    y1 = int()
    x2 = int()
    y2 = int()


    if len(sys.argv) == 6:
        delay = sys.argv[1]
        x1 = int(sys.argv[2])
        y1 = int(sys.argv[3])
        x2 = int(sys.argv[4]) - int(sys.argv[2])
        y2 = int(sys.argv[5]) - int(sys.argv[3])
    elif len(sys.argv) == 2:
        delay = sys.argv[1]
    elif len(sys.argv) == 1:
        delay = 2.0
    else:
        print('invalid number of arguments! \ncommand must be like:\npython typing_speed_bt.py [delay] [x1 y1 x2 y2]')
        exit()

    main(delay, x1, y1, x2, y2)




