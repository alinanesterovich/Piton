from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.org/forms/post")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)
        name_field = wait.until(
            EC.presence_of_element_located((By.NAME, "custname"))
        )
        name_field.clear()
        name_field.send_keys("Алина")
        previous_url = driver.current_url

        submit_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_btn.click()
        wait.until(EC.url_changes(previous_url))

        new_url = driver.current_url
        assert new_url != previous_url, "URL не изменился после отправки формы"
        assert "/post" in new_url or "httpbin.org" in new_url

    finally:
        driver.quit()
