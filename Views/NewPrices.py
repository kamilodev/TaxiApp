from Controllers.Prices import Prices
import time


class NewPrices:
    def __init__(self):
        self.reset_prices = Prices()

    def get_new_prices(self):
        stop = float(input("Introduce la nueva tarifa de parada: "))
        move = float(input("Introduce la nueva tarifa de movimiento: "))

        try:
            self.reset_prices.set_new_prices(stop, move)
            print("Tarifas actualizadas correctamente")
            time.sleep(2)
        except:
            print("Error al guardar los datos")
            time.sleep(2)
