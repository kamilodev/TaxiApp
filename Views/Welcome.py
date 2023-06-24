from art import text2art
from colorama import Fore, Style, init
from PIL import Image
import cv2
import numpy as np
import os
import shutil

init()
green = Fore.GREEN
cyan = Fore.CYAN
reset = Style.RESET_ALL
bold = "\033[1m"
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
        self.text_color = Fore.LIGHTBLUE_EX

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
        instructions = f"\nEl funcionamiento es básico, la App calculará el tiempo que el taxi permanezca detenido, como en un semáforo, o un atasco,\ny el tiempo que este en marcha durante el viaje."
        instructions += f"\n\nAl final te muestra un resumen de los tiempos, y el coste total a pagar"
        instructions += f"\n\nMandos:"
        instructions += f"\n⚙️ <Shift> Inicia / Detiene el viaje"
        instructions += f"\n⚙️ <Ctrl> En marcha / Detenerse"
        instructions += f"\n⚙️ <Esc> Regresa al menu principal"
        self.print_formatted_text(instructions, self.text_color)

        welcome_text = " 👉 Bienvenido, pulsa <Shift> para iniciar 👈 "
        line_width = shutil.get_terminal_size()[0]
        max_width = int(line_width * 0.98)
        if len(welcome_text) > max_width:
            max_width = len(welcome_text)
        centered_text = welcome_text.center(max_width, "-")
        print(f"{green}\n{centered_text}{reset}")

    def main_screen(self):
        welcome = Welcome()
        welcome.display_welcome_screen()
        self.display_title()
        self.display_instructions()
