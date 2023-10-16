import time
import pytesseract
from PIL import Image  # image handling
import pyautogui  # for screenshot taking
import argparse


def main():

    args = parse_arguments()

    delay = args.delay
    goal = args.goal
    text_region = args.text_region
    button_region = args.button_region
    path = args.path

    if text_region:
        x1, y1, x2, y2 = text_region
        x2 = x2 - x1
        y2 = y2 - y1
    else:
        x1, y1, x2, y2 = 1000, 350, 1600 - 1000, 470 - 350

    if button_region:
        a1, b1, a2, b2 = button_region
        a2 = a2 - a1
        b2 = b2 - b1
    else:
        a1, b1, a2, b2 = 1150, 470, 1420 - 1150, 530 - 470

    time.sleep(float(delay))
    pytesseract.pytesseract.tesseract_cmd = path
    screenshot_path = r'tmp.png'
    new_path = r'new.png'
    seen_path = r'seen.png'

    words = set()
    for _ in range(int(goal)):
        my_screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
        my_screenshot.save(screenshot_path)

        image = Image.open(screenshot_path)
        text = pytesseract.image_to_string(image)
        text = text.replace('\n', '')
        if text in words:
            pos = pyautogui.locateOnScreen(seen_path, region=(a1, b1, a2, b2), confidence=0.5)
            pyautogui.click(pos)
        else:
            pos = pyautogui.locateOnScreen(new_path, region=(a1, b1, a2, b2), confidence=0.5)
            pyautogui.click(pos)
        words.add(text)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Verbal Memory Bot')
    parser.add_argument('--delay', type=float, default=3, help='Delay before starting')
    parser.add_argument('--goal', type=int, default=20, help='The score you wanna get')
    parser.add_argument('--text_region', nargs=4, type=int, help='The region coordinates around the text area x1 y1 x2 y2')
    parser.add_argument('--button_region', nargs=4, type=int, help='The region coordinates around the buttons area x1 y1 x2 y2')
    parser.add_argument('--path', type=str, default=r'C:\Program Files\Tesseract-OCR\tesseract.exe',
                        help='path to tesseract.exe')
    return parser.parse_args()


if __name__ == '__main__':
    main()
