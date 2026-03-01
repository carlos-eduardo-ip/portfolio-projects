import logging
import os
from datetime import datetime

class Logger:
    @staticmethod
    def get_logger(name: str, level: str = "INFO"):
        logger = logging.getLogger(name)
        if not logger.handlers:
            if not os.path.exists('logs'):
                os.makedirs('logs')
            
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            log_filename = f"logs/{name}_{datetime.now().strftime('%Y-%m-%d')}.log"
            file_handler = logging.FileHandler(log_filename)
            file_handler.setFormatter(formatter)
            logger.setLevel(logging.getLevelName(level))
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
        return logger
