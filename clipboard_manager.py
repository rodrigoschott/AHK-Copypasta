import pyperclip

def get_clipboard_content():
    """
    Retrieves the current content of the system clipboard.

    Returns:
        str: The content of the clipboard.
    """
    try:
        # Attempt to access the clipboard content
        content = pyperclip.paste()
    except Exception as e:
        # Handle potential exceptions (e.g., clipboard access issues)
        print(f"Error accessing clipboard: {e}")
        content = ""

    return content
