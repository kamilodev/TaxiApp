def show_info(data):
    stop_time = data["total_stopped_time"]
    move_time = data["total_movement_time"]
    total_time = data["total_time"]
    bill_stop = data["total_bill_stop"]
    bill_move = data["total_bill_move"]
    bill_total = data["total_bill_total"]

    print(
        f"\n🏁 Fin de carrera! 🏁\n⏱️ Tiempo total: {total_time}\n"
        f"\n⏱️ Tiempo detenido: {stop_time}\n"
        f"⏱️ Tiempo en movimiento: {move_time}\n\n"
        f"💶 Tarifa en reposo: {bill_stop}€\n"
        f"💶 Tarifa en movimiento: {bill_move}€\n"
        f"💶 Total a pagar: {bill_total}€"
    )
