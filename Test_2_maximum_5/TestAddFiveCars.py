import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HomePage import HomePage


@pytest.fixture(scope="function")
def setup_teardown():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()


def test_add_five_cars(setup_teardown):
    driver, wait = setup_teardown

    # Створюємо об'єкт сторінки "Головна сторінка"
    home_page = HomePage(driver)

    # Відкриваємо головну сторінку
    driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    # Натиснемо на кнопку увійти як гість
    home_page.click_guest_button()

    # Перевірка, що ви можете створити не більше 5 авто
    max_cars = 6
    for i in range(max_cars):
        # Додавання авто
        home_page.click_add_car_button()
        home_page.select_car_brand()
        home_page.select_car_model()
        home_page.enter_mileage("10")
        home_page.click_save_button()

    # Перевірка на максимальну кількість авто
    with pytest.raises(Exception):
        home_page.click_add_car_button()
