from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object для страницы калькулятора.
    Содержит локаторы и методы для взаимодействия с интерфейсом.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)  # Увеличенный таймаут для медленного калькулятора

    def open(self) -> "CalculatorPage":
        """
        Открывает страницу калькулятора.

        :return: Экземпляр текущей страницы для цепочки вызовов.
        :rtype: CalculatorPage
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Устанавливает задержку вычисления в секундах.

        :param seconds: Количество секунд задержки.
        :type seconds: int
        :return: Экземпляр текущей страницы для цепочки вызовов.
        :rtype: CalculatorPage
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def press_button(self, label: str) -> "CalculatorPage":
        """
        Нажимает кнопку на калькуляторе по её тексту.

        :param label: Текст на кнопке (например, '7', '+', '=').
        :type label: str
        :return: Экземпляр текущей страницы для цепочки вызовов.
        :rtype: CalculatorPage
        """
        button = self.driver.find_element(
            By.XPATH, f"//div[@class='keys']//span[text()='{label}']"
        )
        button.click()
        return self

    def get_result(self, expected_text: str) -> str:
        """
        Ожидает появления результата и возвращает его текст.

        :param expected_text: Ожидаемый текст результата (например, '15').
        :type expected_text: str
        :return: Текст, отображаемый в поле результата.
        :rtype: str
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected_text
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text.strip()
