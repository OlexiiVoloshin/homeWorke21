import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page import BasePage
from registration_page import RegistrationPage
from garage_page import GaragePage
from profile_page import ProfilePage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_qa_auto_workflow(driver):
    base_page = BasePage(driver)
    registration_page = RegistrationPage(driver)
    garage_page = GaragePage(driver)
    profile_page = ProfilePage(driver)

    driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    # Введення даних користувача
    base_page.click_element((By.XPATH, "//button[contains(text(), 'Sign up')]"))
    registration_page.enter_name("AVoloshin")
    registration_page.enter_last_name("VAlexey")
    registration_page.enter_email("dimasya@mail.cim")
    registration_page.enter_password("TTeerrii13")
    registration_page.enter_repeat_password("TTeerrii13")
    base_page.click_element((By.XPATH, "//button[contains(text(), 'Register')]"))

    # Додавання авто
    garage_page.click_add_car_button()
    garage_page.select_car_brand(2)
    garage_page.select_car_model(3)
    garage_page.enter_car_mileage("10")
    garage_page.click_save_car_button()

    # Додавання expenses до авто
    garage_page.click_element(
        (
            By.XPATH,
            "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div[1]/div[2]/button[2]",
        )
    )
    garage_page.enter_text((By.XPATH, "//*[@id='addExpenseMileage']"), "20")
    garage_page.enter_text((By.XPATH, "//*[@id='addExpenseLiters']"), "10")
    garage_page.enter_text((By.XPATH, "//*[@id='addExpenseTotalCost']"), "30")
    garage_page.click_element(
        (
            By.XPATH,
            "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]",
        )
    )

    # Перевірка даних на сторінці профайлу
    driver.get("https://guest:welcome2qauto@qauto.forstudy.space/panel/profile")
    profile_page.click_edit_profile_button()
    assert profile_page.get_profile_name() == "AVoloshin", "Profile Name mismatch"
    assert (
        profile_page.get_profile_last_name() == "VAlexey"
    ), "Profile Last Name mismatch"
    profile_page.click_cancel_edit_profile_button()

    # Видалення користувача
    driver.get("https://guest:welcome2qauto@qauto.forstudy.space/panel/settings")
    base_page.click_element(
        (
            By.XPATH,
            "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-settings/div/div[2]/div/div[5]/div/button",
        )
    )
    base_page.click_element(
        (
            By.XPATH,
            "/html/body/ngb-modal-window/div/div/app-remove-account-modal/div[3]/button[2]",
        )
    )
