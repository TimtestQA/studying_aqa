import time
from typing import final

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

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

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://seiyria.com/bootstrap-slider")

SLIDER_LCATOR = ("xpath", "//div[@id='example-8'] //div[@class='slider slider-horizontal'] "
                          "//div[@class='slider-handle min-slider-handle round']")

slider = driver.find_element(*SLIDER_LCATOR)

action.scroll_to_element(slider).perform()
driver.execute_script("""
            window.scrollTo({
                top: window.scrollY + 500,
            });
            """)



def movie_slider(endpoint: int, step: int, slider:WebElement ):



    current_position = int(slider.get_attribute("aria-valuenow"))

    if endpoint > current_position:
        offset = int ((endpoint-current_position)/step)
        slider.send_keys(Keys.ARROW_LEFT * offset)

    else:
        offset = int ((current_position- endpoint) / step)
        slider.send_keys(Keys.ARROW_LEFT * offset)

    final_position = int(slider.get_attribute("aria-valuenow"))

    print (f'Итоговое значение {final_position}')

    assert final_position == endpoint, "Слайдер на неверной позиции, проверьте шаг и значения"



movie_slider(8, 1,slider )

driver.quit()