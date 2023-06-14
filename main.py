#!/usr/bin/python3
from Modules.Welcome import Welcome
from Modules.Control_Keys import Control_Keys


def main():
    welcome = Welcome()
    control_keys = Control_Keys()
    welcome.display_welcome_screen()
    control_keys.run()


if __name__ == "__main__":
    main()
