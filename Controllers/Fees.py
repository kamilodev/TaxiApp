from Views.Timer import Timer
from Controllers.Prices import Prices
from Models.DataTrip import DataTrip


# The `Fees` class calculates the total time, stopped time, movement time, and bills for a taxi trip
# based on the time history and ticket prices.
class Fees:
    def __init__(self):
        self.chrono = Timer()
        self.total_time = 0
        self.total_stopped_time = 0
        self.total_movement_time = 0
        self.start_message = "\nTaximetro en marcha, El taxi esta detenido 🛑\npulsa <Control> para alternar las marchas\n"

    def fee_stoped(self):
        """
        This function updates the total stopped time by adding the time elapsed since the last stop.
        """
        self.total_stopped_time += self.chrono.history_timer()

    def fee_movement(self):
        """
        This function updates the total movement time by adding the time elapsed since the last
        movement.
        """
        self.total_movement_time += self.chrono.history_timer()

    def init_end_move(self):
        """
        This function starts a timer for a new travel.
        """
        print(self.start_message)
        self.chrono.history_timer()

    def seconds_to_minutes(self, seconds: float) -> str:
        """
        The function converts a given number of seconds to minutes and seconds, and returns the result
        as a string.

        :param seconds: The input parameter is a float representing the number of seconds that needs to
        be converted to minutes and seconds
        :type seconds: float
        :return: a string that represents the input number of seconds converted to minutes and seconds,
        with appropriate pluralization of the units. The format of the string is "{minutes} minutos y
        {seconds} segundos".
        """
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
        """
        The function calculates the total time, stopped time, movement time, and bills for a trip based
        on the time history and ticket prices.
        :return: The function `end_travel` is returning an instance of the `DataTrip` class, which
        contains information about the total time, total stopped time, total movement time, and the bill
        for the stopped time, movement time, and total trip.
        """
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
