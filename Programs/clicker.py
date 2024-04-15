import time
import pyautogui

i = 0
while (i < 1000):
    time.sleep(0.5)
    current_pos = pyautogui.position()
    pyautogui.click(current_pos)
    i += 1

print("Current mouse position:", current_pos)
