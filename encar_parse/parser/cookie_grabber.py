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
# regen_encar_cookies.py
# import time
# import json
# import random
# import base64
# import secrets
# from pathlib import Path
# from datetime import datetime, timedelta
# from playwright.sync_api import sync_playwright

# # --------------------------
# # Настройки (настрой под себя)
# # --------------------------
# API_URL = "https://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.N._.CarType.A._.GreenType.Y.)&sr=%7CModifiedDate%7C0%7C20"
# OUT_DIR = Path("regen_result")
# # OUT_DIR.mkdir(exist_ok=True)
# HEADLESS = False  # поставь True, если хочешь headless (но лучше тестировать headful)
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"

# # --------------------------
# # Твои старые (просроченные) cookie — вставь сюда те, что у тебя есть
# # --------------------------
# OLD_COOKIES = [
#     {"name":"_encar_hostname","value":"https://www.encar.com","domain":".encar.com","path":"/","expires":1761580581,"httpOnly":False,"secure":False,"sameSite":"Lax"},
#     {"name":"OAX","value":"sGr5G2j+RKcAAqgW","domain":".encar.com","path":"/","expires":1796054182.425719,"httpOnly":False,"secure":False,"sameSite":"Lax"},
#     {"name":"PCID","value":"17614941825627481999814","domain":".encar.com","path":"/","expires":1796054182.562722,"httpOnly":False,"secure":False,"sameSite":"Lax"},
#     {"name":"_enlog_lpi","value":"1c82.aHR0cHM6Ly93d3cuZW5jYXIuY29tL2luZGV4LmRv.ff5","domain":".encar.com","path":"/","expires":1761495982,"httpOnly":False,"secure":False,"sameSite":"Lax"},
#     {"name":"_ga","value":"GA1.2.657808260.1761494183","domain":".encar.com","path":"/","expires":1796054182.630853,"httpOnly":False,"secure":False,"sameSite":"Lax"},
#     {"name":"_gid","value":"GA1.2.5646491.1761494183","domain":".encar.com","path":"/","expires":1761580582,"httpOnly":False,"secure":False,"sameSite":"Lax"},
#     {"name":"_gat_UA-56065139-3","value":"1","domain":".encar.com","path":"/","expires":1761494242,"httpOnly":False,"secure":False,"sameSite":"Lax"},
#     {"name":"_ga_WY0RWR65ED","value":"GS2.2.s1761494182$o1$g0$t1761494182$j60$l0$h0","domain":".encar.com","path":"/","expires":1796054182.754891,"httpOnly":False,"secure":False,"sameSite":"Lax"}
# ]

# # --------------------------
# # Помощники: генерация значений
# # --------------------------
# def gen_pcid():
#     # похожая на реальную: цифровая строка с префиксом времени + случайное
#     t = int(time.time() * 1000)
#     rnd = secrets.token_hex(8)
#     return f"{t}{rnd}"

# def gen_oax():
#     # пример: base64-like / random-urlsafe
#     return secrets.token_urlsafe(12)

# def gen_ga_pair():
#     # GA cookie format "GA1.2.<clientId>.<timestamp>"
#     client_id = str(random.randint(100000000, 999999999))
#     ts = str(int(time.time()))
#     ga = f"GA1.2.{client_id}.{ts}"
#     gid = f"GA1.2.{random.randint(1000000,9999999)}.{ts}"
#     return ga, gid

# def gen_ga_gid_suffix():
#     # sometimes GA _ga_<id> contains GS2 string; we fake a plausible one
#     ts = int(time.time())
#     return f"GS2.2.s{ts}$o1$g0$t{ts}$j60$l0$h0"

# def regen_enlog_for_url(url: str):
#     # формат был: prefix.base64.url.suffix  -> "1c82.<base64>.ff5"
#     # мы используем похожую структуру: random prefix, base64(current page), random suffix
#     prefix = "1c82"
#     b = base64.b64encode(url.encode()).decode().rstrip("=")  # remove padding to be similar
#     suffix = "ff5"
#     return f"{prefix}.{b}.{suffix}"

# def update_expires(days=30):
#     return int((datetime.utcnow() + timedelta(days=days)).timestamp())

# # --------------------------
# # Основная логика
# # --------------------------
# def build_regenerated_cookies(old_cookies):
#     # Создаём новую карту: возьмём имена старых cookie и заменим значения на сгенерированные/обновлённые
#     new = []
#     # генерим базовые новые значения
#     new_pcid = gen_pcid()
#     new_oax = gen_oax()
#     new_ga, new_gid = gen_ga_pair()
#     new_ga_suffix = gen_ga_gid_suffix()
#     now_url = "https://www.encar.com/index.do"

