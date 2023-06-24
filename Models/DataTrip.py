import json
import os
from datetime import datetime
from pymongo import MongoClient
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time


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
        return json.dumps(data, indent=4)

    def save_history_to_file(self, json_data: str):
        if not os.path.isfile("history.json"):
            with open("history.json", "w") as file:
                file.write("[")
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

        with open("history.json", "a") as file:
            file.write("]")

    def save_history_to_mongo(self, json_data: str):
        try:
            client = MongoClient("mongodb://localhost:27017/")
            db = client["taxi"]
            collection = db["history"]

            if "taxi" not in client.list_database_names():
                db = client["taxi"]
                print("Base de datos 'taxi' creada")

            if "history" not in db.list_collection_names():
                collection = db["history"]
                print("Colección 'history' creada")

            data_to_insert = json.loads(json_data)

            collection.insert_one(data_to_insert)
            print("Historial guardado en la base de datos")
        except:
            print(f"Error al guardar en la base de datos")
            try:
                self.save_history_to_file(json_data)
                print("Guardado en el archivo local")
            except:
                print(f"Error al guardar en el archivo local")

    def update_history_to_mongo():
        with open("history.json", "r") as file:
            history_data = json.load(file)
        try:
            print("Conectando a la base de datos...\n")
            client = MongoClient("mongodb://localhost:27017/")
            db = client["taxi"]
            collection = db["history"]

            db_documents = list(collection.find({}, {"_id": 0}))

            for document in history_data:
                document_id = document["id"]
                if not any(doc["id"] == document_id for doc in db_documents):
                    collection.insert_one(document)
                    print("Agregando registro a la base de datos...")

            time.sleep(2)
            if all(
                any(doc["id"] == document["id"] for doc in db_documents)
                for document in history_data
            ):
                print("No se encontraron documentos faltantes en la base de datos.")
                time.sleep(2)
        except:
            print(f"No hay conexión a la base de datos")
            time.sleep(2)
