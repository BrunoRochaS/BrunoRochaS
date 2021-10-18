from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
driver.get("https://www.google.com.br")
driver.find_element_by_name("q").send_keys("Bruno Rocha")
driver.find_element_by_name("q").send_keys(Keys.RETURN)

