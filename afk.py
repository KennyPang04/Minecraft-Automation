import keyboard
import time


# Parameter: Letter - Type: char
# Presses a key for .5 seconds and then releases
def pressKey(letter):
    keyboard.press(letter)
    time.sleep(0.5)
    keyboard.release(letter)


# Sleep for 5 seconds to let user tab into the game
time.sleep(5)

# Loop the afk bot until the custom key is held
while True:
    if keyboard.is_pressed('p'):
        break
    else:
        pressKey('w')
        pressKey('d')
        pressKey('s')
        pressKey('a')