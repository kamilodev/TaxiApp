import json
from config_manager import load_config


class Prices:
    def __init__(self):
        self.stop = 0
        self.move = 0

    def load_prices(self):
        self.config = load_config()
        self.stop = self.config["prices"][0]["stop"]
        self.move = self.config["prices"][0]["move"]

    def set_new_prices(self, stop: float, move: float):
        self.config = load_config()
        self.config["prices"][0]["stop"] = stop
        self.config["prices"][0]["move"] = move
        with open(".config", "w") as file:
            json.dump(self.config, file, indent=4)

    def ticket(self, stop_time: float, move_time: float) -> float:
        self.load_prices()
        bill_stop = round(stop_time * self.stop, 2)
        bill_move = round(move_time * self.move, 2)
        total_bill = round(bill_stop + bill_move, 2)

        return bill_stop, bill_move, total_bill
