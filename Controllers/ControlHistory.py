import json
import os
import time
from Controllers.AuxFunctions import clear_screen
from config_logger import setup_logger

logger = setup_logger()


def control_history(action: str):
    """
    This function checks if a history file exists and performs an action based on the input, either
    deleting or showing the history.

    :param action: a string parameter that specifies the action to be performed on the history. It can
    be either "delete" to delete the history or "show" to display the history
    :type action: str
    """
    clear_screen()
    logger.info(f"User access control_history with action: {action}")

    if not os.path.isfile("history.json"):
        clear_screen()
        print("No existe historico")
        logger.info("Try to view history but it does not exist")
        time.sleep(2)
        clear_screen()
    else:
        if action == "delete":
            delete()
        elif action == "show":
            show()
        input("Presione Enter para continuar")
        clear_screen()


def delete():
    """
    This Python function prompts the user for confirmation before deleting a file and prints a message
    indicating whether the file was deleted or not.
    """
    confirmation = input(
        "¿Está seguro que desea eliminar el archivo de historial? (s/n): "
    )
    logger.info(f"User confirmation for file deletion: {confirmation}")
    if confirmation.lower() == "s":
        os.remove("history.json")
        print("Archivo eliminado")
        logger.info("History file deleted")
    else:
        print("Eliminacion abortada")
        logger.info("History file deletion aborted")


def show():
    """
    The function reads data from a JSON file with the history and prints a formatted summary of each record.
    """
    current_directory = os.path.abspath(os.getcwd())
    file_path = os.path.join(current_directory, "history.json")
    with open(file_path, "r") as file:
        data = json.load(file)

    logger.info("Displaying trip history")
    for index, record in enumerate(data, 1):
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
