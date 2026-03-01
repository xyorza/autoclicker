import pyautogui
import keyboard
import time

click_type = input("Left or Right (L/R): ").strip().upper()
interval = float(input("Interval (seconds): "))
prefix = input("The Key: ")
is_clicking = False

def toggle():
    global is_clicking
    is_clicking = not is_clicking
    print(f"Active: {is_clicking}")

keyboard.add_hotkey(prefix, toggle)

try:
    while True:
        if is_clicking:
            if click_type == 'L':
                pyautogui.click(button='left')
            else:
                pyautogui.click(button='right')
            time.sleep(interval)
        
        time.sleep(0.01)
        
        if keyboard.is_pressed('esc'):
            break
except KeyboardInterrupt:
    pass