import sys
import os
import time
from src.common.driver_manager import DriverManager
from src.common.config import config
from src.common.logger import Logger
from src.pages.login_page import LoginPage
from src.pages.datasets_page import DatasetsPage
from src.common.utils import wait_for_download
from src.services.data_analysis import DataAnalysisService

def main():
    logger = Logger.get_logger("selenium_kaggle", config.LOG_LEVEL)
    logger.info("Iniciando Automação - Selenium Kaggle")

    download_dir = config.DOWNLOAD_DIR
    driver_manager = DriverManager(headless=False, user_data_dir=config.USER_DATA_DIR, download_dir=str(download_dir))
    driver = driver_manager.get_driver()
    
    try:
        kaggle_page = LoginPage(driver)
        kaggle_page.login(config.KAGGLE_USER, config.KAGGLE_PASSWORD)
        time.sleep(2)
        
        datasets_page = DatasetsPage(driver)
        datasets_page.load_page()
        datasets_page.search("uber")
        datasets_page.click_dataset_uber()
        time.sleep(1)
        datasets_page.click_data_explorer_csv()
        time.sleep(1)
        datasets_page.click_download_button()
        time.sleep(1)
        
        logger.info(f"Aguardando download em: {download_dir}")
        
        if wait_for_download(download_dir):
            logger.info("Download concluído com sucesso!")
            files = sorted(download_dir.glob("*.csv"), key=os.path.getmtime, reverse=True)

            if files:
                analysis = DataAnalysisService()
                analysis.analyze_uber_data(files[0])
            else:
                logger.error("Nenhum arquivo CSV encontrado após download.")
        else:
            logger.error("Timeout aguardando o download.")

        logger.info("Processo finalizado com sucesso!")
        
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        sys.exit(1)
    finally:
        driver_manager.quit_driver()
        logger.info("Sistema encerrado.")

if __name__ == "__main__":
    main()
