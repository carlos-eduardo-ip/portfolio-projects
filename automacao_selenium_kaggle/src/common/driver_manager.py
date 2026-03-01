from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverManager:
    def __init__(self, headless=False, user_data_dir=None, download_dir:str=None):
        self.driver = None
        self.download_dir = download_dir
        self.create_driver(headless, user_data_dir)
    
    def create_driver(self, headless=False, user_data_dir=None):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--lang=pt-BR")
        chrome_options.add_argument("--profile-directory=Default")
        
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": self.download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        
        if user_data_dir:
            chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
    