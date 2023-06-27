from Views.MainTaxi import MainTaxi
from Views.NewPrices import NewPrices
from Controllers.AuxFunctions import generate_pdf
from Views.Documentation import display_documentation
from Controllers.ControlHistory import control_history
from Controllers.AuxFunctions import clear_screen
from Controllers.DataBase import DataBase
from App import run_tests
from PyInquirer import prompt
import os


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
                    "Descargar el histórico de trayectos",
                    "Eliminar el histórico de trayectos",
                    "Actualizar la base de datos",
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
            control_history("show")
        elif answers["Options"] == "Descargar el histórico de trayectos":
            generate_pdf()
        elif answers["Options"] == "Eliminar el histórico de trayectos":
            control_history("delete")
        elif answers["Options"] == "Actualizar la base de datos":
            DataBase.update_history_to_mongo()
        elif answers["Options"] == "Realizar los tests":
            run_tests()
            clear_screen()
        elif answers["Options"] == "Ver la documentación":
            display_documentation()
        elif answers["Options"] == "Salir":
            os._exit(0)


if __name__ == "__main__":
    print_options()
