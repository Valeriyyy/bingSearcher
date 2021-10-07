#!/usr/bin/env python
import pyautogui
import time
from random import *
import string

#keyboard
pyautogui.moveTo(530, 58, duration=2)
pyautogui.click()
pyautogui.moveRel(0,40, duration=2)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('bing.com')
pyautogui.press('enter')
pyautogui.moveTo(540, 340, duration=2)
pyautogui.click()
pyautogui.typewrite('START THE SEARCHING')
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(440, 165, duration=2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
characters = string.ascii_letters + string.digits + string.punctuation
print(characters)
search = ''
for x in range(0,50):
    search += characters[randint(0, len(characters) - 1)]
    pyautogui.click()
    pyautogui.typewrite(characters[randint(0, len(characters) - 1)])
    pyautogui.press('enter')
    time.sleep(5)
