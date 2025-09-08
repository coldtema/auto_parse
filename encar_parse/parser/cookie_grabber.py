# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import requests


# def get_new_encar_cookies():
#     options = Options()
#     # options.add_argument("--headless")
#     driver = webdriver.Chrome()

#     driver.get("https://www.encar.com/")

#     cookies = driver.get_cookies()
#     driver.quit()
#     print(cookies)
#     return cookies
    


from playwright.sync_api import sync_playwright
def get_new_encar_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # тут headless работает
        page = browser.new_page()
        page.goto("https://www.encar.com/")
        cookies = page.context.cookies()
        browser.close()
    print(cookies)
    return cookies