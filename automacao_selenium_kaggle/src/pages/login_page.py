from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.kaggle.com/account/login"
    
    BUTTON_SING_IN_WITH_EMAIL = (By.XPATH, "//button[.//span[text()='Sign in with Email']]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SIGNIN_BUTTON = (By.XPATH, "//button[.//span[text()='Sign In']]")

    def login(self, email, password):
        self.logger.info("Abrindo página de login do Kaggle")
        self.driver.get(self.URL)

        if self.check_element_visible(self.BUTTON_SING_IN_WITH_EMAIL, "Botão de login com Email"):
            self.click(self.BUTTON_SING_IN_WITH_EMAIL, "Botão de login com Email")
            self.write(self.EMAIL_INPUT, email, "Campo de email")
            self.click(self.SIGNIN_BUTTON, "Botão de Sign In")
            self.write(self.PASSWORD_INPUT, password, "Campo de senha")
            self.click(self.SIGNIN_BUTTON, "Botão de Sign In")
        else:
            self.logger.info("Usuário já logado")
