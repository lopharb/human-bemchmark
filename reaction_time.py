from PIL import ImageGrab
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller
from tools import timer
import time
state = False  # True if the plugin is running


def on_press(key):
    global state

    if key == KeyCode.from_char('s'):
        state = not state
    if key == KeyCode.from_char('t'):
        exit()


def has_color(img, target_color=(75, 219, 106)):
    width, height = img.size
    return img.getpixel((width//3, height//2)) == target_color
    # probably a bad solution, but should work most of the time


def main():
    global state
    GREEN = (75, 219, 106)
    listener = Listener(on_press=on_press)
    listener.start()
    mouse = Controller()
    start_time = time.time()
    while True:
        if state:
            cur_time = time.time()
            # a 20 ms delay between screenshots so we don't click the same image twice
            if cur_time - start_time > 0.02:
                img = ImageGrab.grab()
                start_time = cur_time
                if has_color(img=img, target_color=GREEN):
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.click(Button.left, 1)


if __name__ == "__main__":
    main()
