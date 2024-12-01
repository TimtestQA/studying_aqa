import time
from logging import currentframe

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
# options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver,10, 1)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


driver.get('https://hyperskill.org/login')

first_tab = driver.current_window_handle

driver.switch_to.new_window("tab")

driver.get("https://www.avito.ru/")

second_tab = driver.current_window_handle

driver.switch_to.new_window("tab")

driver.get("https://www.ozon.ru/")

third_tab = driver.current_window_handle

windows_count = driver.window_handles

assert len(driver.window_handles) == 3, "Открыто больше 3х вкладок"

original_tab_nandless = driver.window_handles

driver.switch_to.window(second_tab)

print(driver.title)

driver.switch_to.window(first_tab)

print(driver.title)

PRICING_BUTTON = ("xpath", "//a[normalize-space()='Pricing']")

wait.until(EC.element_to_be_clickable(PRICING_BUTTON)).click()

wait.until(EC.url_changes("https://hyperskill.org/pricing"),"URL не изменился")

driver.switch_to.window(third_tab)

print(driver.title)


driver.switch_to.window(second_tab)

AVITO_FOR_BUISENES_BUTTON = ("xpath", "//a[text()='Для бизнеса']")

wait.until(EC.element_to_be_clickable(AVITO_FOR_BUISENES_BUTTON)).click()

assert driver.current_url == "https://www.avito.ru/business", "Раздел не открыт"

driver.switch_to.window(third_tab)

OZON_CART_BUTTON = ("xpath", "//a[@class='a6 p8d_4_9']")

wait.until(EC.element_to_be_clickable(OZON_CART_BUTTON)).click()

for window_handle in driver.window_handles:
    if window_handle not in original_tab_nandless:
        driver.switch_to.window(window_handle)
        break
wait.until(EC.url_to_be("https://www.ozon.ru/cart"),"Корзина не открылась")


driver.close()