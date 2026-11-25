import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def browser() -> WebDriver:
    """
    Фикстура для запуска браузера Chrome.

    Yields:
        WebDriver: Экземпляр веб-драйвера.
    """
    driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка работы медленного калькулятора")
@allure.description(
    "Тест проверяет, что калькулятор корректно выполняет сложение 7 + 8 "
    "с задержкой 45 секунд."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator_7_plus_8(browser: WebDriver) -> None:
    """
    Тест проверяет работу калькулятора с задержкой.

    Args:
        browser (WebDriver): Фикстура веб-драйвера.

    Returns:
        None
    """
    page: CalculatorPage = CalculatorPage(browser)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Ввести задержку 45 секунд"):
        page.set_delay(45)

    with allure.step("Нажать кнопки 7, +, 8, ="):
        page.press_button("7")
        page.press_button("+")
        page.press_button("8")
        page.press_button("=")

    with allure.step("Прочитать результат со страницы"):
        result: str = page.get_result("15")

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15", f"Ожидалось '15', получено '{result}'"

