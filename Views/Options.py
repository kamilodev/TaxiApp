from PyInquirer import prompt
import os


def print_options():
    os.system("cls" if os.name == "nt" else "clear")
    from Views.MainTaxi import MainTaxi

    questions = [
        {
            "type": "list",
            "name": "Options",
            "message": "Selecciona una opción",
            "choices": [
                "Iniciar el taximetro",
                "Cambiar la contraseña",
                "Cambia el precio de las tarifas",
                "Ver el historico de trayectos",
                "Eliminar el historico de trayectos",
                "Realiza los test",
                "Ver la documentación",
                "Salir",
            ],
        }
    ]

    answers = prompt(questions)
    if answers["Options"] == "Iniciar el taximetro":
        MainTaxi().main()
    elif answers["Options"] == "Cambiar la contraseña":
        print("Hey quieres cambiar la contraseña!")
    elif answers["Options"] == "Cambia el precio de las tarifas":
        print("Hey quieres cambiar el precio de las tarifas!")
    elif answers["Options"] == "Ver el historico de trayectos":
        print("Hey quieres ver el historico de trayectos!")
    elif answers["Options"] == "Eliminar el historico de trayectos":
        print("Hey quieres eliminar el historico de trayectos!")
    elif answers["Options"] == "Realiza los test":
        print("Hey quieres realizar los test!")
    elif answers["Options"] == "Ver la documentación":
        print("Hey quieres ver la documentación!")
    elif answers["Options"] == "Salir":
        return


if __name__ == "__main__":
    while True:
        print_options()
