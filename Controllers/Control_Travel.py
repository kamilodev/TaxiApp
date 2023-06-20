from Controllers.Fees import Fees


class Control_Travel:
    def __init__(self):
        self.send_fee = Fees()
        self.is_move = False
        self.is_new_travel = False
        self.counter = 0

    def toggle_fee(self):
        if self.is_move:
            self.send_fee.fee_stoped()
        else:
            self.send_fee.fee_movement()

    def new_travel_fee(self):
        if not self.is_new_travel:
            self.send_fee.init_end_move()
            self.is_new_travel = True
        else:
            data=self.send_fee.end_travel()
            json_data = data.to_json()
            data.save_history_to_file(json_data)
            return False