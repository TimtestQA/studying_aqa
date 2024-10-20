import time
from selenium import webdriver


driver = webdriver.Chrome()



VK_URL = driver.get("https://vk.com/")
VK_TITLE = driver.title
VK_URL = driver.current_url

print(VK_TITLE)

driver.get("https://google.com/")

GOOGLE_TITLE = driver.title

print(GOOGLE_TITLE)

driver.back()

assert VK_URL == "https://vk.com/","Вы не вернулись назад к VK.COM"

assert driver.title == VK_TITLE, "Title не соответствует"

driver.refresh()

print(driver.current_url)


driver.forward()
time.sleep(3)

assert driver.current_url is not VK_URL, "Переход вперед не удался"