from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from config_logger import setup_logger
import json
import os
import time

logger = setup_logger()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def generate_pdf():
    clear_screen()
    try:
        with open("history.json", "r") as file:
            history_data = json.load(file)
            logger.info("History loaded from file")

        c = canvas.Canvas("historico.pdf", pagesize=letter)
        c.setFont("Helvetica", 12)

        registros_por_pagina = 3
        y = 700

        registros_en_pagina = 0

        for document in history_data:
            id = document["id"]
            date = document["today"]
            total_time = document["total_time"]
            stop_time = document["total_stopped_time"]
            move_time = document["total_movement_time"]
            bill_stop = document["total_bill_stop"]
            bill_move = document["total_bill_move"]
            bill_total = document["total_bill_total"]

            c.drawString(100, y - 20, f"Id de operacion: {id}")
            c.drawString(100, y - 40, f"Fecha de registro: {date}")
            c.drawString(100, y - 70, f"Tiempo total: {total_time}")
            c.drawString(100, y - 90, f"Tiempo detenido: {stop_time}")
            c.drawString(100, y - 110, f"Tiempo en movimiento: {move_time}")
            c.drawString(100, y - 150, f"Tarifa en reposo: {bill_stop}€")
            c.drawString(100, y - 170, f"Tarifa en movimiento: {bill_move}€")
            c.drawString(100, y - 190, f"Total a pagar: {bill_total}€")
            c.drawString(100, y - 210, f"-" * 100)

            y -= 220

            registros_en_pagina += 1

            if registros_en_pagina == registros_por_pagina:
                c.showPage()

                registros_en_pagina = 0

                y = 700

        c.save()
        print("Archivo PDF generado con éxito")
        logger.info("PDF file generated successfully")
        time.sleep(2)
        clear_screen()
    except:
        print("Aun no hay ningun registro en el historial")
        logger.warning("No records in history when generating PDF")
        time.sleep(2)
        clear_screen()
