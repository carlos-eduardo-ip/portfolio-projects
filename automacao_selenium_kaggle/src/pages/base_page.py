from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ..common.logger import Logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.wait = WebDriverWait(self.driver, 10)
        self.wait_short = WebDriverWait(self.driver, 5)

    def click(self, locator:tuple, element_name:str=""):
        self.logger.info(f"Clicando no elemento: {element_name}")
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            self.logger.error(f"Erro ao clicar no elemento: {element_name}")
            self.hover(locator, element_name)
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            raise e

    def write(self, locator:tuple, text:str, element_name:str=""):
        self.logger.info(f"Escrevendo no elemento: {element_name}")
        try:
            self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)
        except Exception as e:
            self.logger.error(f"Erro ao escrever no elemento: {e}")
            raise e

    def check_element_visible(self, locator:tuple, element_name:str=""):
        self.logger.info(f"Verificando elemento: {element_name}")
        return len(self.driver.find_elements(*locator)) > 0

    def check_element_not_visible(self, locator:tuple, element_name:str=""):
        self.logger.info(f"Verificando elemento: {element_name}")
        return len(self.driver.find_elements(*locator)) == 0

    def hover(self, locator:tuple, element_name:str=""):
        self.logger.info(f"Movendo mouse para o elemento: {element_name}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
