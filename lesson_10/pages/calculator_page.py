from typing import Optional, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс Page Object для страницы медленного калькулятора.
    Содержит методы для взаимодействия с элементами страницы.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера для управления браузером.

        Returns:
            None
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 60)

    def open(self) -> "CalculatorPage":
        """
        Открывает страницу калькулятора в браузере.

        Returns:
            CalculatorPage: Экземпляр текущей страницы для цепочки вызовов.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Устанавливает задержку вычисления в секундах.

        Args:
            seconds (int): Количество секунд задержки.

        Returns:
            CalculatorPage: Экземпляр текущей страницы для цепочки вызовов.
        """
        delay_input: WebElement = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def press_button(self, label: str) -> "CalculatorPage":
        """
        Нажимает кнопку на калькуляторе по её тексту.

        Args:
            label (str): Текст на кнопке (например, '7', '+', '=').

        Returns:
            CalculatorPage: Экземпляр текущей страницы для цепочки вызовов.
        """
        button: WebElement = self.driver.find_element(
            By.XPATH, f"//div[@class='keys']//span[text()='{label}']"
        )
        button.click()
        return self

    def get_result(self, expected_text: str) -> str:
        """
        Ожидает появления результата и возвращает его текст.

        Args:
            expected_text (str): Ожидаемый текст результата (например, '15').

        Returns:
            str: Текст, отображаемый в поле результата.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected_text
            )
        )
        result_element: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, ".screen"
        )
        return result_element.text.strip()

