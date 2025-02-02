import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
# options.add_argument("--incognito")


driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver,26,poll_frequency=1)

driver.get("https://omayo.blogspot.com/")

DISAPPER_TEXT = ("xpath", "//div[@id='deletesuccess']")
DELAYED_TEXT = ("xpath", "//div[@id='delayedText']")
BUTTON_TO_BE_ENABLE = ("xpath", "//input[@id='timerButton']")
DISABLE_OR_ENABLE_BUTTON = ("xpath", "//button[@id='myBtn']")
TRY_BUTTON = ("xpath", "//button[text()='Try it']")

wait.until(EC.invisibility_of_element(DISAPPER_TEXT), message="Текст не исчез")

wait.until(EC.text_to_be_present_in_element(DELAYED_TEXT, "This text is displayed after 10 seconds of wait."),
           "Текст не появился")

wait.until(EC.element_to_be_clickable(BUTTON_TO_BE_ENABLE), f"Кнопка {BUTTON_TO_BE_ENABLE} не появилась")

wait.until(EC.element_located_selection_state_to_be(DISABLE_OR_ENABLE_BUTTON, is_selected=False),
           f"Кнопка {DISABLE_OR_ENABLE_BUTTON} не выключена")



click_to_disable = driver.find_element(*TRY_BUTTON).click()


wait.until(lambda driver: driver.find_element(*DISABLE_OR_ENABLE_BUTTON).get_attribute("disabled") == "true",
           message=f"Кнопка {DISABLE_OR_ENABLE_BUTTON} активная")

