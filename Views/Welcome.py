from art import text2art
import os
from colorama import Fore, Style, init
import cv2
from PIL import Image
import numpy as np
import shutil

init()
green = Fore.GREEN
cyan = Fore.CYAN
reset = Style.RESET_ALL
bold = '\033[1m'
underline = "\033[4m"


class Welcome:
    def __init__(self):
        self.image_path = "taxi.jpg"

    def display_image(self):
        try:
            image = Image.open(self.image_path)
            image_np = np.array(image)
            terminal_size = (80, 24)
            resized_image = cv2.resize(image_np, terminal_size)
            pixels = resized_image.tolist()

            for row in pixels:
                for pixel in row:
                    r, g, b = pixel
                    print(f"\033[48;2;{r};{g};{b}m \033[0m", end="")
                print()

        except IOError:
            print("No se pudo abrir la imagen.")

    def display_welcome_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
        result = text2art("TaxiApp", font="bulbhead")

        print(f"{cyan}{result}{reset}")
        self.display_image()


class AppInstructions:
    def __init__(self):
        self.title_color = cyan
        self.text_color = Fore.LIGHTRED_EX

    def print_formatted_text(self, text, color):
        print(f"\n{color}{text}{reset}")

    def display_title(self):
        self.print_formatted_text(
            f"\n🌟 TaxiApp es un taxímetro que calcula el precio final de una carrera, teniendo en cuenta dos tarifas: 🌟",
            green,
        )
        self.print_formatted_text(
            "Una para cuando el vehículo está en movimiento y otra para cuando está detenido.",
            self.title_color,
        )

    def display_instructions(self):
        print(f"\n{bold}{underline}Instrucciones:{reset}\n")
        instructions = f"\n✅ Para iniciar una carrera, presiona la tecla 'Enter'. En este momento, la aplicación comenzará a calcular el precio con la tarifa de 'detenido'."
        instructions += f"\n\n✅ Cada vez que el vehículo se ponga en movimiento, presiona la tecla 'Espacio' y calculará con la tarifa 'en movimiento'."
        instructions += f"\n\n✅ Cuando el vehículo se detenga, presiona nuevamente la tecla 'Espacio'. La aplicación se detendrá y calculará el precio utilizando la tarifa de 'detenido'."
        instructions += f"\n\n✅ Para finalizar la carrera, presiona la tecla 'Enter'. La aplicación mostrará en pantalla el total a pagar en euros."
        instructions += f"\n\n✅ La aplicación quedará en espera, lista para iniciar una nueva carrera cuando se presione nuevamente la tecla 'Enter'."
        self.print_formatted_text(instructions, self.text_color)

        welcome_text = " 👉 Bienvenido, pulse Enter para ingresar 👈 "
        line_width = shutil.get_terminal_size()[0]
        max_width = int(line_width * 0.98)
        if len(welcome_text) > max_width:
            max_width = len(welcome_text)
        centered_text = welcome_text.center(max_width, "-")
        print(f"{green}\n{centered_text}{reset}")

    def again(self):
        user_input = input("Pulsa Enter para calcular otro viaje")
        if user_input == "":
            pass
        else:
            return False

    def main_screen(self):
        welcome = Welcome()
        welcome.display_welcome_screen()
        self.display_title()
        self.display_instructions()
