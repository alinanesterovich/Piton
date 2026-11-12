import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_total(browser):
    driver = browser

    # 1. Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация как standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("inventory"))

    # 3. Добавить товары в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Перейти в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart"))

    # 5. Нажать Checkout
    driver.find_element(By.ID, "checkout").click()
    wait.until(EC.url_contains("checkout-step-one"))

    # 6. Заполнить форму данными
    driver.find_element(By.ID, "first-name").send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Petrov")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Нажать Continue
    driver.find_element(By.ID, "continue").click()
    wait.until(EC.url_contains("checkout-step-two"))

    # 8. Прочитать итоговую стоимость (Total)
    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text.strip()

    # 9. Проверить, что итоговая сумма равна $58.29
    assert "$58.29" in total_text, f"Ожидалось '$58.29', получено '{total_text}'"

    # 10. Закрыть браузер (выполняется в фикстуре после завершения теста)