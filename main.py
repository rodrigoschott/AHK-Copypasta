from pynput import keyboard
from clipboard_manager import get_clipboard_content
from keyboard_simulator import type_text
import tkinter as tk
from tkinter import messagebox

# Initialize the listener with no specific on_press function yet
listener = None

def on_activate():
    """
    Called when the hotkey is activated. Retrieves the clipboard content
    and simulates typing it out.
    """
    clipboard_content = get_clipboard_content()
    print("Typing out clipboard content...")
    type_text(clipboard_content)

def toggle_listener(status_label, start_stop_button):
    """
    Starts or stops the listener based on its current state and updates the GUI.
    """
    global listener
    if listener is None:
        # Define what to do on key press
        def on_press(key):
            try:
                if key == keyboard.Key.insert:
                    on_activate()
            except AttributeError:
                pass

        # Start the listener
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        status_label.config(text="Listening for 'Insert'", fg="green")
        start_stop_button.config(text="Stop")
    else:
        # Stop the listener
        listener.stop()
        listener = None
        status_label.config(text="Not Listening", fg="red")
        start_stop_button.config(text="Start")

def setup_gui():
    """
    Sets up the GUI for the program.
    """
    root = tk.Tk()
    root.title("Clipboard Recovery Program")

    status_label = tk.Label(root, text="Not Listening", fg="red")
    status_label.pack(pady=10)

    start_stop_button = tk.Button(root, text="Start", command=lambda: toggle_listener(status_label, start_stop_button))
    start_stop_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=lambda: on_exit(root))
    exit_button.pack(pady=5)

    root.mainloop()

def on_exit(root):
    """
    Handles the exit process for the GUI.
    """
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        global listener
        if listener is not None:
            listener.stop()
        root.destroy()

if __name__ == "__main__":
    setup_gui()
