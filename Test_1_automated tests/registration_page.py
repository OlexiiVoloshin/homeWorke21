from selenium.webdriver.common.by import By
from base_page import BasePage


class RegistrationPage(BasePage):
    def enter_name(self, name):
        self.enter_text((By.XPATH, "//input[@formcontrolname='name']"), name)

    def enter_last_name(self, last_name):
        self.enter_text((By.XPATH, "//input[@formcontrolname='lastName']"), last_name)

    def enter_email(self, email):
        self.enter_text((By.XPATH, "//input[@formcontrolname='email']"), email)

    def enter_password(self, password):
        self.enter_text((By.XPATH, "//input[@formcontrolname='password']"), password)

    def enter_repeat_password(self, password):
        self.enter_text(
            (By.XPATH, "//input[@formcontrolname='repeatPassword']"), password
        )

    def click_register_button(self):
        self.click_element((By.XPATH, "//button[contains(text(), 'Register')]"))
