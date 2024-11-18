
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


driver.get("https://demoqa.com/selectable")

GRID_TAB = ("xpath", "//nav/a[@id='demo-tab-grid']")

ONE_TAB = ("xpath", "//div/li[text()='One']")
TWO_TAB = ("xpath", "//div/li[text()='Two']")


wait.until(EC.element_to_be_clickable(GRID_TAB)).click()

wait.until(EC.element_to_be_clickable(ONE_TAB)).click()
wait.until(EC.element_to_be_clickable(TWO_TAB)).click()
assert "active " in driver.find_element(*ONE_TAB).get_attribute("class")
assert "active " in driver.find_element(*TWO_TAB).get_attribute("class")

wait.until(EC.element_to_be_clickable(ONE_TAB)).click()
wait.until(EC.element_to_be_clickable(TWO_TAB)).click()


assert "active " not in driver.find_element(*ONE_TAB).get_attribute("class")
assert "active " not in driver.find_element(*TWO_TAB).get_attribute("class")



