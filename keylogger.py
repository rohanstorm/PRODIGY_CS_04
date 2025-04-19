from pynput import keyboard
import logging
import os

# Define the path to save the keylog file
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keylog.txt")

# Set up logging configuration
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

print(f"Logging started. Keys will be saved to: {log_file_path}")
print("Press ESC to stop logging...")

# Function to call on key press
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
        print(f'Key {key.char} pressed')  # Print for debug
    except AttributeError:
        logging.info(f'Special key {key} pressed')
        print(f'Special key {key} pressed')  # Print for debug

# Function to call on key release
def on_release(key):
    if key == keyboard.Key.esc:
        print("ESC pressed. Exiting...")
        return False  # Stop listener

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
