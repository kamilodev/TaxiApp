#!/usr/bin/env python
from Controllers.LoginAuth import LoginAuth


def main():
    auth = LoginAuth()
    auth.login_or_register()


if __name__ == "__main__":
    main()
