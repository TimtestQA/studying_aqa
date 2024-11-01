import os.path
import time
from selenium import webdriver
from selenium.webdriver import Keys
import platform


os_name = platform.system()

UNIVERSAL_CTRL = Keys.COMMAND if os_name == 'darwin' else Keys.CONTROL

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

preferences = {
    "download.default_directory" : os.path.join(os.getcwd(), "download")
}

options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/upload-download")

UPLOAD_FILE_FIELD = driver.find_element("xpath", "//input[@type='file']")

UPLOAD_FILE_FIELD.send_keys(os.path.join(os.getcwd(), "Uploadtest.py"))

time.sleep(2)


driver.get("http://the-internet.herokuapp.com/download")

time.sleep(2)
input()
print("Количество файлов для скачивания", len(driver.find_elements("xpath","//div//a[contains(@href, 'download')]")))

DOWNLOAD_FILES = driver.find_elements("xpath","//div//a[contains(@href, 'download')]")

for file in DOWNLOAD_FILES:
    file.click()

driver.close()



