from keyboard import press, release
from cv2 import imread
from pyautogui import locateOnScreen
from time import sleep
from pathlib import Path
from pynput.mouse import Controller
from win32gui import GetWindowText, GetForegroundWindow

DIR = Path(__file__).parent.absolute().as_posix()

CEO = imread(DIR+"/assets/ceo.png")
MC = imread(DIR+"/assets/mc.png")
CEOSELECTED = imread(DIR+"/assets/ceoselected.png")
ALERT = imread(DIR+"/assets/alert.png")

mouse = Controller()

def enter(count: int = 1) -> None:
    for i in range(count):
        press("enter")
        sleep(0.025)
        release("enter")
        if i + 1 != count:
            sleep(0.025)

def scroll(count: int = 1) -> None:
    for i in range(abs(count)):
        mouse.scroll(0, -1 if count < 0 else 1)
        if i + 1 != abs(count):
            sleep(0.025)

def backout(count: int = 1) -> None:
    for i in range(count):
        press("backspace")
        sleep(0.025)
        release("backspace")
        if i + 1 != count:
            sleep(0.025)

def menu() -> None:
    press("m")
    sleep(0.025)
    release("m")

def escape() -> None:
    press("escape")
    sleep(0.025)
    release("escape")

def isVisible(imagePath: str) -> bool:
    return locateOnScreen(imagePath, grayscale=True, confidence=0.95) is not None

def isFocused() -> bool:
    return GetWindowText(GetForegroundWindow()) == "Grand Theft Auto V"

def enterCEO() -> None:
    scroll(10)
    sleep(0.05)
    if isVisible(CEOSELECTED):
        enter(2)
        sleep(0.025)
    backout(2)

def disbandMC() -> None:
    enter()
    sleep(0.025)
    scroll()
    sleep(0.025)
    enter()
    backout(2)

def buyBST() -> None:
    if isVisible(CEOSELECTED):
        enter()
        sleep(0.025)
        scroll(3)
        sleep(0.025)
        enter()
        sleep(0.025)
        scroll(-1)
        sleep(0.025)
        enter()
    if isVisible(ALERT):
        escape()
    backout(3)

def main() -> None:
    if isFocused():
        menu()
        sleep(0.05)
        if not isVisible(CEO):
            if isVisible(MC):
                disbandMC()
                menu()
                sleep(0.025)
            enterCEO()
            sleep(0.025)
            menu()
            sleep(0.025)
        if isVisible(CEO):
            buyBST()
        else:
            backout()

if __name__ == "__main__":
    main()