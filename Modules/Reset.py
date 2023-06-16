from Modules.Control_Keys import Control_Keys
from Modules.Fees import Fees
from Modules.Timer import Timer


class Reset(self):
    def __init__(self):
        self.reset_keys = Control_Keys()
        self.reset_fees = Fees()
        self.reset_timer = Timer()
        self.start_again = Control_Keys()

    def reset_control_keys(self):
        self.reset_keys.is_move = False
        self.reset_keys.is_new_travel = False

    def reset_fees(self):
        self.reset_fees.total_time = 0
        self.reset_fees.total_stopped_time = 0
        self.reset_fees.total_movement_time = 0

    def start_again(self):
        self.start_again.run()

    def reset_timer(self):
        self.reset_timer.lapnum = 0
