from PyInquirer import prompt
from Views.MainTaxi import MainTaxi
from Views.NewPrices import NewPrices
from Controllers.ControlHistory import *
import os


def clear_screen():
    """
    The function clears the terminal screen in Python.
    """
    os.system("cls" if os.name == "nt" else "clear")


def print_options():
    """
    This function presents a menu of options to the user and performs different actions based on the
    user's selection.
    """
    from Controllers.LoginAuth import LoginAuth

    clear_screen()
    send_prices = NewPrices()
    change_password = LoginAuth()
    while True:
        questions = [
            {
                "type": "list",
                "name": "Options",
                "message": "Selecciona una opción",
                "choices": [
                    "Iniciar el taxímetro",
                    "Cambiar la contraseña",
                    "Cambiar el precio de las tarifas",
                    "Ver el histórico de trayectos",
                    "Eliminar el histórico de trayectos",
                    "Realizar los tests",
                    "Ver la documentación",
                    "Salir",
                ],
            }
        ]

        answers = prompt(questions)

        if answers["Options"] == "Iniciar el taxímetro":
            MainTaxi().main()
        elif answers["Options"] == "Cambiar la contraseña":
            change_password.change_password()
        elif answers["Options"] == "Cambiar el precio de las tarifas":
            send_prices.get_new_prices()
        elif answers["Options"] == "Ver el histórico de trayectos":
            clear_screen()
            control_history("show")
        elif answers["Options"] == "Eliminar el histórico de trayectos":
            clear_screen()
            control_history("delete")
        elif answers["Options"] == "Realizar los tests":
            pass
        elif answers["Options"] == "Ver la documentación":
            pass
        elif answers["Options"] == "Salir":
            os._exit(0)


if __name__ == "__main__":
    print_options()
