import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    """Page Object для страницы медленного калькулятора."""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)  # таймаут с запасом на 45с + рендер

    # --- Локаторы ---
    @property
    def delay_input(self):
        return self.driver.find_element(By.ID, "delay")

    @property
    def result_output(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen")

    # Кнопки калькулятора ищутся по тексту (7, +, 8, = и т.д.)
    def button(self, label):
        return self.driver.find_element(
            By.XPATH, f"//div[@class='keys']//span[text()='{label}']"
        )

    # --- Действия ---
    def open(self):
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds):
        self.delay_input.clear()
        self.delay_input.send_keys(str(seconds))
        return self

    def press(self, *labels):
        for label in labels:
            self.button(label).click()
        return self

    def get_result(self):
        return self.result_output.text.strip()

    def wait_for_result(self, expected):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected
            )
        )
        return self.result_output.text.strip()


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator_7_plus_8(browser):
    page = SlowCalculatorPage(browser)

    # 1. Открыть страницу калькулятора
    page.open()

    # 2. Ввести задержку 45 секунд
    page.set_delay(45)

    # 3. Нажать 7, +, 8, =
    page.press("7", "+", "8", "=")

    # 4. Проверить результат 15 (ждём до 45с + запас)
    result = page.wait_for_result("15")
    assert result == "15", f"Ожидалось '15', получено '{result}'"

    print("Готово")