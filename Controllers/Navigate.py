from Views import Options
from Controllers.ControlTravel import ControlTravel
from pynput import keyboard


# The `Navigate` class listens for specific keystrokes and executes corresponding functions to start
# or end a trip.
class Navigate:
    def __init__(self):
        self.control_keys = ControlTravel()
        self.counter = 0
        self.navigate_message = "\n🚖 Pulsa <Shift> para un nuevo viaje 🚖"
        self.back_menu = "\n📕 Pulsa <Esc> para ir al menu principal 📕"

    def on_press(self, key):
        """
        The function checks for specific keystrokes.

        :param key: The key that was pressed on the keyboard. It is an object of the `Key` class from
        the `pynput.keyboard` module
        """
        if key == keyboard.Key.ctrl_l:
            if self.counter == 1:
                self.control_keys.is_move = not self.control_keys.is_move
                self.control_keys.toggle_fee()

        if key == keyboard.Key.shift:
            if self.counter == 2:
                return False
            self.initial()

    def on_release(self, key):
        """
        The function checks when press the key esc and show the menu

        :param key: The key that was pressed on the keyboard. It is an object of the `Key` class from
        the `pynput.keyboard` module
        """
        if key == keyboard.Key.esc:
            Options.print_options()
            return False

    def initial(self):
        """
        This function evaluates if it is starting or ending a trip and executes the corresponding function
        """
        if not self.control_keys.is_new_travel and self.counter % 2 == 0:
            self.control_keys.new_travel_fee()
            self.counter += 1
        else:
            self.control_keys.new_travel_fee()
            self.counter += 1
            print(self.navigate_message, self.back_menu)

    def run(self):
        """
        This function starts a keyboard listener and waits for input.
        """
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        listener.join()
