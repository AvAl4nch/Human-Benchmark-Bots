import sys
import time
import pytesseract
from PIL import Image   # image handling
import keyboard     # for keyboard input
import pyautogui    # for screenshot taking



def main():
    
    path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    x1, y1, x2, y2 = 800, 370, 1000, 160

    if len(sys.argv) == 7:
        delay = sys.argv[1]
        x1 = int(sys.argv[2])
        y1 = int(sys.argv[3])
        x2 = int(sys.argv[4]) - int(sys.argv[2])
        y2 = int(sys.argv[5]) - int(sys.argv[3])
        path = sys.argv[6]
    elif len(sys.argv) == 6:
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
        print('invalid number of arguments! \ncommand must be like:\npython typing_speed_bt.py [delay] [x1 y1 x2 y2] [path to tesseract.exe]')
        exit()


    time.sleep(float(delay))
    pytesseract.pytesseract.tesseract_cmd = path

    screenshot_path = r'tmp.png'
    my_screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
    my_screenshot.save(screenshot_path)

    image = Image.open(screenshot_path)
    text = pytesseract.image_to_string(image)


    lines = text.split('\n')

    for line in lines:
        keyboard.write(line)
        keyboard.press_and_release('space')


if __name__ == "__main__":
    main()
