from Controllers.Prices import Prices
import time
import os


# The NewPrices class prompts the user to input new stop and move prices, sets them using a method
# from another class, and prints a success or error message.
class NewPrices:
    def __init__(self):
        self.reset_prices = Prices()
        self.messages = {
            "new_stop": "👉 Introduce la nueva tarifa de parada: ",
            "new_move": "👉 Introduce la nueva tarifa de movimiento: ",
            "success": "👌 Tarifas actualizadas correctamente",
            "error": "🤙 Error al guardar los datos",
        }

    def clear_screen():
        """
        The function clears the terminal screen in Python.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def get_new_prices(self):
        """
        This function prompts the user to input new stop and move prices, sets them using a method from
        another class, and prints a success or error message.
        """
        NewPrices.clear_screen()
        stop = float(input(self.messages["new_stop"]))
        move = float(input(self.messages["new_move"]))

        try:
            self.reset_prices.set_new_prices(stop, move)
            print(self.messages["success"])
            time.sleep(2)
            NewPrices.clear_screen()
        except:
            print(self.messages["error"])
            time.sleep(2)
            self.clear_screen()
