Keystroke Logger
Description
This Python script uses the pyautogui library to capture and log keystrokes. It continuously monitors and prints the keys pressed along with the number of times each key has been pressed.

Warning
This script is intended for educational purposes only. Unauthorized use of keylogging software can violate privacy laws and regulations. Always obtain proper consent before running this script on any system.

Requirements
Python 3.x

pyautogui library

Installation
Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install the required library:


pip install pyautogui
Usage
Run the script:


python keylogger.py
Script Content:

python
import pyautogui

def log_keyrokes():
    while True:
        pressed_keys = pyautogui.getPresses()
        for key, events in pressed_keys.items():
            print(f'{key} was pressed {events} times.')

log_keyrokes()
Notes
Ensure you have the appropriate permissions to run this script on any system.

This script continuously runs until manually stopped. Use Ctrl + C to terminate the script.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
pyautogui documentation for providing the keylogging functionality.
