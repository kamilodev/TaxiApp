import json
import os
import time
from Views.PrintValues import PrintValues


def control_history(action: str):
    """
    This function checks if a history file exists and performs an action based on the input, either
    deleting or showing the history.

    :param action: a string parameter that specifies the action to be performed on the history. It can
    be either "delete" to delete the history or "show" to display the history
    :type action: str
    """
    if not os.path.isfile("history.json"):
        print("No existe historico")
    else:
        if action == "delete":
            delete()
        elif action == "show":
            show()
        input("Presione Enter para continuar")
        os.system("cls" if os.name == "nt" else "clear")


def delete():
    """
    This Python function prompts the user for confirmation before deleting a file and prints a message
    indicating whether the file was deleted or not.
    """
    confirmation = input(
        "¿Está seguro que desea eliminar el archivo de historial? (s/n): "
    )
    if confirmation.lower() == "s":
        os.remove("history.json")
        print("Archivo eliminado")
    else:
        print("Eliminacion abortada")


def show():
    """
    The function reads data from a JSON file with the history and prints a formatted summary of each record.
    """
    current_directory = os.path.abspath(os.getcwd())
    file_path = os.path.join(current_directory, "history.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    for index, record in enumerate(data, 1):
        print("_" * 30)
        stop_time = record["total_stopped_time"]
        move_time = record["total_movement_time"]
        total_time = record["total_time"]
        bill_stop = record["total_bill_stop"]
        bill_move = record["total_bill_move"]
        bill_total = record["total_bill_total"]
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
