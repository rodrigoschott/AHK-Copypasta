import tkinter as tk
from tkinter import messagebox

def setup_gui(on_start_stop):
    """
    Sets up the GUI for the Clipboard Recovery Program.

    Args:
        on_start_stop (function): Callback function for the Start/Stop button.
    """
    root = tk.Tk()
    root.title("Clipboard Recovery Program")

    # Status Label
    status_label = tk.Label(root, text="Press 'Shift + V' to start", fg="green")
    status_label.pack(pady=10)

    # Start/Stop Button
    start_stop_button = tk.Button(root, text="Start", command=lambda: on_start_stop(status_label, start_stop_button))
    start_stop_button.pack(pady=5)

    # Exit Button
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=5)

    root.protocol("WM_DELETE_WINDOW", lambda: on_exit(root))
    root.mainloop()

def on_exit(root):
    """
    Handles the GUI exit event.

    Args:
        root (tk.Tk): The root window of the GUI.
    """
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
