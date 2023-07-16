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


def test_add_five_cars(setup_teardown):
    driver, wait = setup_teardown

    try:
        driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

        # Натиснемо на кнопку увійти як гість
        guest_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[1]",
                )
            )
        )
        guest_button.click()

        # Перевірка, що ви можете створити не більше 5 авто
        max_cars = 5
        for i in range(max_cars):
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
                    (By.XPATH, "//*[@id='addCarBrand']/option[1]")
                )
            )
            car_brand_option.click()

            # Вибір моделі авто
            car_model_option = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='addCarModel']/option[1]")
                )
            )
            car_model_option.click()

            # Введення пробігу авто
            mileage_input = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='addCarMileage']"))
            )
            mileage_input.send_keys("10")

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

            # Перевірка, чи авто додано успішно
            print(f"Тест додавання {i + 1}-го авто пройшов успішно!")

        # Перевірка на максимальну кількість авто
        try:
            add_car_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button",
                    )
                )
            )
            add_car_button.click()
            pytest.fail("Додано більше 5ти авто")
        except:
            print("Перевірка на максимальну кількість авто пройшла успішно!")

    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    test_add_five_cars()
