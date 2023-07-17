from selenium.webdriver.common.by import By
from base_page import BasePage


class ProfilePage(BasePage):
    def click_edit_profile_button(self):
        self.click_element(
            (
                By.XPATH,
                "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-profile/div/div[1]/button",
            )
        )

    def get_profile_name(self):
        return self.get_element_attribute(
            (By.XPATH, "//*[@id='editProfileName']"), "value"
        )

    def get_profile_last_name(self):
        return self.get_element_attribute(
            (By.XPATH, "//*[@id='editProfileLastName']"), "value"
        )

    def click_cancel_edit_profile_button(self):
        self.click_element(
            (
                By.XPATH,
                "/html/body/ngb-modal-window/div/div/app-edit-profile-modal/div[1]/button",
            )
        )
