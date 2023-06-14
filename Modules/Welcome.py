from art import text2art
import os
from colored import fg, bg, attr

# Definir colores
red = fg("red")
green = fg("green")
yellow = fg("yellow")
reset = attr("reset")


class Welcome:
    def display_welcome_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
        result = text2art("TaxiApp", font="small")
        print(f"{yellow}{result}")
        print(f"{green}Bienvenido, pulse Enter para ingresar{reset}")
