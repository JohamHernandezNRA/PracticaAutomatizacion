from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service ("Driver/chromedriver.exe")
clave ="PORTATILES LENOVO GAMER"

driver = webdriver.Chrome(service=service)
driver.maximize_window()
time.sleep(2)

driver.get("https://www.mercadolibre.com.co/")
time.sleep(3)

cookies = driver.find_elements(By.PATH, '/html/body/div[2]/div[1]/div/div[3]/button[1]')
cookies.click()
time.sleep(3)

mastarde = driver.find_element(By.PATH, '/html/body/div[3]/div/div/div[2]/div/div/div[2]/button[2]/span')
mastarde.click()
time.sleep(3)

search = driver.find_element(By.PATH, '/html/body/header/div/div[2]/form/button/div')
search.click()
search.send_keys (clave)
time.sleep(3)

