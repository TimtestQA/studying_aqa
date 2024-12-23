import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from table_handler import TableHandler

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
action = ActionChains(driver)
table = TableHandler(driver)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://mega.readyscript.ru/admin")

#Login -> Product catalog table

SUBMIT_BUTTON = ("xpath", "//button[@type='submit'] //span[contains(text(), 'войти')]")

PRODUCTS_BUTTON = ("xpath", "//span[contains(text(), 'Товары')]")

CATALOG_PRODUCTS = ("xpath", "//span[contains(text(), 'Каталог товаров')]")

TITLE_CATALOG_PRODUCTS = ("xpath", "//h2//span[contains(text(), 'Каталог товаров')]")



wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON),"Кнопка не активна или ненайдена").click()

wait.until(EC.element_to_be_clickable(PRODUCTS_BUTTON))

product_button = driver.find_element(*PRODUCTS_BUTTON)

catalog_enter = driver.find_element(*CATALOG_PRODUCTS)

action.click(product_button).click(catalog_enter).perform()



print(table.row_count)

print(table.get_row_content(9))

print(table.get_cell_content(9, 4))

print(table.status_check(2))

table.select_row(4)