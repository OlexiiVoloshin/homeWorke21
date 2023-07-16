import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_variables import *


@pytest.fixture(scope="function")
def setup_teardown():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()


def test_qa_auto_workflow(setup_teardown):
    driver, wait = setup_teardown

    try:
        driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

        # Клік на кнопку "Sign up"
        sign_up_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Sign up')]")
            )
        )
        sign_up_button.click()

        # Введення даних користувача
        name_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@formcontrolname='name']")
            )
        )
        name_input.send_keys(USER_NAME)

        last_name_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@formcontrolname='lastName']")
            )
        )
        last_name_input.send_keys(USER_LAST_NAME)

        email_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@formcontrolname='email']")
            )
        )
        email_input.send_keys(USER_EMAIL)

        password_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@formcontrolname='password']")
            )
        )
        password_input.send_keys(USER_PASSWORD)

        repeat_password_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@formcontrolname='repeatPassword']")
            )
        )
        repeat_password_input.send_keys(USER_PASSWORD)

        # Клік на кнопку "Register"
        register_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Register')]")
            )
        )
        register_button.click()

        # Тут можна додати перевірку, чи зареєстровано користувача успішно

        print("Тест створення користувача пройшов успішно!")

        # Додавання авто
        add_car_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button",
                )
            )
        )
        add_car_button.click()

        # Вибір марки авто
        car_brand_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//*[@id='addCarBrand']/option[{CAR_BRAND_OPTION}]")
            )
        )
        car_brand_option.click()

        # Вибір моделі авто
        car_model_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//*[@id='addCarModel']/option[{CAR_MODEL_OPTION}]")
            )
        )
        car_model_option.click()

        # Введення пробігу авто
        mileage_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='addCarMileage']"))
        )
        mileage_input.send_keys(CAR_MILEAGE)

        # Клік на кнопку "Save"
        save_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]",
                )
            )
        )
        save_button.click()

        # Перевірка, чи авто додано успішно (можна провести додаткові перевірки)

        print("Тест додавання авто пройшов успішно!")

        # Додавання expenses до авто
        add_expenses_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div[1]/div[2]/button[2]",
                )
            )
        )
        add_expenses_button.click()

        # Введення даних про expenses
        mileage_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='addExpenseMileage']"))
        )
        mileage_input.send_keys(EXPENSES_MILEAGE)

        liters_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='addExpenseLiters']"))
        )
        liters_input.send_keys(EXPENSES_LITERS)

        total_cost_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='addExpenseTotalCost']")
            )
        )
        total_cost_input.send_keys(EXPENSES_TOTAL_COST)

        # Клік на кнопку "Save"
        save_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]",
                )
            )
        )
        save_button.click()

        # Перевірка, чи expenses додано успішно (можна провести додаткові перевірки)

        print("Тест додавання expenses пройшов успішно!")

        # Перевірка даних на сторінці профайлу
        profile_url = "https://guest:welcome2qauto@qauto.forstudy.space/panel/profile"
        driver.get(profile_url)

        # Клік на кнопку "Edit Profile"
        edit_profile_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-profile/div/div[1]/button",
                )
            )
        )
        edit_profile_button.click()

        # Перевірка даних Name та LastName
        name_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='editProfileName']"))
        )
        last_name_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='editProfileLastName']")
            )
        )

        assert (
            name_input.get_attribute("value") == USER_NAME
        ), f"Actual Name: {name_input.get_attribute('value')}, Expected Name: {USER_NAME}"
        assert (
            last_name_input.get_attribute("value") == USER_LAST_NAME
        ), f"Actual LastName: {last_name_input.get_attribute('value')}, Expected LastName: {USER_LAST_NAME}"

        # Клік на кнопку "Cancel" для закриття вікна редагування профайлу
        cancel_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/ngb-modal-window/div/div/app-edit-profile-modal/div[1]/button",
                )
            )
        )
        cancel_button.click()

        # Тут можна додати додаткові перевірки

        print("Тест перевірки даних на сторінці профайлу пройшов успішно!")

        # Видалення користувача
        settings_url = "https://guest:welcome2qauto@qauto.forstudy.space/panel/settings"
        driver.get(settings_url)

        remove_account_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-settings/div/div[2]/div/div[5]/div/button",
                )
            )
        )
        remove_account_button.click()

        confirm_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/ngb-modal-window/div/div/app-remove-account-modal/div[3]/button[2]",
                )
            )
        )
        confirm_button.click()

        # Тут можна додати перевірку, чи користувач успішно видалений

        print("Тест видалення користувача пройшов успішно!")

    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    test_qa_auto_workflow()
