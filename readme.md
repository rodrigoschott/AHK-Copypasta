# Clipboard Recovery Program

The Clipboard Recovery Program is a utility designed to run on Windows, allowing users to recover and automatically "type out" the last entry of their clipboard by simulating keyboard clicks. This tool is particularly useful for quickly pasting clipboard content into applications that do not support traditional paste operations.

## Features

- **Clipboard Monitoring**: Continuously monitors the clipboard for new content.
- **Keyboard Simulation**: Types out the clipboard's content as if entered manually via the keyboard, including spaces, new lines, etc.
- **Custom Hotkey Activation**: Utilizes the "Insert" key as a trigger for pasting the clipboard content.

## Installation

To use the Clipboard Recovery Program, follow these steps:

1. Download the latest version of the program from the [releases page](https://github.com/your-username/your-repo/releases).
2. Unzip the downloaded file to a convenient location on your computer.
3. Run the installer and follow the on-screen instructions.

## Usage

1. Start the Clipboard Recovery Program.
2. Copy any text or data you wish to "type out" into an application.
3. Press the "Insert" key. The program will simulate typing the content of the clipboard into the currently focused application.

## How It Works

The program uses the following Python libraries:

- [`pyperclip`](https://pypi.org/project/pyperclip/): For accessing the system clipboard.
- [`pynput`](https://pypi.org/project/pynput/): To monitor keyboard inputs and simulate keyboard typing.

When active, the program listens for the "Insert" key press. Upon detection, it fetches the current content of the clipboard and simulates typing this content, character by character, into the currently active application.

## Development

To set up a development environment for the Clipboard Recovery Program, you will need Python installed on your system. It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
Install the required dependencies:
```bash
pip install pyperclip pynput
```

You can then clone the repository and make your modifications:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```