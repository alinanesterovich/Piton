import allure
import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def browser():
    """Фикстура для запуска браузера Chrome."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка работы медленного калькулятора")
@allure.description("Тест проверяет, что калькулятор корректно выполняет сложение 7 + 8 с задержкой 45 секунд.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator_7_plus_8(browser):
    page = CalculatorPage(browser)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Ввести задержку 45 секунд"):
        page.set_delay(45)

    with allure.step("Нажать кнопки 7, +, 8, ="):
        page.press_button("7")
        page.press_button("+")
        page.press_button("8")
        page.press_button("=")

    with allure.step("Проверить, что результат равен 15"):
        result = page.get_result("15")
        assert result == "15", f"Ожидалось '15', получено '{result}'"
