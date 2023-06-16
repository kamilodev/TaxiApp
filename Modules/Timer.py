import time


class Timer:
    def __init__(self):
        self.starttime = time.time()
        self.lasttime = self.starttime
        self.lapnum = 0

    def history_timer(self):
        if self.lapnum == 0:
            self.lapnum += 1
            self.starttime = time.time()
            self.lasttime = self.starttime

        else:
            laptime = round((time.time() - self.lasttime), 2)

            totaltime = round((time.time() - self.starttime), 2)

            print("* " * 20)
            # Printing the lap number, lap-time, and total time
            print(f"Tramo {str(self.lapnum)}")
            if self.lapnum % 2 != 0:
                print(f"Tiempo tramo taxi detenido: {str(laptime)}")
            else:
                print(f"Tiempo tramo taxi en marcha: {str(laptime)}")
            print(f"Tiempo total: {str(totaltime)}")

            print("* " * 20)
            print("\n")

            # Updating the previous total time and lap number
            self.lasttime = time.time()
            self.lapnum += 1
            return laptime
