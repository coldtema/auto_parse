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
from playwright.sync_api import sync_playwright, TimeoutError

def get_new_encar_cookies():
    print("[INFO] Starting get_new_encar_cookies()")
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.6478.127 Safari/537.36"
    )

    try:
        print("[INFO] Starting virtual display")
        with Display(visible=0, size=(1920, 1080)):
            print("[INFO] Virtual display started")

            with sync_playwright() as p:
                print("[INFO] Playwright started")
                browser = p.chromium.launch(headless=False)
                print("[INFO] Browser launched")
                
                context = browser.new_context(
                    user_agent=user_agent,
                    viewport={"width": 1920, "height": 1080},
                    locale="en-US",
                    timezone_id="Asia/Seoul",
                )
                print("[INFO] Browser context created")

                page = context.new_page()
                print("[INFO] New page opened")

                try:
                    page.goto("https://www.encar.com/", timeout=60000)
                    print("[INFO] Page loaded successfully")
                except TimeoutError:
                    print("[ERROR] Page load timed out")

                cookies = context.cookies()
                print(f"[INFO] Retrieved cookies: {cookies}")

                browser.close()
                print("[INFO] Browser closed")

    except Exception as e:
        print(f"[ERROR] Exception in get_new_encar_cookies: {e}")
        cookies = []

    return cookies

