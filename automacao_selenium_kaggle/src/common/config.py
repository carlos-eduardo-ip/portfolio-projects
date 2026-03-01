import os
from dotenv import load_dotenv
from pathlib import Path

# Carregar variáveis de ambiente
load_dotenv()

class Config:
    KAGGLE_USER = os.getenv("KAGGLE_USER")
    KAGGLE_PASSWORD = os.getenv("KAGGLE_PASSWORD")
    CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    USER_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "user_data"
    DOWNLOAD_DIR = Path(__file__).resolve().parents[2] / "data" / "downloads"

config = Config()
