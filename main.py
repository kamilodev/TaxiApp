#!/usr/bin/python3
import time

from Modules.Welcome import AppInstructions
from Modules.Control_Travel import Control_Travel
from Modules.PrintValues import PrintValues
from pynput import keyboard
import warnings, sys


class Navigate:
    def __init__(self):
        self.control_keys = Control_Travel()
        self.counter = 0
        self.printer = PrintValues()

    def on_press(self, key):
        if key == keyboard.Key.space:
            self.control_keys.is_move = not self.control_keys.is_move
            self.control_keys.toggle_fee()

        if key == keyboard.Key.enter:
            if self.counter == 2:
                return False
            self.initial()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def initial(self):
        if not self.control_keys.is_new_travel and self.counter % 2 == 0:
            print("Entre a la primera")
            self.control_keys.new_travel_fee()
            self.counter += 1
        elif self.counter % 2 != 0:
            print("Entre a la segunda")
            self.control_keys.new_travel_fee()
            self.printer.show_info()
            self.counter += 1
            input("Tienes que pulsar enter para continuar...")
            print(self.counter)

    def run(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        listener.join()


def main():
    welcome = AppInstructions()
    navigate = Navigate()

    welcome.main_screen()
    with open('warnings.log', 'w') as f:
        # Redirigir los warnings a un archivo
        warnings.filterwarnings('always')
        warnings.showwarning = lambda *args, **kwargs: None
        sys.stderr = f

        navigate.run()

    sys.stderr = sys.__stderr__

if __name__ == "__main__":
    main.navigate = None
    while True:
        if main.navigate is None:
            main()
        else:
            print("Entre en el else")
            main.navigate.run()