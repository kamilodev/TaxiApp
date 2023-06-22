from Views import Options

class App:
    def __init__(self):
        self.auth = True

    def run(self):
        if self.auth == False:
            input("Presiona Enter para ingresar...")
            Options.print_options()
        else:
            Options.print_options()


if __name__ == "__main__":
    app = App()
    app.run()
