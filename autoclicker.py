import keyboard
import mouse
import time

# Sleep for 5 seconds to let user tab into the game
time.sleep(5)

# Loop the clicks until the custom key is held
while True:
    if keyboard.is_pressed('p'):
        break
    else:
        # Can be modified to 'left' or 'right'
        mouse.click('left')
        # To modify the speed you change the denominator (1 second / # clicks)
        # Since it is a high level language it will
        # not be exactly the amount of clicks per second
        time.sleep(1/10)