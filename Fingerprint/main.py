# imports
import pyautogui
import keyboard

from colorama import init
from pyautogui import *

# text colors
class colors:
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'

# function to get location of image
def getlocation(x, y):
    if int(x) > 540 and int(x) < 550:
        Column = '1st Column'
    elif int(x) > 680 and int(x) < 690:
        Column = '2nd Column'
    else:
        return
    if int(y) > 340 and int(y) < 350:
        Row = '1st Row'
    elif int(y) > 480 and int(y) < 490:
        Row = '2nd Row'
    elif int(y) > 620 and int(y) < 630:
        Row = '3rd Row'
    elif int(y) > 760 and int(y) < 770:
        Row = '4th Row'
    else:
        return
    return f'{Column} {Row}'

# function that finds fingerprint and components
def findprint():
    try:
        fingerprint1 = pyautogui.locateCenterOnScreen('images/fingerprint1.png', grayscale=True, confidence=0.8)
        if fingerprint1 is not None:
            print(f'{colors.green}Fingerprint 1 Was Found!{colors.end}')
            fingerprint1component1 = pyautogui.locateCenterOnScreen('images/fingerprint1-1.png', grayscale=True, confidence=0.8)
            if fingerprint1component1 is None:
                return False            
            else:
                x = str(fingerprint1component1).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint1component1).replace(')', '')
                y = y[-3:]
                result1 = getlocation(x, y)
                if result1 is None:
                    return False
                else:
                    print(f'{colors.green}Component 1: {result1}{colors.end}')
                    if result1 == '1st Column 1st Row':
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 2nd Row':
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 3rd Row':
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 4th Row':
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 1st Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 2nd Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 3rd Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 4th Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    else:
                        return False
            fingerprint1component2 = pyautogui.locateCenterOnScreen('images/fingerprint1-2.png', grayscale=True, confidence=0.8)
            if fingerprint1component2 is None:
                return False
            else:
                x = str(fingerprint1component2).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint1component2).replace(')', '')
                y = y[-3:]
                result2 = getlocation(x, y)
                if result2 is None:
                    return False
                else:
                    print(f'{colors.green}Component 2: {result2}{colors.end}')
                    if result2 == '1st Column 1st Row':
                        if result1 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')                        
                            keyboard.press('w')                        
                            keyboard.release('w')                       
                            keyboard.press('enter')                        
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('a')                       
                            keyboard.release('a')                        
                            keyboard.press('w')                        
                            keyboard.release('w')                       
                            keyboard.press('w')                        
                            keyboard.release('w')                        
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 2nd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 3rd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 4th Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 1st Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 2nd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 3rd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 4th Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
            fingerprint1component3 = pyautogui.locateCenterOnScreen('images/fingerprint1-3.png', grayscale=True, confidence=0.8)
            if fingerprint1component3 is None:
                return False
            else:
                x = str(fingerprint1component3).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint1component3).replace(')', '')
                y = y[-3:]
                result3 = getlocation(x, y)
                if result3 is None:
                    return False
                else:
                    print(f'{colors.green}Component 3: {result3}{colors.end}')
                    if result3 == '1st Column 1st Row':
                        if result2 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 2nd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 3rd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 4th Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 1st Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 2nd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 3rd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 4th Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
            fingerprint1component4 = pyautogui.locateCenterOnScreen('images/fingerprint1-4.png', grayscale=True, confidence=0.8)
            if fingerprint1component4 is None:
                return False
            else:
                x = str(fingerprint1component4).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint1component4).replace(')', '')
                y = y[-3:]
                result4 = getlocation(x, y)
                if result4 is None:
                    return False
                else:
                    print(f'{colors.green}Component 4: {result4}{colors.end}')
                    if result4 == '1st Column 1st Row':
                        if result3 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 2nd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 3rd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 4th Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 1st Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 2nd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 3rd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 4th Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
                    keyboard.press('tab')
                    keyboard.release('tab')
            onkeypress()
            return False
        fingerprint2 = pyautogui.locateCenterOnScreen('images/fingerprint2.png', grayscale=True, confidence=0.8)
        if fingerprint2 is not None:
            print(f'{colors.green}Fingerprint 2 Was Found!{colors.end}')
            fingerprint2component1 = pyautogui.locateCenterOnScreen('images/fingerprint2-1.png', grayscale=True, confidence=0.8)
            if fingerprint2component1 is None:
                return False
            else:
                x = str(fingerprint2component1).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint2component1).replace(')', '')
                y = y[-3:]
                result1 = getlocation(x, y)
                if result1 is None:
                    return False
                else:
                    print(f'{colors.green}Component 1: {result1}{colors.end}')
                    if result1 == '1st Column 1st Row':
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 2nd Row':
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 3rd Row':
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 4th Row':
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 1st Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 2nd Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 3rd Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 4th Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    else:
                        return False
            fingerprint2component2 = pyautogui.locateCenterOnScreen('images/fingerprint2-2.png', grayscale=True, confidence=0.8)
            if fingerprint2component2 is None:
                return False
            else:
                x = str(fingerprint2component2).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint2component2).replace(')', '')
                y = y[-3:]
                result2 = getlocation(x, y)
                if result2 is None:
                    return False
                else:
                    print(f'{colors.green}Component 2: {result2}{colors.end}')
                    if result2 == '1st Column 1st Row':
                        if result1 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')                        
                            keyboard.press('w')                        
                            keyboard.release('w')                       
                            keyboard.press('enter')                        
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('a')                       
                            keyboard.release('a')                        
                            keyboard.press('w')                        
                            keyboard.release('w')                       
                            keyboard.press('w')                        
                            keyboard.release('w')                        
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 2nd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 3rd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 4th Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 1st Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 2nd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 3rd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 4th Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
            fingerprint2component3 = pyautogui.locateCenterOnScreen('images/fingerprint2-3.png', grayscale=True, confidence=0.8)
            if fingerprint2component3 is None:
                return False
            else:
                x = str(fingerprint2component3).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint2component3).replace(')', '')
                y = y[-3:]
                result3 = getlocation(x, y)
                if result3 is None:
                    return False
                else:
                    print(f'{colors.green}Component 3: {result3}{colors.end}')
                    if result3 == '1st Column 1st Row':
                        if result2 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 2nd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 3rd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 4th Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 1st Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 2nd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 3rd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 4th Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
            fingerprint2component4 = pyautogui.locateCenterOnScreen('images/fingerprint2-4.png', grayscale=True, confidence=0.8)
            if fingerprint2component4 is None:
                return False
            else:
                x = str(fingerprint2component4).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint2component4).replace(')', '')
                y = y[-3:]
                result4 = getlocation(x, y)
                if result4 is None:
                    return False
                else:
                    print(f'{colors.green}Component 4: {result4}{colors.end}')
                    if result4 == '1st Column 1st Row':
                        if result3 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 2nd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 3rd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 4th Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 1st Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 2nd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 3rd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 4th Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
                    keyboard.press('tab')
                    keyboard.release('tab')
            onkeypress()
            return False
        fingerprint3 = pyautogui.locateCenterOnScreen('images/fingerprint3.png', grayscale=True, confidence=0.8)
        if fingerprint3 is not None:
            print(f'{colors.green}Fingerprint 3 Was Found!{colors.end}')
            fingerprint3component1 = pyautogui.locateCenterOnScreen('images/fingerprint3-1.png', grayscale=True, confidence=0.8)
            if fingerprint3component1 is None:
                return False
            else:
                x = str(fingerprint3component1).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint3component1).replace(')', '')
                y = y[-3:]
                result1 = getlocation(x, y)
                if result1 is None:
                    return False
                else:
                    print(f'{colors.green}Component 1: {result1}{colors.end}')
                    if result1 == '1st Column 1st Row':
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 2nd Row':
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 3rd Row':
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 4th Row':
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 1st Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 2nd Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 3rd Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 4th Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    else:
                        return False
            fingerprint3component2 = pyautogui.locateCenterOnScreen('images/fingerprint3-2.png', grayscale=True, confidence=0.8)
            if fingerprint3component2 is None:
                return False
            else:
                x = str(fingerprint3component2).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint3component2).replace(')', '')
                y = y[-3:]
                result2 = getlocation(x, y)
                if result2 is None:
                    return False
                else:
                    print(f'{colors.green}Component 2: {result2}{colors.end}')
                    if result2 == '1st Column 1st Row':
                        if result1 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')                        
                            keyboard.press('w')                        
                            keyboard.release('w')                       
                            keyboard.press('enter')                        
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('a')                       
                            keyboard.release('a')                        
                            keyboard.press('w')                        
                            keyboard.release('w')                       
                            keyboard.press('w')                        
                            keyboard.release('w')                        
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 2nd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 3rd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 4th Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 1st Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 2nd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 3rd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 4th Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
            fingerprint3component3 = pyautogui.locateCenterOnScreen('images/fingerprint3-3.png', grayscale=True, confidence=0.8)
            if fingerprint3component3 is None:
                return False
            else:
                x = str(fingerprint3component3).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint3component3).replace(')', '')
                y = y[-3:]
                result3 = getlocation(x, y)
                if result3 is None:
                    return False
                else:
                    print(f'{colors.green}Component 3: {result3}{colors.end}')
                    if result3 == '1st Column 1st Row':
                        if result2 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 2nd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 3rd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 4th Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 1st Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 2nd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 3rd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 4th Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
            fingerprint3component4 = pyautogui.locateCenterOnScreen('images/fingerprint3-4.png', grayscale=True, confidence=0.8)
            if fingerprint3component4 is None:
                return False
            else:
                x = str(fingerprint3component4).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint3component4).replace(')', '')
                y = y[-3:]
                result4 = getlocation(x, y)
                if result4 is None:
                    return False
                else:
                    print(f'{colors.green}Component 4: {result4}{colors.end}')
                    if result4 == '1st Column 1st Row':
                        if result3 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 2nd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 3rd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 4th Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 1st Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 2nd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 3rd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 4th Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
                    keyboard.press('tab')
                    keyboard.release('tab')
            onkeypress()
            return False
        fingerprint4 = pyautogui.locateCenterOnScreen('images/fingerprint4.png', grayscale=True, confidence=0.8)
        if fingerprint4 is not None:
            print(f'{colors.green}Fingerprint 4 Was Found!{colors.end}')
            fingerprint4component1 = pyautogui.locateCenterOnScreen('images/fingerprint4-1.png', grayscale=True, confidence=0.8)
            if fingerprint4component1 is None:
                return False
            else:
                x = str(fingerprint4component1).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint4component1).replace(')', '')
                y = y[-3:]
                result1 = getlocation(x, y)
                if result1 is None:
                    return False
                else:
                    print(f'{colors.green}Component 1: {result1}{colors.end}')
                    if result1 == '1st Column 1st Row':
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 2nd Row':
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 3rd Row':
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '1st Column 4th Row':
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 1st Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 2nd Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 3rd Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('s')
                        keyboard.release('s')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    elif result1 == '2nd Column 4th Row':
                        keyboard.press('d')
                        keyboard.release('d')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('enter')
                        keyboard.release('enter')
                    else:
                        return False
            fingerprint4component2 = pyautogui.locateCenterOnScreen('images/fingerprint4-2.png', grayscale=True, confidence=0.8)
            if fingerprint4component2 is None:
                return False
            else:
                x = str(fingerprint4component2).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint4component2).replace(')', '')
                y = y[-3:]
                result2 = getlocation(x, y)
                if result2 is None:
                    return False
                else:
                    print(f'{colors.green}Component 2: {result2}{colors.end}')
                    if result2 == '1st Column 1st Row':
                        if result1 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')                        
                            keyboard.press('w')                        
                            keyboard.release('w')                       
                            keyboard.press('enter')                        
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('a')                       
                            keyboard.release('a')                        
                            keyboard.press('w')                        
                            keyboard.release('w')                       
                            keyboard.press('w')                        
                            keyboard.release('w')                        
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 2nd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 3rd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '1st Column 4th Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 1st Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 2nd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 3rd Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result2 == '2nd Column 4th Row':
                        if result1 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result1 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
            fingerprint4component3 = pyautogui.locateCenterOnScreen('images/fingerprint4-3.png', grayscale=True, confidence=0.8)
            if fingerprint4component3 is None:
                return False
            else:
                x = str(fingerprint4component3).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint4component3).replace(')', '')
                y = y[-3:]
                result3 = getlocation(x, y)
                if result3 is None:
                    return False
                else:
                    print(f'{colors.green}Component 3: {result3}{colors.end}')
                    if result3 == '1st Column 1st Row':
                        if result2 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 2nd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 3rd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '1st Column 4th Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 1st Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 2nd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 3rd Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result3 == '2nd Column 4th Row':
                        if result2 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result2 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
            fingerprint4component4 = pyautogui.locateCenterOnScreen('images/fingerprint4-4.png', grayscale=True, confidence=0.8)
            if fingerprint4component4 is None:
                return False
            else:
                x = str(fingerprint4component4).replace('Point(x=', '')
                x = x[:3]
                y = str(fingerprint4component4).replace(')', '')
                y = y[-3:]
                result4 = getlocation(x, y)
                if result4 is None:
                    return False
                else:
                    print(f'{colors.green}Component 4: {result4}{colors.end}')
                    if result4 == '1st Column 1st Row':
                        if result3 == '1st Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 2nd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 3rd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '1st Column 4th Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('a')
                            keyboard.release('a')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 1st Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 2nd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 3rd Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 4th Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    elif result4 == '2nd Column 4th Row':
                        if result3 == '1st Column 1st Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 2nd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 3rd Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '1st Column 4th Row':
                            keyboard.press('d')
                            keyboard.release('d')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 1st Row':
                            keyboard.press('w')
                            keyboard.release('w')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 2nd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                        elif result3 == '2nd Column 3rd Row':
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.press('enter')
                            keyboard.release('enter')
                    else:
                        return False
                    keyboard.press('tab')
                    keyboard.release('tab')
        else:
            return False
    except:
        return False

# function that detects keypress to start
def onkeypress():
    print(f'{colors.green}Press F6 To Solve Fingerprint.{colors.end}')
    keyboard.wait('F6')
    function = findprint()
    if function == False:
        print(f'{colors.red}Invalid.{colors.end}')
    onkeypress()

# run onkeypress function
if __name__ == '__main__':
    os.system('title Fingerprint Bot')
    os.system('cls')
    init()
    onkeypress()