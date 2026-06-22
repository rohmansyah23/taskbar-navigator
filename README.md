# 🚀 Taskbar Auto-Navigator

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight and smart Windows automation tool that re-maps taskbar navigation to the `Alt` key. This utility ensures that your applications not only switch focus but also pop to the foreground, effectively solving the "minimized window" issue.

## ✨ Features

- **Ergonomic Hotkeys**: Uses `Alt + [Number]` instead of the default Windows `Win + [Number]`.
- **Anti-Minimize Logic**: Automatically detects if an application remains minimized or fails to focus and re-triggers the command to bring it to the front.
- **Seamless Integration**: Lightweight and runs in the background with minimal resource consumption.

```
## 📂 Project Structure
taskbar-navigator/
├── .gitignore
├── README.md
└── taskbar-navigation/
    ├── main.py          # Core logic
    └── requirements.txt # Dependencies

```

## 🚀 Installation & Setup

### Prerequisites

* Windows OS
* Python 3.x installed

### Steps

1. **Clone the repository:**
```bash
git clone [https://github.com/rohmansyah23/taskbar-navigator.git](https://github.com/rohmansyah23/taskbar-navigator.git)
cd taskbar-navigator

```


2. **Navigate to the script folder:**
```bash
cd taskbar-navigation

```


3. **Install required libraries:**
```bash
pip install -r requirements.txt

```



## 🛠️ Usage

> [!IMPORTANT]
> You must run your terminal or command prompt as **Administrator** for the script to have permission to control keyboard inputs and intercept shortcuts globally.

1. **Run the script:**
```bash
python main.py

```


2. **Use your new shortcuts:**
* `Alt + 1` → Opens or focuses the 1st app on your Taskbar.
* `Alt + 2` → Opens or focuses the 2nd app on your Taskbar.
* ... up to `Alt + 9`.



## 🔍 How it Works

The script captures `Alt + [Number]` keypresses and converts them to the native Windows `Win + [Number]` commands.

After sending the command, it performs a validation check: *"Is the newly focused window actually active and in the foreground?"*. If the target window is still minimized, the script executes an anti-minimize routine to force the window to pop up and stay active.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author

* **Rohmansyah** - [GitHub Profile](https://github.com/rohmansyah23)
