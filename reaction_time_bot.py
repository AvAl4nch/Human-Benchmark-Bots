import pyautogui
import time
import argparse


def main():
    args = parse_arguments()

    delay = args.delay
    green = args.green

    if green:
        r, g, b = green
    else:
        r, g, b = 75, 219, 106

    time.sleep(delay)
    c = 0

    while True:
        x, y = 300, 600
        pixel = pyautogui.pixel(300, 600)
        if pixel == (r, g, b):  # the RGB values for the  green color
            pyautogui.click(x, y)
            pyautogui.click(x, y)
            c = c + 1
            if c == 5: break


def parse_arguments():
    parser = argparse.ArgumentParser(description='Reaction Time Bot')
    parser.add_argument('--delay', type=float, default=3, help='Delay before starting')
    parser.add_argument('--green', nargs=3, type=int, help='Green RGB values R G B')
    return parser.parse_args()


if __name__ == '__main__':
    main()
