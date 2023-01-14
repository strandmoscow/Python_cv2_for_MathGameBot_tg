import os
import cv2
import time
from PIL import Image
import pytesseract
import numexpr as ne
import keyboard

def returnString(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    # Perform text extraction
    data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')

    data = data.replace(' ', '')
    data = data.replace('[', '1')
    data = data.replace(']', '1')
    data = data.replace('!', '1')
    data = data.replace('(', '1')
    data = data.replace(')', '1')
    data = data.replace('I', '1')
    data = data.replace('i', '1')
    data = data.replace('l', '1')
    data = data.replace('{', '1')
    data = data.replace('}', '1')
    data = data.replace('|', '1')
    data = data.replace('f', '1')
    data = data.replace('t', '1')
    data = data.replace('O', '0')
    data = data.replace('B', '8')
    data = data.replace('x', '*')
    data = data.replace('х', '*')

    return data


time.sleep(1)

while 1:

    os.system("screencapture screen.png")

    im = Image.open('screen.png')
    im.crop((1800, 700, 2400, 850)).save('screen_crop1.png')
    im.crop((1800, 850, 2400, 1050)).save('screen_crop2.png')

    data1 = returnString(cv2.imread('screen_crop1.png'))[:-1]
    data2 = returnString(cv2.imread('screen_crop2.png'))[1:-1]

    print(data1)
    print(data2)

    try:
        int(data2) == ne.evaluate(data1)
    except ValueError:
        keyboard.press('right')
        keyboard.press('space')
    except SyntaxError:
        keyboard.press('right')
        keyboard.press('space')
    except KeyError:
        keyboard.press('right')
        keyboard.press('space')
    except TypeError:
        keyboard.press('right')
        keyboard.press('space')
    else:
        if int(data2) == ne.evaluate(data1):
            keyboard.press('left')
        else:
            keyboard.press('right')

