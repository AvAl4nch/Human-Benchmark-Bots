# Human Benchmark Bots in Python
This project contains a collection of Python bots that can perform various tasks on the [Human Benchmark](https://humanbenchmark.com) website, such as reaction time, verbal memory, aim trainer, and more. I built this project to challenge myself and learn more about web automation and computer vision. The goal of these bots is to achieve the highest possible scores on each challenge and demonstrate the capabilities of artificial intelligence.
# Installation
To run this project, you need to have Python 3.8 or higher installed on your system. You also need to install the following libraries:
- pytesseract
- pillow
- keyboard
- pyautogui
- [Tesseract-OCR](https://www.softpedia.com/get/Programming/Other-Programming-Files/Tesseract-OCR.shtml)

You can install them using pip:
```
pip install pytesseract pillow keyboard pyautogui
```
- [Tesseract-OCR](https://www.softpedia.com/get/Programming/Other-Programming-Files/Tesseract-OCR.shtml)

intall and lunch th `.exe` installer

# Usage
To run a bot for a specific challenge, simply execute the corresponding Python script. For example, to run the bot for the typing speed challenge, run:

```
python typing_speed_bot.py
```

`[x1 y1 x2 y2]` are the `top left` and `botom right` corners of the text area
## to find `[x1 y1 x2 y2]`
1- open a windows terninal

2- make sure u have all libraries for this project installed mainly `pyautogui`

3- run python3

```
> python3
Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyautogui
>>> pyautogui.displayMousePosition()
Press Ctrl-C to quit.
X:  662 Y: 1141 RGB: (133, 133, 133)
```

4- hover over the corners and type the x, y values

5- to exit press `ctrl+c` then type `exit()`
