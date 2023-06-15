from Modules.Timer import Timer
from Modules.Print_Values import Print_Values


class Fees:
    def __init__(self):
        self.print = Print_Values()
        self.chrono = Timer()
        self.state = True
        self.total_time = 0
        self.total_stopped_time = 0
        self.total_movement_time = 0

    def fee_stoped(self):
        print("Tarifa detenido")
        # self.chrono.history_timer()
        self.total_stopped_time += self.chrono.history_timer()

    def fee_movement(self):
        print("Tarifa movimiento")
        # self.chrono.history_timer()
        self.total_movement_time += self.chrono.history_timer()

    def init_end_move(self):
        if self.state == True:
            print("Inicio de carrera, tarifa detenido\n")
            self.chrono.history_timer()
            self.state = False

    def end_travel(self):
        if self.chrono.lapnum % 2 == 0:
            self.total_movement_time += self.chrono.history_timer()
        else:
            self.total_stopped_time += self.chrono.history_timer()

        self.total_time = self.total_movement_time + self.total_stopped_time
        self.print.show_info(
            self.total_stopped_time, self.total_movement_time, self.total_time
        )

        return False
