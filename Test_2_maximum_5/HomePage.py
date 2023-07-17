from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Локатори
        self.guest_button = (
            By.XPATH,
            "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[1]",
        )
        self.add_car_button = (
            By.XPATH,
            "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button",
        )
        self.car_brand_option = (By.XPATH, "//*[@id='addCarBrand']/option[1]")
        self.car_model_option = (By.XPATH, "//*[@id='addCarModel']/option[1]")
        self.mileage_input = (By.XPATH, "//*[@id='addCarMileage']")
        self.save_button = (
            By.XPATH,
            "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]",
        )

    def click_guest_button(self):
        self.wait.until(EC.element_to_be_clickable(self.guest_button)).click()

    def click_add_car_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_car_button)).click()

    def select_car_brand(self):
        self.wait.until(EC.element_to_be_clickable(self.car_brand_option)).click()

    def select_car_model(self):
        self.wait.until(EC.element_to_be_clickable(self.car_model_option)).click()

    def enter_mileage(self, mileage):
        mileage_input = self.wait.until(
            EC.visibility_of_element_located(self.mileage_input)
        )
        mileage_input.send_keys(mileage)

    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()
