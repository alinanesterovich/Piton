import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form(browser):
    driver = browser
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("7985899998787")
    driver.find_element(By.NAME, "zip-code").clear()
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("data-types-submitted"))
    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    zip_code_element = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_element.get_attribute("class"), \
        "Поле Zip code не подсвечено красным"
    assert zip_code_element.text == "N/A", \
        f"Ожидалось 'N/A' для Zip code, получено '{zip_code_element.text}'"

    fields_to_check = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "7985899998787",
        "job-position": "QA",
        "company": "SkyPro"
    }
    for element_id, expected_value in fields_to_check.items():
        element = driver.find_element(By.ID, element_id)
        assert "alert-success" in element.get_attribute("class"), \
            f"Поле {element_id} не подсвечено зелёным"
        assert element.text == expected_value, \
            (f"Поле {element_id}: ожидалось '{expected_value}', "
             f"получено '{element.text}'")

        print("Проверка прошла успешно")