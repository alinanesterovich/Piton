from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()


    wait = WebDriverWait(driver, 10)
    
    hello_world_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )


    driver.save_screenshot("dynamic_loading_screenshot.png") 

    actual_text = hello_world_element.text
    assert actual_text == "Hello World!", f"Ожидался 'Hello World!', получен '{actual_text}'"

    driver.quit()