# Keylogger with Python

This project is a simple keylogger written in Python using the [`pynput`](https://pypi.org/project/pynput/) library.  
It captures keystrokes, including modifier keys (Ctrl, Shift, Alt, Caps Lock), and saves them into a log file.

**Disclaimer**  
This project is created for educational and research purposes only (such as studying how keylogging works, cybersecurity awareness, and defensive programming).  
Do not use it for malicious purposes. Misuse of this code may violate laws and lead to legal consequences. Use responsibly.

---

## Features
- Logs all keystrokes and combinations (e.g., `Ctrl+C`, `Shift+A`).
- Captures special keys like `CapsLock`, `Enter`, etc.
- Detects modifier keys (Ctrl, Shift, Alt).
- Saves logs with timestamp to a file.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/keylogger.git
   cd keylogger
   ```

2. Install required dependencies:
   ```bash
   pip install pynput
   ```

---

## Usage

1. Open `mainkeylogger.py` and set your log file path:
   ```python
   log_file = "C:/path/to/save/keyLog.txt"
   ```

2. Run the script:
   ```bash
   python mainkeylogger.py
   ```

3. The keystrokes will be saved to the file you specified.

---

## Example Log
```
2025-08-26 09:30:15,123: Ctrl+C
2025-08-26 09:30:16,456: Shift+A
2025-08-26 09:30:18,789: CapsLock
```

---

## Legal and Ethical Use
- Allowed: Research, self-education, learning about security.
- Forbidden: Installing on someone else's computer without consent.
