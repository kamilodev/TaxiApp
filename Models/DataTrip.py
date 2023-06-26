from Views.PrintValues import show_info
from Controllers.AuxFunctions import clear_screen
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from config_logger import setup_logger
import json
import os
import time

logger = setup_logger()


class DataTrip:
    def __init__(
        self, total_time, stop_time, move_time, bill_stop, bill_move, bill_total
    ):
        self.total_time = total_time
        self.stop_time = stop_time
        self.move_time = move_time
        self.bill_stop = bill_stop
        self.bill_move = bill_move
        self.bill_total = bill_total
        self.today = datetime.now().strftime("%d-%m-%Y")
        self.hour = datetime.now().strftime("%H:%M")
        self.id = id(self.hour)

    def data_to_json(self):
        """
        This function converts data attributes into a JSON format and returns it as a string.
        :return: The method `data_to_json` returns a JSON string representation of a dictionary
        containing various data attributes.
        """
        data = {
            "id": self.id,
            "today": self.today,
            "hour": self.hour,
            "total_time": self.total_time,
            "total_stopped_time": self.stop_time,
            "total_movement_time": self.move_time,
            "total_bill_stop": self.bill_stop,
            "total_bill_move": self.bill_move,
            "total_bill_total": self.bill_total,
        }
        logger.info("Data converted to JSON")
        return json.dumps(data, indent=4)

    def save_history_to_file(self, json_data: str):
        """
        This function saves JSON data to a file named "history.json" and ensures that the file contains
        valid JSON format.

        :param json_data: A string containing JSON-formatted data to be saved to a file
        :type json_data: str
        """
        if not os.path.isfile("history.json"):
            with open("history.json", "w") as file:
                file.write("[")
                logger.info("File 'history.json' created")
        else:
            with open("history.json", "r") as file:
                content = file.read().strip()

            if content.endswith("],"):
                content = content[:-2]
            elif content.endswith("]"):
                content = content[:-1]

            with open("history.json", "w") as file:
                file.write(content)

        with open("history.json", "a") as file:
            if os.stat("history.json").st_size > 1:
                file.write(",")
            file.write(json_data)
            logger.info("Data saved to file 'history.json'")

        with open("history.json", "a") as file:
            file.write("]")

    def save_history_to_mongo(self, json_data: str):
        data_to_insert = json.loads(json_data)
        try:
            client = MongoClient(
                "mongodb://localhost:27017/", serverSelectionTimeoutMS=5000
            )
            db = client["taxi"]
            collection = db["history"]

            if "taxi" not in client.list_database_names():
                db = client["taxi"]
                print("Base de datos 'taxi' creada")
                logger.info("Database 'taxi' created")

            if "history" not in db.list_collection_names():
                collection = db["history"]
                print("Colección 'history' creada")
                logger.info("Collection 'history' created")

            collection.insert_one(data_to_insert)
            print("Historial guardado en la base de datos")
            logger.info("History saved to database")
            show_info(data_to_insert)
        except ServerSelectionTimeoutError:
            print(f"Error al guardar en la base de datos")
            logger.warning("Error saving to database")
            try:
                self.save_history_to_file(json_data)
                print("Guardado en el archivo local")
                show_info(data_to_insert)
                logger.info("Saved to local file")
            except:
                print(f"Error al guardar en el archivo local")

    def update_history_to_mongo():
        try:
            clear_screen()
            with open("history.json", "r") as file:
                history_data = json.load(file)
            try:
                print("Conectando a la base de datos...\n")
                client = MongoClient(
                    "mongodb://localhost:27017/", serverSelectionTimeoutMS=5000
                )
                db = client["taxi"]
                collection = db["history"]

                db_documents = list(collection.find({}, {"_id": 0}))

                for document in history_data:
                    document_id = document["id"]
                    if not any(doc["id"] == document_id for doc in db_documents):
                        collection.insert_one(document)
                        print("Agregando registro a la base de datos...")
                        logger.info("Adding record to database")

                time.sleep(2)
                if all(
                    any(doc["id"] == document["id"] for doc in db_documents)
                    for document in history_data
                ):
                    print("No se encontraron documentos faltantes en la base de datos.")
                    logger.info("No missing documents found in database")
                    time.sleep(2)
            except ServerSelectionTimeoutError:
                print(f"No hay conexión a la base de datos")
                logger.warning("No connection to database when try to update")
                time.sleep(2)
        except:
            print("Aun no hay ningun registro en el historial")
            logger.warning("No records in history")
            time.sleep(2)
        clear_screen()

    def generate_pdf():
        clear_screen()
        try:
            with open("history.json", "r") as file:
                history_data = json.load(file)
                logger.info("History loaded from file")

            # Crear un nuevo archivo PDF
            c = canvas.Canvas("historico.pdf", pagesize=letter)

            # Definir el formato y el tamaño de la fuente
            c.setFont("Helvetica", 12)

            # Número de registros por página
            registros_por_pagina = 3

            # Posición vertical inicial
            y = 700

            # Contador de registros en la página actual
            registros_en_pagina = 0

            # Iterar sobre los documentos del historial
            for document in history_data:
                id = document["id"]
                date = document["today"]
                total_time = document["total_time"]
                stop_time = document["total_stopped_time"]
                move_time = document["total_movement_time"]
                bill_stop = document["total_bill_stop"]
                bill_move = document["total_bill_move"]
                bill_total = document["total_bill_total"]

                # Agregar la información formateada al archivo PDF
                c.drawString(100, y - 20, f"Id de operacion: {id}")
                c.drawString(100, y - 40, f"Fecha de registro: {date}")
                c.drawString(100, y - 70, f"Tiempo total: {total_time}")
                c.drawString(100, y - 90, f"Tiempo detenido: {stop_time}")
                c.drawString(100, y - 110, f"Tiempo en movimiento: {move_time}")
                c.drawString(100, y - 150, f"Tarifa en reposo: {bill_stop}€")
                c.drawString(100, y - 170, f"Tarifa en movimiento: {bill_move}€")
                c.drawString(100, y - 190, f"Total a pagar: {bill_total}€")
                c.drawString(100, y - 210, f"-" * 100)

                # Actualizar la posición vertical
                y -= 220

                # Incrementar el contador de registros en la página actual
                registros_en_pagina += 1

                # Comprobar si se ha alcanzado el límite de registros por página
                if registros_en_pagina == registros_por_pagina:
                    c.showPage()
                    # Reiniciar el contador de registros en la página actual
                    registros_en_pagina = 0
                    # Reiniciar la posición vertical para la siguiente página
                    y = 700

            # Guardar el archivo PDF y cerrar el lienzo
            c.save()
            print("Archivo PDF generado con éxito")
            logger.info("PDF file generated successfully")
            time.sleep(2)
            clear_screen()
        except:
            print("Aun no hay ningun registro en el historial")
            logger.warning("No records in history when generating PDF")
            time.sleep(2)
            clear_screen()
