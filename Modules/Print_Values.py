#from Modules.Reset import Reset
import json

class Print_Values:
    def __init__(self):
        self.total_price = 0

    def read_last_history_from_file(self):
        with open('history.json', 'r') as file:
            data = json.load(file)
            last_history = data[-1]
            return last_history

    def show_info(self):
        last_history = self.read_last_history_from_file()

        stop_time = last_history['total_stopped_time']
        move_time = last_history['total_movement_time']
        total_time = last_history['total_time']
        bill_stop = last_history['total_bill_stop']
        bill_move = last_history['total_bill_move']
        bill_total = last_history['total_bill_total']

        print(f"\nFin de carrera!\nTiempo total: {total_time}")
        print(f"Tiempo detenido: {stop_time} segundos")
        print(f"Tiempo en movimiento: {move_time} segundos")
        print(f"\n\nTotal tarifa en reposo: {bill_stop}€")
        print(f"Total tarifa en movimiento: {bill_move}€")
        print(f"Total a pagar: {bill_total}€")
