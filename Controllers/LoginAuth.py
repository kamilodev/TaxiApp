from Views.Options import print_options
from Controllers.AuxFunctions import clear_screen
from config_manager import load_config, save_config
from config_logger import setup_logger
import getpass
import hashlib
import time

logger = setup_logger()


# The LoginAuth class provides methods for registering and authenticating users, as well as changing
# passwords.
class LoginAuth:
    def __init__(self):
        self.config = load_config()
        self.messages = {
            "email": "🙋‍♂️ Ingrese su usuario: ",
            "password": "🔐 Ingrese su contraseña: ",
            "change_password": "🔐 Ingrese su nueva contraseña:",
            "register": "😎 Bienvenido, registre un nuevo usuario 😎",
            "success": "\n🔥 Inicio de sesión exitoso.",
            "error": "\n👹 Error de autenticación. Por favor, inténtelo nuevamente.",
        }
        self.responses = {
            "register_ok": "💪 Usuario registrado correctamente!",
            "register_error": "👹 Error al crear el usuario",
            "change_password_ok": "💪 Contraseña actualizada correctamente!",
            "change_password_error": "👹 Error al actualizar la contraseña, intenta nuevamente",
        }

        clear_screen()

    def register_user(self):
        """
        This function registers a user by taking their email and password, hashing the password, and
        adding the user to a configuration file.
        """
        clear_screen()
        print(self.messages["register"])
        email = input(self.messages["email"])
        password = getpass.getpass(self.messages["password"])
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            self.config["users"].append({"email": email, "password": hashed_password})
            save_config(self.config)
            print(self.responses["register_ok"])
            logger.info(f"User {email} registered successfully")
            time.sleep(2)
        except:
            print(self.responses["register_error"])
            logger.warning(f"Error registering user {email}")
            time.sleep(2)
            clear_screen()
            self.register_user()

    def authenticate_user(self) -> bool:
        """
        This function authenticates a user
        :return: The function `authenticate_user` returns a boolean value (`True` or `False`).
        """
        clear_screen()
        email = input(self.messages["email"])
        password = getpass.getpass(self.messages["password"])

        users = self.config["users"]

        for user in users:
            if user["email"] == email:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if user["password"] == hashed_password:
                    return True
        return False

    def change_password(self):
        """
        This function allows a user to change their password by inputting their email, current password,
        and new password.
        """
        clear_screen()

        try:
            email = input(self.messages["email"])
            password = getpass.getpass(self.messages["password"])
            new_password = getpass.getpass(self.messages["change_password"])
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            new_hashed_password = hashlib.sha256(new_password.encode()).hexdigest()

            for user in self.config["users"]:
                if user["email"] == email and user["password"] == hashed_password:
                    user["password"] = new_hashed_password
                    save_config(self.config)
                    print(self.responses["change_password_ok"])
                    time.sleep(2)
                    clear_screen()
                    break
                else:
                    print(self.responses["change_password_error"])
                    time.sleep(2)
                    clear_screen()
        except:
            print(self.responses["change_password_error"])
            time.sleep(2)

    def login_or_register(self):
        """
        This function checks if there are any registered users and either registers a new user or
        authenticates an existing user.
        """
        if not self.config["users"]:
            self.register_user()

        while True:
            if self.authenticate_user():
                print(self.messages["success"])
                time.sleep(2)
                break
            else:
                print(self.messages["error"])
                time.sleep(2)

        print_options()
