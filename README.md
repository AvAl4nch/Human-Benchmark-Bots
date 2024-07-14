# Human Benchmark Bots in Python
![Untitled design (1)](https://github.com/user-attachments/assets/731f03ec-4a4a-4c1a-ba27-4c9f611288a4)

This project contains a collection of Python bots that can perform various tasks on the [Human Benchmark](https://humanbenchmark.com) website, such as reaction time, verbal memory, aim trainer, and more. I built this project to challenge myself and learn more about web automation and computer vision. The goal of these bots is to achieve the highest possible scores on each challenge and demonstrate the capabilities of artificial intelligence.
# Installation
To run this project, you need to have Python 3.8 or higher installed on your system. You also need to install the following libraries:
- pytesseract
- pillow
- keyboard
- pyautogui
- OpenCV-python
- argparse
- [Tesseract-OCR](https://www.softpedia.com/get/Programming/Other-Programming-Files/Tesseract-OCR.shtml)

You can install them using pip:
```
pip install pytesseract pillow keyboard pyautogui  OpenCV-python argparse
```
- [Tesseract-OCR](https://www.softpedia.com/get/Programming/Other-Programming-Files/Tesseract-OCR.shtml)

intall and lunch th `.exe` installer

# Usage
To run a bot for a specific challenge, simply execute the corresponding Python script with -h for arguments:

```
python typing_speed_bot.py -h
```
then open  your web brouser on the chalenge 
after th delay period the programe will start 


```
 python .\typing_speed_bot.pyy --delay 5 --region 800 400 1790 560 --path 'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Aim trainer

you need to add a target.png which is a amall pic of the target only, in the same file as the programe

# to find `[x1 y1 x2 y2]` and `RGB` values:

`[x1 y1 x2 y2]` are the `top left` and `botom right` corners of the text area

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

5- to exit press `ctrl+c`


# note
this is just a thing i do as a hobby
if you have any idea how to improve the code don't hesitate sharing it
