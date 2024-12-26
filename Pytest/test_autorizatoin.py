
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import pytest


class TestAutorization:
    ERROR_MESSAGE_LOCATOR = ("xpath", "//div[contains(@class, 'll-modal-auth-alt__error')]")

    EMAIL_FIELD_LOCATOR = ("xpath", "//input[@type='text']")

    PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@type='password']")

    SUBMIT_BUTTON_LOCATOR = ("xpath", "//button[span[contains(text(), 'Войти в аккаунт')]]")


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
        self.action = ActionChains(self.driver)

        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        self.driver.get("https://lingualeo.com/ru/modules/auth/login")

    @pytest.mark.parametrize(
        "email, password, error_message, expected_result",
        [("newf-trainings@mak.ru","1234",None, True),
         ("jung_prodtes@mak.ru", "1234", None, True),
         ("jung_prodtes@mak.ru", "123400999", "Неправильный e-mail или пароль.", False)
         ]
    )
    def test_autorization(self, email, password, error_message, expected_result):

        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD_LOCATOR), "Поле email не активно или не найдено").send_keys(
            email, )

        self.driver.find_element(*self.PASSWORD_FIELD_LOCATOR).send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON_LOCATOR)).click()

        self.wait.until(EC.url_changes("https://city.lingualeo.com/training-lobby"))

        if not expected_result:
            assert self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE_LOCATOR)).text == error_message


    def teardown_methtod(self):
        self.driver.quit()
