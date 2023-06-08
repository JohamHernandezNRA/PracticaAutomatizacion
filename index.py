#Se llaman las librerias necesarias para la ejecución del proceso 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

#Se marca el "Ahora no" del Alert del éxito
ahoraNo = driver.find_element(By.XPATH, '/html/body/div[8]/div/div/div/div[2]/a[2]')
ahoraNo.click()
time.sleep(5)

#Se da clic al botón lugar de partida y se envía texto al campo 
lugarSalida = "Jose Maria Cordova"
origen = driver.find_element(By.ID, "CityPredictiveFrom_netactica_airhotel")
origen.click()
time.sleep(3)
textoOrigen = driver.find_element(By.ID, "popUpCityPredictiveFrom_netactica_airhotel")
textoOrigen.send_keys(lugarSalida)
textoOrigen.send_keys(Keys.ENTER) #Se da Enter para ingresar el texto
time.sleep(3)

#Se da clic al botón destino de partida y se envía texto al campo
lugarDestino = "cancun"
destino = driver.find_element(By.ID, "CityPredictiveTo_netactica_airhotel")
destino.click()
time.sleep(3)
textoDestino = driver.find_element(By.ID, "popUpCityPredictiveTo_netactica_airhotel")
textoDestino.send_keys(lugarDestino)
textoDestino.send_keys(Keys.ENTER)
time.sleep(3)

#Se da clic en huéspedes y se seleccionan cantidades 
huespedes = driver.find_element(By.ID, "txtNumPassengersPaquetesComplete")
huespedes.click()
time.sleep(3)
#Se agrega habitación
agregarHabitacion = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]")
agregarHabitacion.click()
time.sleep(3)
#Se da clic al botón de aplicar de las habitaciones
botonAplicar = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button")
botonAplicar.click()
time.sleep(3)

#Se da clic al botón de fechas y se seleccionan las fechas indicadas 
fechas = driver.find_element(By.ID, "Date_netactica_air_hotel")
fechas.click()
time.sleep(3)
#Seleccionar fecha de salida
fechaSalida = driver.find_elements(By.CLASS_NAME, "mbsc-calendar-cell-text mbsc-calendar-day-text mbsc-ios")
fechaSalida[3].click()
time.sleep(3)
fechaRegreso = driver.find_element(By.XPATH, "/html/body/div[10]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[4]/div[2]")
fechaRegreso.click()
time.sleep(3)

#Se da clic al botón de buscar viajes
buscar = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a")
buscar.click()
time.sleep(3)

driver.close() #Se cierra la ventana de ejecución
driver.quit() #Se cierra el controlador y se cierran todas las ventanas asociadas