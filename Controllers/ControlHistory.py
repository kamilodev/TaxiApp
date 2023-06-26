import os
import json
import time
import logging
from Controllers.AuxFunctions import clear_screen
from config_logger import setup_logger

logger = setup_logger()


def control_history(action: str):
    """
    The function `control_history` takes a string parameter `action` and either prints "borrando
    historico" if `action` is "delete" or "mostrando" if `action` is "show".

    :param action: a string that represents the action to be performed on the control history. It can be
    either "delete" or "show"
    """
    clear_screen()
    logger.info(f"Executing control_history with action: {action}")

    if not os.path.isfile("history.json"):
        clear_screen()
        logger.info("No existe historico")
        time.sleep(2)
        clear_screen()
    else:
        if action == "delete":
            confirmation = input(
                "¿Está seguro que desea eliminar el archivo de historial? (s/n): "
            )
            logger.info(f"User confirmation for file deletion: {confirmation}")
            if confirmation.lower() == "s":
                os.remove("history.json")
                logger.info("Archivo eliminado")
            else:
                logger.info("Eliminacion abortada")
        elif action == "show":
            show()
        input("Presione Enter para continuar")
        os.system("cls" if os.name == "nt" else "clear")


def show():
    current_directory = os.path.abspath(os.getcwd())
    file_path = os.path.join(current_directory, "history.json")
    with open(file_path, "r") as file:
        data = json.load(file)

    logger.info("Displaying trip history")
    for index, record in enumerate(data, 1):
        logger.info(f"Trip number: {index}")
        stop_time = record["total_stopped_time"]
        move_time = record["total_movement_time"]
        total_time = record["total_time"]
        bill_stop = record["total_bill_stop"]
        bill_move = record["total_bill_move"]
        bill_total = record["total_bill_total"]
        print("_" * 30)
        print(
            f"\n🏁 Viaje numero {index} 🏁\n\n"
            f"Tiempo total             : {total_time}\n"
            f"Tiempo detenido          : {stop_time} \n"
            f"Tiempo en movimiento     : {move_time} \n"
            f"Tarifa en reposo         : {bill_stop}€\n"
            f"Tarifa en movimiento     : {bill_move}€\n"
            f"Total a pagar            : {bill_total}€"
        )
        print("_" * 30)
