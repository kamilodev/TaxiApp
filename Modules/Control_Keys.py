from pynput import keyboard
from Modules.Fees import Fees


class Control_Keys:
    def __init__(self):
        self.is_move = False
        self.is_new_travel = False
        self.send_fee = Fees()

    def toggle_fee(self):
        if self.is_move == False:
            self.send_fee.fee_stoped()
        else:
            self.send_fee.fee_movement()

    def new_travel_fee(self):
        print("new_travel_fee")

    def on_press(self, key):
        if key == keyboard.Key.space:
            self.is_move = False if self.is_move else True
            self.toggle_fee()

        elif key == keyboard.Key.enter:
            self.is_move = False
            self.is_new_travel = True
            self.new_travel_fee()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def run(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        listener.join()

        self.toggle_fee() if self.is_move else self.toggle_fee()

        if self.is_new_travel:
            self.new_travel_fee()
