from Views.Timer import Timer
from Controllers.Prices import Prices
from Models.DataTrip import DataTrip

class Fees:
    def __init__(self):
        self.chrono = Timer()
        self.total_time = 0
        self.total_stopped_time = 0
        self.total_movement_time = 0
        self.start_message = "\nTaximetro en marcha, El taxi esta detenido 🛑\npulsa <space> para alternar las marchas\n"

    def fee_stoped(self):
        self.total_stopped_time += self.chrono.history_timer()

    def fee_movement(self):
        self.total_movement_time += self.chrono.history_timer()

    def init_end_move(self):
        print(self.start_message)
        self.chrono.history_timer()

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
            round(self.total_time, 2),
            round(self.total_stopped_time, 2),
            round(self.total_movement_time, 2),
            bill_stop,
            bill_move,
            total_bill,
        )
