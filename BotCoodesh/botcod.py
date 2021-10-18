from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import autoit
import pyautogui
from selenium.webdriver import ActionChains



driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
driver.get("https://beta.coodesh.com/")
assistente = driver.find_element_by_xpath("/html/body/div[1]/header/div/div/nav/div[2]/ul/li[1]/a").click()
time.sleep(4)
driver.find_element_by_name("search").send_keys("PiedPiper")
driver.find_element_by_name("search").send_keys(Keys.RETURN)  
driver.refresh()
time.sleep(2)

selecionavaga = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/a[1]/div/div/div[2]/div[1]/div/h1").click()

time.sleep(4)
candidatar = driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div/div/button").click()

# Cadastro para vaga
driver.find_element_by_id("fullname").send_keys("Bruno Rocha")
driver.find_element_by_id("email").send_keys("bruno.rcontato@gmail.com")
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/form/div/div[3]/div[1]/input").send_keys("98109518")
time.sleep(1)
driver.find_element_by_id("contact_preference").send_keys("w")
driver.find_element_by_id("contact_preference").send_keys(Keys.RETURN) 
driver.find_element_by_id("contact_hour").send_keys("10")
time.sleep(2)
driver.find_element_by_id("city").send_keys("Fortaleza")
driver.find_element_by_id("contact_hour").send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='salary_range.max']").send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='salary_range.max']").send_keys("\ue012")
driver.find_element_by_xpath("//*[@id='salary_range.max']").send_keys("\ue012")
driver.find_element_by_xpath("//*[@id='salary_range.max']").send_keys("\ue012")
driver.find_element_by_xpath("//*[@id='salary_range.max']").send_keys("\ue012")
driver.find_element_by_xpath("//*[@id='salary_range.max']").send_keys(2000)
driver.find_element_by_id("linkedin").send_keys("https://www.linkedin.com/in/brunorochatic/")
driver.find_element_by_id("linkedin").send_keys(Keys.RETURN) 
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/form/div/div[15]/div/button").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/section/div/div/div[1]/button").click()
time.sleep(4) # esperar para que a janela do windows abra
pyautogui.write(r"teste.pdf") #path of File
pyautogui.press('enter')
time.sleep(3)
aceite = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/form/div/div[16]/div/label/span").click()
#aceite.send_keys("\ue00d")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button").click()
print("teste finalizado com sucesso")