#     for c in old_cookies:
#         name = c.get("name")
#         cookie = dict(c)  # copy
#         # обновляем expires и value по имени
#         cookie["expires"] = update_expires(days=30)
#         if name == "PCID":
#             cookie["value"] = new_pcid
#         elif name == "OAX":
#             cookie["value"] = new_oax
#         elif name == "_enlog_lpi":
#             cookie["value"] = regen_enlog_for_url(now_url)
#         elif name == "_ga":
#             cookie["value"] = new_ga
#         elif name == "_gid":
#             cookie["value"] = new_gid
#         elif name == "_ga_WY0RWR65ED":
#             cookie["value"] = new_ga_suffix
#         elif name == "_encar_hostname":
#             cookie["value"] = "https://www.encar.com"
#         # отметим домен (Playwright требует без пути httpOnly bool etc)
#         cookie["domain"] = ".encar.com"
#         cookie["path"] = "/"
#         # Playwright expects expires as unix seconds or None; keep as int
#         new.append(cookie)
#     return new

# def human_like(page):
#     # простая human-like имитация
#     page.mouse.move(200, 200)
#     time.sleep(random.uniform(0.3, 1.2))
#     page.mouse.wheel(0, 400)
#     time.sleep(random.uniform(0.2, 1.0))
#     # случайный клик
#     page.mouse.click(random.randint(200, 800), random.randint(200, 600))
#     time.sleep(random.uniform(0.5, 1.5))

# # --------------------------
# # Запуск Playwright
# # --------------------------

# def get_new_encar_cookies():
#     regenerated = build_regenerated_cookies(OLD_COOKIES)
#     # out_old = OUT_DIR / "old_cookies.json"
#     # out_new = OUT_DIR / "regenerated_cookies.json"
#     # out_api = OUT_DIR / "api_result.json"
#     # out_state = OUT_DIR / "encar_state_after.json"
#     # out_old.write_text(json.dumps(OLD_COOKIES, ensure_ascii=False, indent=2))
#     # out_new.write_text(json.dumps(regenerated, ensure_ascii=False, indent=2))

#     print("Regenerated cookies preview:")
#     for c in regenerated:
#         print(c["name"], "=", c["value"])
#     # with Display(visible=0, size=(1920, 1080)):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=HEADLESS, args=["--disable-blink-features=AutomationControlled"])
#         context = browser.new_context(user_agent=USER_AGENT, viewport={"width":1366,"height":768}, locale="ko-KR", timezone_id="Asia/Seoul")
#         page = context.new_page()

#         # Устанавливаем cookie в контекст (Playwright принимает dicts with expires optional)
#         # Note: Playwright wants 'expires' as float seconds since epoch or nothing — we pass int
#         try:
#             context.add_cookies([
#                 {
#                     "name": c["name"],
#                     "value": str(c["value"]),
#                     "domain": c.get("domain", ".encar.com"),
#                     "path": c.get("path", "/"),
#                     "expires": int(c.get("expires")) if c.get("expires") else None,
#                     "httpOnly": c.get("httpOnly", False),
#                     "secure": c.get("secure", False),
#                     "sameSite": c.get("sameSite", "Lax"),
#                 } for c in regenerated
#             ])
#             print("Cookies added to context.")
#         except Exception as e:
#             print("Failed to add cookies:", e)

#         # Заходим на страницу, имитируем поведение
#         try:
#             page.goto("https://www.encar.com/", timeout=60000)
#         except Exception as e:
#             print("Page goto error (continuing):", e)

#         # human-like
#         try:
#             human_like(page)
#         except Exception as e:
#             print("Human-like actions failed:", e)

#         # Ждём, даём JS возможность среагировать и поменять куки если нужно
#         time.sleep(3.0)

#         # Посмотрим, какие cookie теперь видит браузер
#         cookies_after = context.cookies()
#         filtered = [c for c in cookies_after if "encar.com" in c["domain"]]
#         print(filtered)
#         print(f"Cookies saved to")
#         return filtered

#         (OUT_DIR / "cookies_after.json").write_text(json.dumps(cookies_after, ensure_ascii=False, indent=2))
#         print("Saved cookies_after.json (count=%d)" % len(cookies_after))

#         # Выполним fetch к API внутри браузера и соберём ответ (если сервер примет наш "сгенеренный" пайп)
#         try:
#             fetch_script = f"""
#             () => fetch("{API_URL}", {{
#                 method: "GET",
#                 credentials: "include",
#                 headers: {{
#                     "Accept": "application/json, text/javascript, */*; q=0.01",
#                     "X-Requested-With": "XMLHttpRequest",
#                     "Referer": "https://www.encar.com/",
#                     "Origin": "https://www.encar.com",
#                     "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
#                 }}
#             }}).then(async resp => {{
#                 const text = await resp.text();
#                 const headers = {{}};
#                 for (const [k,v] of resp.headers.entries()) headers[k] = v;
#                 return {{status: resp.status, headers: headers, body: text.slice(0, 5000)}};
#             }}).catch(e => {{ return {{error: String(e)}} }});
#             """
#             result = page.evaluate(fetch_script)
#         except Exception as e:
#             result = {"error": str(e)}

