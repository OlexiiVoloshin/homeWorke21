from selenium.webdriver.common.by import By
from base_page import BasePage


class GaragePage(BasePage):
    def click_add_car_button(self):
        self.click_element(
            (
                By.XPATH,
                "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button",
            )
        )

    def select_car_brand(self, option_number):
        locator = (By.XPATH, f"//*[@id='addCarBrand']/option[{option_number}]")
        self.click_element(locator)

    def select_car_model(self, option_number):
        locator = (By.XPATH, f"//*[@id='addCarModel']/option[{option_number}]")
        self.click_element(locator)

    def enter_car_mileage(self, mileage):
        self.enter_text((By.XPATH, "//*[@id='addCarMileage']"), mileage)

    def click_save_car_button(self):
        self.click_element(
            (
                By.XPATH,
                "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]",
            )
        )
