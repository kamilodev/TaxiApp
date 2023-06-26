import logging

logger = None


def setup_logger():
    global logger

    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        file_handler = logging.FileHandler("app.log")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
