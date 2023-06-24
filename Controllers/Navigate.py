from Controllers.ControlTravel import ControlTravel
from Views.PrintValues import PrintValues
from Views import Options
from pynput import keyboard


class Navigate:
    def __init__(self):
        self.control_keys = ControlTravel()
        self.counter = 0
        self.printer = PrintValues()
        self.navigate_message = "\n🚖 Pulsa <Shift> para un nuevo viaje 🚖"
        self.back_menu = "\n📕 Pulsa <Esc> para ir al menu principal 📕"

    def on_press(self, key):
        if key == keyboard.Key.ctrl_l:
            if self.counter == 1:
                self.control_keys.is_move = not self.control_keys.is_move
                self.control_keys.toggle_fee()

        if key == keyboard.Key.shift:
            if self.counter == 2:
                return False
            self.initial()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            Options.print_options()
            return False

    def initial(self):
        if not self.control_keys.is_new_travel and self.counter % 2 == 0:
            self.control_keys.new_travel_fee()
            self.counter += 1
        elif self.counter % 2 != 0:
            self.control_keys.new_travel_fee()
            self.printer.show_info()
            self.counter += 1
            print(self.navigate_message, self.back_menu)

    def run(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        listener.join()