#         out_api.write_text(json.dumps(result, ensure_ascii=False, indent=2))
#         print("API result saved to", out_api)

#         # Сохраняем storage_state после попытки (может содержать подставленные/серверные куки)
#         try:
#             context.storage_state(path=str(out_state))
#             print("Saved storage state to", out_state)
#         except Exception as e:
#             print("Failed to save storage state:", e)

#         browser.close()
#     print("Done. Check folder:", OUT_DIR.resolve())


from playwright.sync_api import sync_playwright
import random
import time

cookie_string = "OAX=sGr5G2i9bqQACwLB; PCID=17572450956999853444598; _fwb=77F9PqnVOm4b0B1ZOWkr70.1757245130323; _fbp=fb.1.1757435425388.635278253321423332; _gcl_au=1.1.183355727.1757443117; afUserId=9d2cac16-864d-4a98-b917-82248bf93ce9-p; RecentViewTruck=40341321%2C40517735; _ga_GRHD5Z14DC=GS2.2.s1758037408$o1$g0$t1758037418$j50$l0$h0; _ga_BQ7RK9J6BZ=GS2.1.s1758037408$o1$g1$t1758037429$j39$l0$h287401605; cto_bundle=WD5YnV8yN0dEb3BSWnlmNHhFczBnN0pXZmNGdjlOJTJCZjMydkluTiUyQm1rN09pa1FmNnRFaWhmVEtGSkNkR0lLOGVaNE50akxnQkQzMjVyMUk1dDYwaXhOV081SFFYZ25UdDl1R0JDZWtoOVZ4QWp5R0U5MGxWJTJCSVY0dXFkeXN4NmJOMUZvaCUyRm83RGloZW5RckRQc3NYcjdaRmJ4QSUzRCUzRA; _ga_SX6YBF7MKB=GS2.1.s1758037408$o1$g1$t1758037430$j38$l0$h0; AF_SYNC=1761005549155; WMONID=VvQ26h4wLkB; _encar_hostname=https://www.encar.com; _ga=GA1.2.697281578.1757245096; _gid=GA1.2.1056656369.1761483327; RecentViewAllCar=40295866%2C40513970%2C40510520%2C39311796%2C39628414%2C40156109%2C40430916%2C40294388%2C40434638%2C39852733%2C40448202%2C40176722%2C40372580%2C40341321%2C40517735%2C40425905%2C40478397%2C40480049%2C40489567%2C39422651%2C40343782; RecentViewCar=40295866%2C40513970%2C40510520%2C39311796%2C39628414%2C40156109%2C40430916%2C40294388%2C40434638%2C39852733%2C40448202%2C40176722%2C40372580%2C40425905%2C40478397%2C40480049%2C40489567%2C39422651%2C40343782; JSESSIONID=B10CE7CFE38FC573848FFC645E48C36D.mono-web-prod_201.65; _enlog_lpi=3270.aHR0cHM6Ly93d3cuZW5jYXIuY29tL2luZGV4LmRv.6a2; _enlog_datatalk_hit=; wcs_bt=4b4e532670e38c:1761544745; _ga_WY0RWR65ED=GS2.2.s1761544706$o13$g1$t1761544747$j19$l0$h0"

def parse_cookie_string(cookie_string):
    """Преобразует строку кук в формат для Playwright"""
    cookies = []
    for cookie in cookie_string.split('; '):
        if '=' in cookie:
            name, value = cookie.split('=', 1)
            cookies.append({
                'name': name.strip(),
                'value': value.strip(),
                'domain': '.encar.com',
                'path': '/'
            })
    return cookies



