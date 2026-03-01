from selenium.webdriver.common.by import By
from .base_page import BasePage

class DatasetsPage(BasePage):
    URL = "https://www.kaggle.com/datasets"

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Search datasets']")
    DATASET_UBER = (By.CSS_SELECTOR, "a[aria-label='Uber Data Analytics Dashboard']")
    DATA_EXPLORER_CSV = (By.XPATH, "//p[contains(text(), '.csv')]")
    DOWNLOAD_BUTTON = (By.XPATH, "//span[@role='button' and @aria-label='Download']")

    def load_page(self):
        self.driver.get(self.URL)
    
    def search(self, query: str):
        self.write(self.SEARCH_INPUT, query, "Campo de busca")

    def click_dataset_uber(self):
        self.click(self.DATASET_UBER, "Dataset Uber")

    def click_data_explorer_csv(self):
        self.click(self.DATA_EXPLORER_CSV, "Arquivo .csv do Data Explorer")

    def click_download_button(self):
        self.click(self.DOWNLOAD_BUTTON, "Botão de download")