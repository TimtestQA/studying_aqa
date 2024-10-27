import time
from selenium import webdriver
from selenium.webdriver import Keys
import platform

os_name = platform.system()

UNIVERSAL_CTRL = Keys.COMMAND if os_name == 'darwin' else Keys.CONTROL

driver = webdriver.Chrome()

MAIN_PAGE = driver.get("https://demoqa.com/text-box")

user_name= driver.find_element("xpath", "//input[@id='userName']")
time.sleep(2)

user_name.clear()

assert user_name.get_attribute("value") == "","Поле не пустое"

user_name.send_keys("John")


assert user_name.get_attribute("value") == "John", "Неверное имя пользователя"


email = driver.find_element ("xpath", "//input[@id='userEmail']")

email.clear()


assert email.get_attribute("value")== "","Поле не пустое"

email.send_keys("test.hobbit@gmail.com")

assert email.get_attribute("value") == "test.hobbit@gmail.com", "Неверный email"


current_address = driver.find_element ("xpath", "//div/textarea[@id='currentAddress']")

current_address.clear()

assert current_address.get_attribute("value")== "","Поле не пустое"

current_address.send_keys("Shire, Hobbiton, Bag End")

assert current_address.get_attribute("value") == "Shire, Hobbiton, Bag End", "Адрес верный"


permanent_address = driver.find_element ("xpath", "//div/textarea[@id='permanentAddress']")


permanent_address.clear()

assert permanent_address.get_attribute("value") == "", "Поле не пустое"

permanent_address.send_keys("Middleeart")

assert permanent_address.get_attribute("value") == "Middleeart"

time.sleep(3)

# Задание 2

SECOND_PAGE = driver.get(" https://the-internet.herokuapp.com/login")

USER_LOGIN = "tomsmith"
USER_PASSWORD = "SuperSecretPassword!"

LOGIN_BUTTON = ("xpath", "//button[@class='radius' and @type='submit']")

LOGOUT_BUTTON = ("xpath", "//a[normalize-space()='Logout']")

USERNAME_FIELD = driver.find_element("xpath", "//input[@id='username']")

USERNAME_FIELD.clear()

assert USERNAME_FIELD.get_attribute("value") == "", "Поле Username не пустое"

USERNAME_FIELD.send_keys(USER_LOGIN)

assert USERNAME_FIELD.get_attribute("value") == USER_LOGIN, "Неверный логин"

PASSWORD_FIELD = driver.find_element("xpath", "//input[@id='password']")

PASSWORD_FIELD.clear()

assert PASSWORD_FIELD.get_attribute("value") == "", "Поле Password не пустое"

PASSWORD_FIELD.send_keys(USER_PASSWORD)

assert PASSWORD_FIELD.get_attribute("value") == USER_PASSWORD, "Неверный пароль"

driver.find_element(*LOGIN_BUTTON).click()

time.sleep(5)


assert driver.find_element(*LOGOUT_BUTTON), 'Юзер не авторизован, кнопки Logout нет'


driver.close()