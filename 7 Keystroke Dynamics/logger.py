from pynput.keyboard import Key, Listener
# for linux
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout


def on_press(key):
    try:
        print(key.char)
        # print(key.char.encode("ascii"))
    # print(f"{key} was pressed")
    except AttributeError:
        print(str(key))

def on_release(key):
    # print(f"{key} was released")
    if (key == Key.esc):
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
    
tcflush(stdin, TCIFLUSH) # flush my stdin buffer