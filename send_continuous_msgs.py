import pyautogui
import time

print("starting in 3 seconds...")

time.sleep(3)
for i in range(10):
    pyautogui.write("Happy Birthday to you...")
    pyautogui.press("Enter")
    