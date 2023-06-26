from datetime import datetime
from config_logger import setup_logger
import json
import os

logger = setup_logger()


class DataTrip:
    def __init__(
        self, total_time, stop_time, move_time, bill_stop, bill_move, bill_total
    ):
        self.total_time = total_time
        self.stop_time = stop_time
        self.move_time = move_time
        self.bill_stop = bill_stop
        self.bill_move = bill_move
        self.bill_total = bill_total
        self.today = datetime.now().strftime("%d-%m-%Y")
        self.hour = datetime.now().strftime("%H:%M")
        self.id = id(self.hour)

    def data_to_json(self):
        """
        This function converts data attributes into a JSON format and returns it as a string.
        :return: The method `data_to_json` returns a JSON string representation of a dictionary
        containing various data attributes.
        """
        data = {
            "id": self.id,
            "today": self.today,
            "hour": self.hour,
            "total_time": self.total_time,
            "total_stopped_time": self.stop_time,
            "total_movement_time": self.move_time,
            "total_bill_stop": self.bill_stop,
            "total_bill_move": self.bill_move,
            "total_bill_total": self.bill_total,
        }
        logger.info("Data converted to JSON")
        return json.dumps(data, indent=4)

    def save_history_to_file(self, json_data: str):
        """
        This function saves JSON data to a file named "history.json" and ensures that the file contains
        valid JSON format.

        :param json_data: A string containing JSON-formatted data to be saved to a file
        :type json_data: str
        """
        if not os.path.isfile("history.json"):
            with open("history.json", "w") as file:
                file.write("[")
                logger.info("File 'history.json' created")
        else:
            with open("history.json", "r") as file:
                content = file.read().strip()

            if content.endswith("],"):
                content = content[:-2]
            elif content.endswith("]"):
                content = content[:-1]

            with open("history.json", "w") as file:
                file.write(content)

        with open("history.json", "a") as file:
            if os.stat("history.json").st_size > 1:
                file.write(",")
            file.write(json_data)
            logger.info("Data saved to file 'history.json'")

        with open("history.json", "a") as file:
            file.write("]")
