from Controllers.Fees import Fees


# The ControlTravel class manages the fees for a travel and saves the travel history.
class ControlTravel:
    def __init__(self):
        self.send_fee = Fees()
        self.is_move = False
        self.is_new_travel = False
        self.counter = 0

    def toggle_fee(self):
        """
        The function toggles between stopping and starting a fee based on whether or not there is
        movement.
        """
        if self.is_move:
            self.send_fee.fee_stoped()
        else:
            self.send_fee.fee_movement()

    def new_travel_fee(self):
        """
        The following function checks if there is a new trip and saves the history after the trip has finished.
        """
        if not self.is_new_travel:
            self.send_fee.init_end_move()
            self.is_new_travel = True
        else:
            data = self.send_fee.end_travel()
            json_data = data.data_to_json()
            data.save_history_to_file(json_data)
            return False
