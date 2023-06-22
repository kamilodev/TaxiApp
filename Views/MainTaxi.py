#!/usr/bin/python3
from Controllers.Navigate import Navigate
from Views.Welcome import AppInstructions
import warnings, sys


class MainTaxi:
    def main(self):
        while True:
            welcome = AppInstructions()
            navigate = Navigate()

            welcome.main_screen()
            with open("../warnings.log", "w") as f:
                warnings.filterwarnings("always")
                warnings.showwarning = lambda *args, **kwargs: None
                sys.stderr = f

                navigate.run()

            sys.stderr = sys.__stderr__

if __name__ == "__main__":
    main_taxi = MainTaxi()
    main_taxi.main()
