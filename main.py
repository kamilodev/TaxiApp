#!/usr/bin/python3
from Modules.Welcome import Welcome
from Modules.Welcome import AppInstructions
from Modules.Control_Keys import Control_Keys
from Modules.Reset import Reset
from pynput import keyboard


class Navigate:
    def __init__(self):
        self.control_keys = Control_Keys()
        self.reset = Reset()

    def on_press(self, key):
        if key == keyboard.Key.space:
            self.control_keys.is_move = not self.control_keys.is_move
            self.control_keys.toggle_fee()

        elif key == keyboard.Key.enter:
            if not self.control_keys.is_new_travel:
                self.control_keys.new_travel_fee()
            else:
                self.reset.reset_all_values()
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
    welcome = Welcome()
    welcome.display_welcome_screen()
    instructions = AppInstructions()
    instructions.display_title()
    instructions.display_instructions()
    navigate = Navigate()
    navigate.run()


if __name__ == "__main__":
    main.navigate = None
    while True:
        if main.navigate is None:
            main()
        else:
            main.navigate.run()
