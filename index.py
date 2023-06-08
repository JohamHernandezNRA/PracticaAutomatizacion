#Se llaman las librerias necesarias para la ejecución del proceso 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service ("Driver/chromedriver.exe") #Se ejecuta el driver de Chrome

driver = webdriver.Chrome(service=service)
driver.maximize_window()
time.sleep(2)

#Se habre la página a probar
driver.get("https://www.viajesexito.com/vuelos-baratos?utm_source=google-ads&utm_medium=cpc&utm_campaign=ao-marca&gclid=CjwKCAjw1YCkBhAOEiwA5aN4AYLcSSXwU7lhUeI7exmnRl6mHyRRJS7FwGLnCUfISPCQOvoQivEOKhoC2NAQAvD_BwE")
time.sleep(3)

#Se da clic al botón paquetes de vuelo
paquetes = driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]')
paquetes.click()
time.sleep(3)

ahorano = driver.find_element(By.XPATH, '/html/body/div[8]/div/div/div/div[2]/a[2]')
ahorano.click()
time.sleep(5)

#Se da clic al botón lugar de partida y se envía texto al campo 
lugarSalida = "Jose Maria Cordova"
origen = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
origen.click()
time.sleep(3)
origen.send_keys(lugarSalida)
time.sleep(3)

search = driver.find_element(By.PATH, '/html/body/header/div/div[2]/form/button/div')
search.click()
search.send_keys (clave)
time.sleep(3)

