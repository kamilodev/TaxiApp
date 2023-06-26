from Controllers.Fees import Fees
from config_logger import setup_logger
logger = setup_logger()

class ControlTravel:
    def __init__(self):
        self.send_fee = Fees()
        self.is_move = False
        self.is_new_travel = False
        self.counter = 0

    def toggle_fee(self):
        if self.is_move:
            self.send_fee.fee_stoped()
            logger.info("Vehículo detenido")
        else:
            self.send_fee.fee_movement()
            logger.info("Vehiculo en marcha")

    def new_travel_fee(self):
        if not self.is_new_travel:
            self.send_fee.init_end_move()
            self.is_new_travel = True
            logger.info("Viaje iniciado")
        else:
            data = self.send_fee.end_travel()
            json_data = data.data_to_json()
            data.save_history_to_mongo(json_data)
            logger.info("Viaje finalizado")
            return False
