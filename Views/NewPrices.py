from Controllers.Prices import Prices
from Controllers.AuxFunctions import clear_screen
import time
from config_logger import setup_logger

logger = setup_logger()


# The NewPrices class prompts the user to input new stop and move prices, sets them using a method
# from another class, and prints a success or error message.
class NewPrices:
    def __init__(self):
        self.reset_prices = Prices()
        self.messages = {
            "new_stop": "👉 Introduce la nueva tarifa de parada: ",
            "new_move": "👉 Introduce la nueva tarifa de movimiento: ",
            "success": "👌 Tarifas actualizadas correctamente",
            "error": "🤙 Error al guardar los datos, intenta nuevamente",
        }

    def get_new_prices(self):
        """
        This function prompts the user to input new stop and move prices, sets them using a method from
        another class, and prints a success or error message.
        """
        clear_screen()

        try:
            stop = float(input(self.messages["new_stop"]))
            move = float(input(self.messages["new_move"]))
            self.reset_prices.set_new_prices(stop, move)
            print(self.messages["success"])
            logger.info(f"New prices set successfully")
            time.sleep(2)
            clear_screen()
        except:
            print(self.messages["error"])
            logger.warning(f"Error setting new prices")
            time.sleep(2)
            clear_screen()
