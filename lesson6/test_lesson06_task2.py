from selenium import webdriver
from time import sleep

def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru/")


    driver.add_cookie({
        "name": "SESSION",
        "value": "NDIxYjZhNzgtYWM4Ny00M2FiLTllY2EtMzhhM2UxZTg2MDll",
        "domain": "gitflic.ru"
})

    driver.refresh()
    driver.get("https://gitflic.ru/")
    url_user1 = driver.current_url
    print("URL пользователя 1:", url_user1)
    sleep(2)

    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
            "name": "SESSION",
            "value": "YWU0YzgzN2MtMzUwOC00MzA5LWE5OTctOTI2NGI2N2NhNGIy",
            "domain": "gitflic.ru"
})

    driver.refresh()
    driver.get("https://gitflic.ru/")
    url_user2 = driver.current_url
    print("URL пользователя 2:", url_user2)
    sleep(2)

    assert url_user1 != url_user2, "URL пользователя совпадают! Авторизация не работает."
    print("✅ URL пользователей различаются")
    sleep(2)

    driver.quit()