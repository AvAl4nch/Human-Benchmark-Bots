import time
import pyautogui    # for screenshot taking
import argparse


def main():

    args = parse_arguments()

    delay = args.delay
    region = args.region

    if region:
        x1, y1, x2, y2 = region
        x2 = x2 - x1
        y2 = y2 - y1
    else:
        x1, y1, x2, y2 = 800, 170, 1790 - 700, 680 - 150

    time.sleep(float(delay))

    screenshot_path = r'tmp.png'
    target_path = r'target.png'

    for _ in range(31):

        pos = pyautogui.locateOnScreen(target_path, region=(x1, y1, x2, y2), confidence=0.5)
        center = [pos.left + pos.width / 2, pos.top + pos.height / 2]

        pyautogui.click(center[0], center[1])


def parse_arguments():
    parser = argparse.ArgumentParser(description='Aim Trainer Bot')
    parser.add_argument('--delay', type=float, default=4, help='Delay before starting')
    parser.add_argument('--region', nargs=4, type=int, help='Region coordinates x1 y1 x2 y2')
    return parser.parse_args()


if __name__ == '__main__':
    main()
