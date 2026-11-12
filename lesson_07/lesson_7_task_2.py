import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object страницы авторизации."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        self.wait.until(EC.url_contains("inventory"))
        return InventoryPage(self.driver)


class InventoryPage:
    """Page Object главной страницы магазина."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, *item_ids):
        for item_id in item_ids:
            self.driver.find_element(
                By.ID, f"add-to-cart-{item_id}"
            ).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.wait.until(EC.url_contains("cart"))
        return CartPage(self.driver)


class CartPage:
    """Page Object страницы корзины."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_item_names(self):
        return [
            el.text
            for el in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        ]

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        self.wait.until(EC.url_contains("checkout-step-one"))
        return CheckoutPage(self.driver)


class CheckoutPage:
    """Page Object страницы оформления заказа."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
        self.wait.until(EC.url_contains("checkout-step-two"))
        return self

    def get_total(self):
        total_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text.strip()


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_total(browser):
    # 1. Открыть сайт и авторизоваться
    login_page = LoginPage(browser).open()
    inventory_page = login_page.login("standard_user", "secret_sauce")

    # 2-3. Добавить товары в корзину
    inventory_page.add_to_cart(
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie",
    )

    # 4. Перейти в корзину и проверить содержимое
    cart_page = inventory_page.go_to_cart()
    items = cart_page.get_item_names()
    expected_items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]
    assert items == expected_items, f"Ожидались {expected_items}, получено {items}"

    # 5-7. Checkout и заполнение формы
    checkout_page = cart_page.checkout().fill_form("Ivan", "Petrov", "123456")

    # 8. Прочитать итоговую стоимость
    total = checkout_page.get_total()

    # 9. Проверить сумму (браузер закроется в фикстуре)
    assert "$58.29" in total, f"Ожидалось '$58.29', получено '{total}'"