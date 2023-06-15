class Print_Values:
    def __init__(self):
        self.total_price = 0

    def show_info(self, stop_time, move_time, total_time):
        self.total_price = stop_time * 0.2 + move_time * 0.5

        print(f"\nFin de carrera!\nTiempo total: {round(total_time, 2)}")
        print(f"Tiempo detenido: {round(stop_time, 2)} segundos")
        print(f"Tiempo en movimiento: {round(move_time, 2)} segundos")
        print(f"\n\nTotal tarifa en reposo: {round(stop_time * 0.2, 2)}€")
        print(f"Total tarifa en movimiento: {round(move_time * 0.5, 2)}€")
        print(f"Total a pagar: {round(self.total_price, 2)}€")
