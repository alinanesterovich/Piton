import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test(browser):
    driver = browser
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html ")

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait = WebDriverWait(driver, 50)
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    actual_result = driver.find_element(By.CLASS_NAME, "screen").text
    assert actual_result == "15", f"Ожидалось 15, получено {actual_result}"

    print("Успешно")