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
    


# save_cookies.py
import json
from pathlib import Path
from pyvirtualdisplay import Display
from playwright.sync_api import sync_playwright


# def get_new_encar_cookies():
#     user_agent = (
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) "
#         "Chrome/126.0.6478.127 Safari/537.36"
#     )

#     #with Display(visible=0, size=(1920, 1080)): # виртуальный дисплей для Linux сервера (локально не нужен)
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context(
#             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
#             viewport={"width": 1920, "height": 1080},
#             locale="en-US",
#             timezone_id="Asia/Seoul",
#         )
#         page = context.new_page()
        
#         # простая имитация действий
#         page.goto("https://www.encar.com/", timeout=60000)
#         page.mouse.move(100, 100)
#         page.mouse.click(100, 100)
#         page.wait_for_timeout(5000)
        
#         cookies = context.cookies()
#         browser.close()
#         return cookies

#     # фильтруем только куки для encar.com
#     filtered = [c for c in cookies if "encar.com" in c["domain"]]

#     print(f"Cookies saved to")
#     return filtered



# файл: encar_cookies_stealth.py
import json
import random
import time
from pathlib import Path
from typing import Optional, List, Dict

from playwright.sync_api import sync_playwright

# --- Настройки ---
USER_AGENTS = [
    # несколько реалистичных UA (можно расширять)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6423.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6423.93 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6423.93 Safari/537.36",
]

DEFAULT_VIEWPORT = {"width": 1366, "height": 768}
DEFAULT_LOCALE = "en-US"  # или "en-US" — энкар корейский, locale можно подбирать
DEFAULT_TIMEZONE = "Asia/Seoul"

# --- Stealth script: скрываем webdriver и кое-что ещё ---
STEALTH_JS = r"""
// navigator.webdriver
Object.defineProperty(navigator, 'webdriver', {get: () => false, configurable: true});

// languages
Object.defineProperty(navigator, 'languages', {get: () => ['ko-KR', 'ko', 'en-US', 'en'], configurable: true});

// plugins (fake non-empty)
Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5], configurable: true});

// chrome runtime stub
window.chrome = window.chrome || { runtime: {} };

// permissions
const originalQuery = window.navigator.permissions.query;
window.navigator.permissions.query = (parameters) => (
    parameters.name === 'notifications' ?
        Promise.resolve({ state: Notification.permission }) :
        originalQuery(parameters)
);

// webdriver attributes on prototypes
try {
  delete Object.getPrototypeOf(navigator).webdriver;
} catch (e) {}
"""

# --- Utility: случайные человеческие действия ---
def human_like_activity(page, actions_count=5):
    """Примитивная имитация: движения мыши, скролл, клики, ввод."""
    w = page.viewport_size["width"]
    h = page.viewport_size["height"]

    def rnd_delay(a=0.2, b=1.2):
        time.sleep(random.uniform(a, b))

    # небольшая пауза перед активностью
    rnd_delay(0.5, 1.5)

    # несколько случайных движений мыши
    for _ in range(random.randint(3, 7)):
        x = random.randint(50, max(100, w - 50))
        y = random.randint(50, max(100, h - 50))
        page.mouse.move(x, y, steps=random.randint(5, 20))
        rnd_delay(0.05, 0.3)

    # скролл вниз/вверх
    for _ in range(random.randint(1, 3)):
        by = random.randint(200, int(h * 0.8))
        page.evaluate(f"window.scrollBy(0, {by});")
        rnd_delay(0.4, 1.2)
    page.evaluate("window.scrollTo(0, 0);")
    rnd_delay(0.2, 0.6)

    # клик в случайной точке (но в видимой части)
    try:
        px = random.randint(100, w - 100)
        py = random.randint(120, h - 120)
        page.mouse.click(px, py)
    except Exception:
        pass
    rnd_delay(0.3, 1.0)

    # попытка найти поле поиска и ввести текст (если есть) — не критично если не найдено
    try:
        # пример селектора — может не совпасть, просто пробует
        input_sel = "input[type='search'], input[name*=search], input[placeholder*='검색'], input[placeholder*='Search']"
        el = page.query_selector(input_sel)
        if el:
            text = random.choice(["test", "현대", "suv", "기아"])
            el.click()
            for ch in text:
                el.type(ch)
                time.sleep(random.uniform(0.05, 0.18))
            time.sleep(random.uniform(0.8, 1.6))
            # очищаем поле (чтобы не ломать последующие сценарии)
            el.fill("")
    except Exception:
        pass

# --- Главная функция ---
def get_new_encar_cookies(
    proxy: Optional[str] = None,
    headless: bool = False,
    save_path: Optional[str] = "encar_cookies.json",
    extra_user_agent_list: Optional[List[str]] = None,
    timeout_ms: int = 60000
) -> List[Dict]:
    """
    proxy: пример "http://user:pass@host:port" или "http://host:port" или None
    headless: False рекомендовано для маскировки (имитации реального браузера)
    save_path: куда сохранить JSON с куками (включая заголовки)
    """
    ua_list = USER_AGENTS + (extra_user_agent_list or [])
    user_agent = random.choice(ua_list)

    # Парсим proxy для playwright
    proxy_arg = None
    if proxy:
        # Playwright принимает словарь {"server": "http://host:port"} и можно встраивать user:pass в URL.
        proxy_arg = {"server": proxy}

    filtered = []
    save_p = Path(save_path)
    with Display(visible=0, size=(1920, 1080)):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=headless, args=["--no-sandbox", "--disable-blink-features=AutomationControlled"])
            context = browser.new_context(
                user_agent=user_agent,
                viewport=DEFAULT_VIEWPORT,
                locale=DEFAULT_LOCALE,
                timezone_id=DEFAULT_TIMEZONE,
                java_script_enabled=True,
                # Если нужно использовать proxy на уровне контекста, Playwright позволяет передать proxy при launch, 
                # но для синхронного API — мы задали при launch, можно также задать здесь (зависит от версии).
            )

            # Встраиваем stealth JS до загрузок страниц:
            context.add_init_script(STEALTH_JS)

            # Открываем страницу
            page = context.new_page()
            try:
                page.goto("https://encar.com/", timeout=timeout_ms)
            except Exception as e:
                print("Ошибка при загрузке:", e)
                # пробуем всё равно собрать куки (возможно редирект на страницу блока)
            # Подождём немного, даём сайтам прогрузиться
            time.sleep(random.uniform(2.5, 5.5))

            # Human-like actions
            try:
                human_like_activity(page)
            except Exception as e:
                print("human_like_activity failed:", e)

            # Доп. пауза, чтобы сайт успел отработать
            time.sleep(random.uniform(30.0, 40.0))

            try:
                cookies = context.cookies()
            except Exception as e:
                print("Не удалось получить cookies:", e)
                cookies = []

            # Закрываем browser/context
            try:
                context.close()
                browser.close()
            except Exception:
                pass

        # Фильтруем по домену encar.com
        filtered = [c for c in cookies if "encar.com" in c.get("domain", "") or c.get("domain", "").endswith(".encar.com")]

        print(cookies)

        return filtered

