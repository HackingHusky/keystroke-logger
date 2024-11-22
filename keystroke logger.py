import pyautogui

def log_keyrokes():
    while True:
        pressed_keys = pyautogui.getPresses()
        for key, events in pressed_keys.items():
            print(f'{key} was pressed {events} times.')

log_keyrokes()