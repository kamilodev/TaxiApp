from Modules.Timer import Timer
from Modules.Prices import Prices
from Modules.History import History
from Modules.Print_Values import Print_Values

class Fees:
    def __init__(self):
        self.chrono = Timer()
        self.printer = Print_Values()
        self.total_time = 0
        self.total_stopped_time = 0
        self.total_movement_time = 0
        self.start_message = "Inicio de carrera, El taxi esta detenido, pulsa <space> para ponerlo en marcha\n"

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

        history = History(
            round(self.total_time, 2),
            round(self.total_stopped_time, 2),
            round(self.total_movement_time, 2),
            bill_stop,
            bill_move,
            total_bill,
        )

        json_data = history.to_json()
        history.save_history_to_file(json_data)
        self.printer.show_info()