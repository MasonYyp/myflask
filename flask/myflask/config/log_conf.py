import logging
from logging.handlers import RotatingFileHandler


def init_logs():
    # Set the level of logs
    logging.basicConfig(level=logging.DEBUG)

    # Create the logger, set size of logs and max number of logs
    file_log_handler = RotatingFileHandler("./logs/log", maxBytes=1024 * 1024, backupCount=10)

    # Set global for logs
    logging.getLogger().addHandler(file_log_handler)
