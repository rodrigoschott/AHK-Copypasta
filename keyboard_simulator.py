from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

def type_text(text):
    """
    Simulates typing the specified text as keyboard inputs.

    Args:
        text (str): The text to be typed out.
    """
    for char in text:
        if char == '\n':
            # For new lines, press the ENTER key
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif char == '\t':
            # For tabs, press the TAB key
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        else:
            # For regular characters, type them as is
            keyboard.type(char)
        time.sleep(0.05)  # Slight delay between keystrokes for realism
