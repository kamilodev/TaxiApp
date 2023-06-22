import json

class PrintValues:
    def __init__(self):
        self.total_price = 0

    def get_last_trip(self):
        with open('history.json', 'r') as file:
            data = json.load(file)
            last_history = data[-1]
            return last_history

    def show_info(self):
        last_history = self.get_last_trip()

        stop_time = last_history['total_stopped_time']
        move_time = last_history['total_movement_time']
        total_time = last_history['total_time']
        bill_stop = last_history['total_bill_stop']
        bill_move = last_history['total_bill_move']
        bill_total = last_history['total_bill_total']

        print(
            f"\n🏁 Fin de carrera! 🏁\n⏱️ Tiempo total: {total_time}\n"
            f"\n⏱️ Tiempo detenido: {stop_time} segundos\n"
            f"⏱️ Tiempo en movimiento: {move_time} segundos\n\n"
            f"💶 Tarifa en reposo: {bill_stop}€\n"
            f"💶 Tarifa en movimiento: {bill_move}€\n"
            f"💶 Total a pagar: {bill_total}€"
        )


