import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://testautomationpractice.blogspot.com/')

driver.find_element('class name','wikipedia-search-wiki-link' )
driver.find_element('id', 'Wikipedia1_wikipedia-search-input')
driver.find_element('css selector', '.wikipedia-search-button')
input_field = driver.find_element('tag name', 'input')
input_fields = driver.find_elements('tag name', 'input')

