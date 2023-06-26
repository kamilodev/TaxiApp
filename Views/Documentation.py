from rich.console import Console
from rich.markdown import Markdown
from Controllers.AuxFunctions import clear_screen
from config_logger import setup_logger

logger = setup_logger()

console = Console()


def display_documentation():
    clear_screen()
    try:
        with open("./README.md", "r+") as help_file:
            markdown = Markdown(help_file.read())
            console.print(markdown)
            logger.info("User accessed the help file")
        input("\nPresione Enter para volver al menu principal")
        clear_screen()
    except FileNotFoundError:
        print("No se encontró el archivo de ayuda")
        logger.warning("Help file not found")