def create_stealth_browser():
    playwright = sync_playwright().start()
    
    browser = playwright.chromium.launch(
        headless=False,  # На время отладки False
        args=[
            '--no-sandbox',
            '--disable-blink-features=AutomationControlled',
            '--disable-dev-shm-usage',
            '--disable-web-security',
            '--disable-features=site-per-process',
            '--no-first-run',
            '--disable-default-apps',
            '--disable-popup-blocking',
            '--disable-translate',
            '--disable-background-timer-throttling',
            '--disable-renderer-backgrounding',
            '--disable-backgrounding-occluded-windows',
        ]
    )
    
    # Создаем контекст с реальными данными пользователя
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        locale="ru-RU",
        timezone_id="Europe/Moscow",
        permissions=["geolocation"],
        geolocation={"latitude": 55.7558, "longitude": 37.6173},
        color_scheme="light"
    )
    
    # Удаляем все следы автоматизации
    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined,
        });
        
        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3, 4, 5],
        });
        
        Object.defineProperty(navigator, 'languages', {
            get: () => ['ru-RU', 'ru', 'en-US', 'en'],
        });
        
        window.chrome = {
            app: {},
            runtime: {},
        };
    """)
    
    page = context.new_page()
    
    # Добавляем случайные заголовки
    page.set_extra_http_headers({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Cache-Control": "no-cache",
                "Origin": "https://www.encar.com",
                "Pragma": 'no-cache',
                "Priority": "u=1, i",
                "Referer": "https://www.encar.com/",
                "Sec-Ch-Ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                # "X-Requested-With": "XMLHttpRequest",
            })
    
    return playwright, browser, context, page

def human_delay(min_ms=1000, max_ms=5000):
    """Случайная задержка как у человека"""
    delay = random.randint(min_ms, max_ms) / 1000.0
    time.sleep(delay)

def human_type(page, selector, text):
    """Человеческий ввод текста"""
    element = page.query_selector(selector)
    element.click()
    
    # Случайная пауза перед началом ввода
    human_delay(200, 800)
    
    for char in text:
        element.type(char, delay=random.randint(50, 150))
        # Случайные паузы между словами
        if char == ' ':
            human_delay(100, 300)

def human_scroll(page):
    """Человеческая прокрутка страницы"""
    scroll_amount = random.randint(300, 800)
    scroll_steps = random.randint(3, 8)
    
    for _ in range(scroll_steps):
        scroll_step = scroll_amount // scroll_steps
        page.evaluate(f"window.scrollBy(0, {scroll_step})")
        human_delay(100, 400)

def human_mouse_move(page, selector):
    """Плавное движение мыши к элементу"""
    element = page.query_selector(selector)
    if not element:
        return
        
    box = element.bounding_box()
    if not box:
        return
    
    # Плавное движение с случайным количеством шагов
    target_x = box['x'] + box['width'] / 2
    target_y = box['y'] + box['height'] / 2
    
    steps = random.randint(8, 15)
    current_x, current_y = 100, 100  # Начальная позиция
    
    for i in range(steps):
        progress = (i + 1) / steps
        new_x = current_x + (target_x - current_x) * progress
        new_y = current_y + (target_y - current_y) * progress
        
        page.mouse.move(new_x, new_y)
        time.sleep(random.uniform(0.02, 0.05))
    
    human_delay(200, 600)
    element.click()


def get_new_encar_cookies():
    with Display(visible=0, size=(1920, 1080)):
        playwright, browser, context, page = create_stealth_browser()
        
        try:
            print("🕵️ Запускаем stealth браузер...")
            
            # Сначала идем на нейтральный сайт
            print("📝 Имитируем обычный серфинг...")
            page.goto("https://google.com")
            human_delay(2000, 5000)
            
            # Случайные действия на странице
            human_scroll(page)
            human_delay(1000, 3000)
            
            # Теперь переходим на encar
            print("🚀 Переходим на encar.ru...")
            cookies = parse_cookie_string(cookie_string)
            context.add_cookies(cookies)
            page.goto("https://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.N._.CarType.A._.GreenType.Y.)&sr=%7CModifiedDate%7C0%7C20", wait_until="networkidle", timeout=60000)
            human_delay(3000, 7000)
            
            # Имитируем изучение страницы
            human_scroll(page)
            human_delay(2000, 4000)
            
            # Случайные движения мыши
            page.mouse.move(300, 400)
            human_delay(500, 1500)
            page.mouse.move(700, 200)
            human_delay(500, 1500)
            
            print("✅ Страница загружена, можно работать...")
            
            # Здесь ваша логика парсинга
            # Например:
            # elements = page.query_selector_all(".car-item")
            # for element in elements:
            #     title = element.query_selector(".title")
            #     if title:
            #         print(title.text_content())
            
            # Сохраняем куки для будущего использования
            cookies = context.cookies()
            print(f"🍪 Получено {len(cookies)} кук")
            
            # Сохраняем куки в файл
            # import json
            # with open("encar_cookies.json", "w") as f:
            #     json.dump(cookies, f)
            
            print("💾 Куки сохранены в encar_cookies.json")
            
            # Демонстрация работы - ждем
            print("⏳ Демонстрация работы...")
            human_delay(10000, 20000)
            
            return cookies
            
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            return None
            
        finally:
            # Делаем скриншот для отладки
            # page.screenshot(path="encar_result.png")
            # print("📸 Скриншот сохранен как encar_result.png")
            
            browser.close()
            playwright.stop()
            return cookies
