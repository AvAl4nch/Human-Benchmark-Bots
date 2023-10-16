import time
import pytesseract
from PIL import Image  # image handling
import keyboard  # for keyboard input
import pyautogui  # for screenshot taking
import argparse


def main():
    args = parse_arguments()

    delay = args.delay
    region = args.region
    path = args.path

    if region:
        x1, y1, x2, y2 = region
        x2 = x2 - x1
        y2 = y2 - y1
    else:
        x1, y1, x2, y2 = 800, 370, 1000, 160

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


def parse_arguments():
    parser = argparse.ArgumentParser(description='Typing Speed Bot')
    parser.add_argument('--delay', type=float, default=4, help='Delay before starting')
    parser.add_argument('--region', nargs=4, type=int, help='Region coordinates x1 y1 x2 y2')
    parser.add_argument('--path', type=str, default=r'C:\Program Files\Tesseract-OCR\tesseract.exe',
                        help='path to tesseract.exe')
    return parser.parse_args()


if __name__ == "__main__":
    main()
