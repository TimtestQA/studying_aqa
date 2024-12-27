import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestJoke:
    POST_FIELD = ("xpath", "//textarea[contains(@class, 'input')]")
    POSTED_BUTTON = ("xpath", "//button[normalize-space()='Post']")
    USERNAME_FIELD = ("xpath", "//div/input[@name='username']")
    EMAIL_FIELD = ("xpath", "//div/input[@type='password']")
    SUBMIT_BUTTON = ("xpath", "//div/button[@type='submit']")
    USER_BLOCK = ("xpath", "//div[contains(@class, 'userarea')]")


    def setup_method(self):

        self.options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        self.options.add_argument("--window-size=1920,1080")
        # self.options.add_argument("--incognito")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.page_load_strategy = 'normal'

        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 10, 1)

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD), "Поле не активно").send_keys("Admin")
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD), "Поле не активно").send_keys("admin123")
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON), "Кнопка не кликабельная").click()
        self.wait.until(EC.url_changes("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"),
                        "Нет перехода со страницы логина")
        self.wait.until(EC.element_to_be_clickable(self.USER_BLOCK), "Вы не авторизованы")

    def test_post_joke(self, get_joke):

        self.wait.until(EC.element_to_be_clickable(self.POST_FIELD), "Поле не кликабельно").send_keys(get_joke)
        self.wait.until(EC.element_to_be_clickable(self.POSTED_BUTTON), "Кнопка не доступна").click()
        self.wait.until(EC.visibility_of_element_located(("xpath", "//div/p[text()='Success']")),"Нет попапа успеха")
        self.wait.until(EC.invisibility_of_element(("xpath", "//div/p[text()='Success']")),"Попап не исчез")
        joke_text = self.wait.until(EC.element_to_be_clickable(("xpath", "(//div/p[@class='oxd-text oxd-text--p orangehrm-buzz-post-body-text'])[1]"))).text

        self.wait.until(EC.text_to_be_present_in_element(
            ("xpath", "(//div/p[@class='oxd-text oxd-text--p orangehrm-buzz-post-body-text'])[1]"), get_joke))

        assert joke_text == get_joke, "Шутка не запостилась"






    def teardown_method(self):
        self.driver.quit()


