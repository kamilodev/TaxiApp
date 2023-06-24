from Views.Timer import Timer
from Controllers.Prices import Prices
from Models.DataTrip import DataTrip


class Fees:
    def __init__(self):
        self.chrono = Timer()
        self.total_time = 0
        self.total_stopped_time = 0
        self.total_movement_time = 0
        self.start_message = "\nTaximetro en marcha, El taxi esta detenido 🛑\npulsa <Control> para alternar las marchas\n"

    def fee_stoped(self):
        self.total_stopped_time += self.chrono.history_timer()

    def fee_movement(self):
        self.total_movement_time += self.chrono.history_timer()

    def init_end_move(self):
        print(self.start_message)
        self.chrono.history_timer()

    def seconds_to_minutes(self, seconds):
        minutes = round(seconds // 60, 2)
        remaining_seconds = round(seconds % 60, 2)
        if minutes == 1:
            minutes_str = " minuto"
        else:
            minutes_str = " minutos"

        if remaining_seconds == 1:
            seconds_str = " segundo"
        else:
            seconds_str = " segundos"

        result = (
            f"{int(minutes)} {minutes_str} y {int(remaining_seconds)} {seconds_str}"
        )
        return result

    def end_travel(self):
        if self.chrono.lapnum % 2 == 0:
            self.total_movement_time += self.chrono.history_timer()
        else:
            self.total_stopped_time += self.chrono.history_timer()

        self.total_time = self.total_movement_time + self.total_stopped_time

        prices = Prices()
        bill_stop, bill_move, total_bill = prices.ticket(
            self.total_stopped_time, self.total_movement_time
        )
        return DataTrip(
            self.seconds_to_minutes(self.total_time),
            self.seconds_to_minutes(self.total_stopped_time),
            self.seconds_to_minutes(self.total_movement_time),
            bill_stop,
            bill_move,
            total_bill,
        )
