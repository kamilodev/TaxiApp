import time


# The Timer class calculates and prints the elapsed time for each lap and the total time elapsed since
# the start of the timer.
class Timer:
    def __init__(self):
        self.starttime = time.time()
        self.lasttime = self.starttime
        self.lapnum = 0

    def history_timer(self) -> float:
        """
        This function calculates and prints the elapsed time for each lap and the total time elapsed
        since the start of the timer.
        :return: the laptime, which is the time elapsed since the last lap or since the start of the
        timer, depending on whether the lap is even or odd.
        """
        if self.lapnum == 0:
            self.lapnum += 1
            self.starttime = time.time()
            self.lasttime = self.starttime
        else:
            laptime = round((time.time() - self.lasttime), 2)

            totaltime = round((time.time() - self.starttime), 2)

            print("* " * 20)
            print(f"Tramo {str(self.lapnum)} 🚩")
            if self.lapnum % 2 != 0:
                print(f"Tiempo detenido: {str(laptime)}")
            else:
                print(f"Tiempo en marcha: {str(laptime)}")
            print(f"Tiempo acumulado: {str(totaltime)}")

            print("* " * 20)
            print("\n")

            self.lasttime = time.time()
            self.lapnum += 1
            return laptime
