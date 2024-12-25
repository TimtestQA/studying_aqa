import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement



class TestLogin:

    def setup_method(self):
        self.options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        self.options.add_argument("--window-size=1920,1080")
        # options.add_argument("--incognito")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.page_load_strategy = 'normal'

        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 10, 1)
        self.action = ActionChains(self.driver)

        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def test_autorization(self):

        USERNAME_FIELD = ("xpath", "//div/input[@name='username']")
        EMAIL_FIELD = ("xpath", "//div/input[@type='password']")
        SUBMIT_BUTTON = ("xpath", "//div/button[@type='submit']")
        USER_BLOCK = ("xpath", "//div[contains(@class, 'userarea')]")

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print(self.driver.title)
        self.wait.until(EC.visibility_of_element_located(USERNAME_FIELD), "Поле не активно").send_keys("Admin")
        self.wait.until(EC.visibility_of_element_located(EMAIL_FIELD), "Поле не активно").send_keys("admin123")
        self.wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON),"Кнопка не кликабельная").click()
        self.wait.until(EC.url_changes("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"), "Нет перехода со страницы логина")
        self.wait.until(EC.element_to_be_clickable(USER_BLOCK), "Вы не авторизованы")

    def test_logo_is_availablea(self):
        LOGO = ("xpath", "//a[@class='oxd-brand']")
        self.test_autorization()
        self.wait.until(EC.element_to_be_clickable(LOGO), "Лого не кликабельно").click()


    def teardown_method(self):
        print("After test use")
        self.driver.quit()

