#!/usr/bin/env python
from Views.Documentation import display_documentation
import sys
import subprocess


def run_tests():
    subprocess.run(["python", "-m", "pytest", "-v"])
    input("Presiona enter para continuar")


def main():
    from Controllers.LoginAuth import LoginAuth

    auth = LoginAuth()
    auth.login_or_register()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            display_documentation()
        if sys.argv[1] == "--test":
            run_tests()
        else:
            print("Argumento inválido")
