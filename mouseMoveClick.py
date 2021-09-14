import mouse
import time

while (True):
    mouse.move(500, 300, absolute=True, duration=3)
    mouse.click(button='left')
    time.sleep(60)
    mouse.move(600, 400, absolute=True, duration=3)
    mouse.click(button='left')
    time.sleep(60)

# generate .exe => pyinstaller --onefile main.py