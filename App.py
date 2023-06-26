#!/usr/bin/env python
from Controllers.LoginAuth import LoginAuth
from Views.Documentation import display_documentation
import sys


def main():
    auth = LoginAuth()
    auth.login_or_register()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            display_documentation()
        else:
            print("Argumento inválido")
