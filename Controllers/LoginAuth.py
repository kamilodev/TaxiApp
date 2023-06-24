import getpass
import hashlib
import time
import os
from config_manager import load_config, save_config
from Views.Options import print_options


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

        self.clear_screen()

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def register_user(self):
        self.clear_screen()
        print(self.messages["register"])
        email = input(self.messages["email"])
        password = getpass.getpass(self.messages["password"])
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            self.config["users"].append({"email": email, "password": hashed_password})
            save_config(self.config)
            print(self.responses["register_ok"])
            time.sleep(2)
        except:
            print(self.responses["register_error"])
            time.sleep(2)
            self.clear_screen()
            self.register_user()

    def authenticate_user(self):
        self.clear_screen()
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
        self.clear_screen()
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
                    self.clear_screen()
                    break
                else:
                    print(self.responses["change_password_error"])
                    time.sleep(2)
                    self.clear_screen()
        except:
            print(self.responses["change_password_error"])
            time.sleep(2)

    def login_or_register(self):
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
