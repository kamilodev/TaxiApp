from Modules.Control_Travel import Control_Travel
from Modules.Fees import Fees
from Modules.Timer import Timer


class Reset:
    def __init__(self):
        self.reset_keys = Control_Travel()
        self.reset_fees = Fees()
        self.reset_timer = Timer()

    def reset_control_keys_values(self):
        self.reset_keys.is_move = False
        self.reset_keys.is_new_travel = False

    def reset_fees_values(self):
        self.reset_fees.total_time = 0
        self.reset_fees.total_stopped_time = 0
        self.reset_fees.total_movement_time = 0

    def reset_timer_values(self):
        self.reset_timer.lapnum = 0

    def reset_all_values(self):
        self.reset_control_keys_values()
        self.reset_fees_values()
        self.reset_timer_values()
        print("\nSe han reseteado todos los valores\n")
