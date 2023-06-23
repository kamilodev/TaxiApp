#!/usr/bin/env python

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
            "email": "Ingrese su email: ",
            "password": "Ingrese su contraseña: ",
            "register": "Bienvenido, registre un nuevo usuario:",
            "success": "Inicio de sesión exitoso.",
            "error": "Error de autenticación. Por favor, inténtelo nuevamente.",
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

        self.config["users"].append({"email": email, "password": hashed_password})
        save_config(self.config)

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


if __name__ == "__main__":
    auth = LoginAuth()
    auth.login_or_register()
