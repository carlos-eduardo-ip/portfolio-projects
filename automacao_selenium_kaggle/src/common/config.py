import os
from dotenv import load_dotenv
from pathlib import Path

# Carregar variáveis de ambiente
load_dotenv()

class Config:
    BASE_DIR = Path(__file__).resolve().parents[2]

    KAGGLE_USER = os.getenv("KAGGLE_USER")
    KAGGLE_PASSWORD = os.getenv("KAGGLE_PASSWORD")
    CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    USER_DATA_DIR = BASE_DIR / "data" / "user_data"
    DOWNLOAD_DIR = BASE_DIR / "data" / "downloads"
    LOGS_DIR = BASE_DIR / "logs"

    @classmethod
    def ensure_directories(cls):
        cls.USER_DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
        cls.LOGS_DIR.mkdir(parents=True, exist_ok=True)

config = Config()
config.ensure_directories()