from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    html_form = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form.click()
    if driver.current_url.endswith("/forms/post"):
        print("Успешно")
    else:
        print(f"Провал. Текущий url: {driver.current_url}")
    driver.back()
    if driver.current_url == "https://httpbin.qa-territory.online":
        print("Успешно")
    else:
        print(f"Провален. Текущий url: {driver.current_url}")
    driver.quit()
