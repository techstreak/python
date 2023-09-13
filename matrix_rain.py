import random
import time

# Constants
WIDTH, HEIGHT = 80, 24

# Create an empty screen
screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

while True:
    # Add a random character ('0' or '1') to the top row in green color
    char = random.choice(['0', '1'])
    screen[0][random.randint(0, WIDTH - 1)] = f"\033[32m{char}\033[0m"  # 32 represents green color

    # Shift characters down
    for i in range(HEIGHT - 1, 0, -1):
        screen[i] = screen[i - 1][:]

    # Print the screen
    for row in screen:
        print("".join(row))

    # Introduce a small delay for animation
    time.sleep(0.03)  # Adjust this value to control the animation speed
