from config_manager import load_config
import json


# The Prices class loads and sets stop and move prices from a configuration file and calculates the
# total bill for a ticket based on stop and move time.
class Prices:
    def __init__(self):
        self.stop = 0
        self.move = 0

    def load_prices(self):
        """
        This function loads the stop and move prices from a configuration file.
        """
        self.config = load_config()
        self.stop = self.config["prices"][0]["stop"]
        self.move = self.config["prices"][0]["move"]

    def set_new_prices(self, stop: float, move: float):
        """
        This function sets new stop and move prices in a configuration file and saves the changes.

        :param stop: The new stop price to be set
        :type stop: float
        :param move: The amount by which the stop loss should be moved when the price moves in favor of
        the trade
        :type move: float
        """
        self.config = load_config()
        self.config["prices"][0]["stop"] = stop
        self.config["prices"][0]["move"] = move
        with open(".config", "w") as file:
            json.dump(self.config, file, indent=4)

    def ticket(self, stop_time: float, move_time: float) -> float:
        """
        This Python function calculates the total bill for a ticket based on stop time and move time.

        :param stop_time: The amount of time the vehicle will be stopped during the trip
        :type stop_time: float
        :param move_time: The time spent moving on the transportation (e.g. bus, train, etc.)
        :type move_time: float
        :return: a tuple containing three values: bill_stop, bill_move, and total_bill.
        """
        self.load_prices()
        bill_stop = round(stop_time * self.stop, 2)
        bill_move = round(move_time * self.move, 2)
        total_bill = round(bill_stop + bill_move, 2)

        return bill_stop, bill_move, total_bill
