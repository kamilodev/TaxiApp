from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Controllers.AuxFunctions import clear_screen
from Views.PrintValues import show_info
from config_logger import setup_logger
import time
import json

logger = setup_logger()


class DataBase:
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
