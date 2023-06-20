from Controllers.ControlTravel import ControlTravel
from Views.PrintValues import PrintValues
from pynput import keyboard


class Navigate:
    def __init__(self):
        self.control_keys = ControlTravel()
        self.counter = 0
        self.printer = PrintValues()
        self.navigate_message = "\n🚖 Pulsa enter para un nuevo viaje 🚖"

    def on_press(self, key):
        if key == keyboard.Key.space:
            if self.counter == 1:
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
            self.control_keys.new_travel_fee()
            self.counter += 1
        elif self.counter % 2 != 0:
            self.control_keys.new_travel_fee()
            self.printer.show_info()
            self.counter += 1
            input(self.navigate_message)

    def run(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        listener.join()
