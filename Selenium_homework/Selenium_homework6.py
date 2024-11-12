import os.path
import time
import pickle
from os import getcwd
from selenium import webdriver
from selenium.webdriver import Keys
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


driver.get("https://lingualeo.com/ru/modules/auth/login")


driver.add_cookie({'name': 'username',
                   'value': 'user123'})



assert driver.get_cookie("username"), "Cookie отсутствует"

print(driver.get_cookie("username"))


driver.delete_cookie('username')

driver.refresh()




assert (driver.get_cookie('username')) == None,"Аборигены не смогли съесть куку"


driver.get("https://biggeek.ru/catalog/apple")

cookies_path = os.path.join(os.getcwd(), "cookies", "cookies.pkl")

BACK_TO_CATALOG = ("xpath", "//button[@class='cart-modal__return']")


if os.path.exists(cookies_path):
    driver.delete_all_cookies()
    cookies = pickle.load(open(cookies_path, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
else:
    for i in range(3):
        CLICK_BUTTON = ("xpath", f"(//a[@title='Добавить в корзину'])[{i + 1}]")
        wait.until(EC.element_to_be_clickable(CLICK_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(BACK_TO_CATALOG)).click()

        pickle.dump(driver.get_cookies(), open(cookies_path, "wb"))