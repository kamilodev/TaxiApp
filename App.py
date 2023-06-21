from Views import MainTaxi
from PyInquirer import prompt

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
    MainTaxi.main()
else:
    pass

if __name__ == "__main__":
    while True:
        MainTaxi.main()
