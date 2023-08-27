import time
import pyautogui

text = input('text: ')
# text = r"""write_picklez('../../demo.license', {'docs': 10000, 'pages': 10000, 'splits': 10000, 'fields': 10000, 'date_end': '2023-10-15'})'"""
time.sleep(5)

for char in text:
    if char in ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', ':', '"', '|', '<', '>', '?']:
        pyautogui.keyDown('shift')
        pyautogui.write(char)
        pyautogui.keyUp('shift')
    else:
        pyautogui.write(char)