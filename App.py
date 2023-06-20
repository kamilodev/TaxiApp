import inquirer
from Views import MainTaxi

questions = [
    inquirer.List(
        "options",
        choices=[
            "Iniciar el taximetro",
            "Cambiar la contraseña",
            "Cambia el precio de las tarifas",
            "Ver el historico de trayectos",
            "Eliminar el historico de trayectos",
            "Realiza los test",
            "Ver la documentación",
            "Salir",
        ],
        carousel=False,
    )
]

answers = inquirer.prompt(questions)

if answers["options"] == "Iniciar el taximetro":
    MainTaxi.main()

if __name__ == "__main__":
    while True:
        MainTaxi.main()