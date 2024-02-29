from pynput.keyboard import Key, Listener

def on_press(key):
    print(f"{key} pressed")

def on_release(key):
    if key == Key.insert:
        print("Insert key detected")
        # Add your activation logic here
    print(f"{key} released")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
