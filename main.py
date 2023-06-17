#!/usr/bin/python3

from Modules.Welcome import AppInstructions
from Modules.Control_Travel import Control_Travel
from pynput import keyboard
import time


class Navigate:
    def __init__(self):
        self.control_keys = Control_Travel()
        self.counter = 0

    def on_press(self, key):
        if key == keyboard.Key.space:
            self.control_keys.is_move = not self.control_keys.is_move
            self.control_keys.toggle_fee()

        elif key == keyboard.Key.enter:
            self.counter += 1
            if not self.control_keys.is_new_travel and self.counter % 2 != 0:
                print("Entre a la primera")
                self.control_keys.new_travel_fee()
            elif self.counter % 2 == 0:
                print("Entre a la segunda")
                self.counter = 0
                return False

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def run(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        listener.join()

        if self.control_keys.is_new_travel:
            self.control_keys.new_travel_fee()


def main():
    welcome = AppInstructions()
    navigate = Navigate()
    
    welcome.main_screen()
    navigate.run()


if __name__ == "__main__":
    main.navigate = None
    while True:
        if main.navigate is None:
            time.sleep(10)
            main()
        else:
            print("Entre en el else")
            main.navigate.run()
