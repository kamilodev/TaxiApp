import os
from PyInquirer import prompt
from Views.MainTaxi import MainTaxi
from Views.NewPrices import NewPrices
from Controllers.ControlHistory import control_history


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_options():
    send_prices = NewPrices()
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
            print("¡Hey, quieres cambiar la contraseña!")
        elif answers["Options"] == "Cambiar el precio de las tarifas":
            clear_screen()
            send_prices.get_new_prices()
            clear_screen()
        elif answers["Options"] == "Ver el histórico de trayectos":
            clear_screen()
            control_history("show")
        elif answers["Options"] == "Eliminar el histórico de trayectos":
            clear_screen()
            control_history("delete")
        elif answers["Options"] == "Realizar los tests":
            print("¡Hey, quieres realizar los tests!")
        elif answers["Options"] == "Ver la documentación":
            print("¡Hey, quieres ver la documentación!")
        elif answers["Options"] == "Salir":
            os._exit(0)


if __name__ == "__main__":
    print_options()
