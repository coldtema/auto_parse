from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests


# def get_new_encar_cookies():
#     options = Options()
#     # options.add_argument("--headless")
#     driver = webdriver.Chrome()

#     driver.get("https://www.encar.com/")

#     cookies = driver.get_cookies()
#     driver.quit()
#     print(cookies)
#     return cookies
    


from pyvirtualdisplay import Display
from playwright.sync_api import sync_playwright

def get_new_encar_cookies():
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.6478.127 Safari/537.36"
    )

    # виртуальный дисплей только на время работы браузера
    with Display(visible=0, size=(1920, 1080)):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False) 
            context = browser.new_context(
                user_agent=user_agent,
                viewport={"width": 1920, "height": 1080},
                locale="en-US",
                timezone_id="Asia/Seoul",
            )

            page = context.new_page()
            page.goto("https://www.encar.com/", timeout=60000)

            cookies = context.cookies()
            browser.close()

    return cookies
