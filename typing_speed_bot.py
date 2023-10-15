# work in peogress 
import sys
import pytesseract
from PIL import Image
import keyboard
import time
import pyautogui


time.sleep(float(sys.argv[1]))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



myScreenshot = pyautogui.screenshot(region=(800, 370, 1000, 160))
myScreenshot.save(r'C:\Users\laith\PycharmProjects\typing_test\tmp.png')

image = Image.open('tmp.png')

text = pytesseract.image_to_string(image)


text = text.split('\n')


for line in text:
    keyboard.write(line)
    keyboard.press_and_release('space')



