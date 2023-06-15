class Print_Values:
    def show_info(self, stop_time, move_time, total_time):
        print(f"Fin de carrera!\nEl tiempo ha sido de {total_time}")
        print(f"El tiempo estando parado fueron: {stop_time} segundos")
        print(f"El tiempo estando en movimiento fueron: {move_time} segundos")
