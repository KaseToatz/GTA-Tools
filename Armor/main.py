import keyboard
import time
import pyautogui

from pynput.mouse import Controller
from win32gui import GetWindowText, GetForegroundWindow

keybind = 'k'

mouse = Controller()

def sleep() -> None:
    time.sleep(0.1)

def armorEmpty() -> bool:
    if pyautogui.locateOnScreen('assets/noleft.png', grayscale=True, confidence=0.9):
        return True
    return False

def getInventory() -> bool:
    for x in range(2):
        mouse.scroll(0, -1)
        sleep()
    for x in range(5):
        if not pyautogui.locateOnScreen('assets/inventory.png', grayscale=True, confidence=0.75):
            mouse.scroll(0, -1)
            sleep()
        else:
            keyboard.send('enter')
            sleep()
            return True
    return False

def getBodyArmor() -> None:
    for x in range(3):
        mouse.scroll(0, -1)
        sleep()
    keyboard.send('enter')
    sleep()

def getArmor() -> bool:
    for x in range(3):
        mouse.scroll(0, 1)
        sleep()
    for x in range(5):
        if armorEmpty():
            mouse.scroll(0, 1)
            sleep()
        else:
            keyboard.send('enter')
            sleep()
            return True
    return False

def equipArmor(key) -> None:
    if GetWindowText(GetForegroundWindow()) == 'Grand Theft Auto V':
        keyboard.send('m')
        if not getInventory():
            return keyboard.send('m')
        getBodyArmor()
        if not getArmor():
            return keyboard.send('m')
        keyboard.send('m')

keyboard.on_press_key(keybind, equipArmor, suppress=True)
keyboard.wait()