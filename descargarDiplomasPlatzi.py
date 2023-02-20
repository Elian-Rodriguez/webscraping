from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from bs4 import BeautifulSoup
import time
import os

#UDUARIO A BUSCAR
#user=str(input("DIGITE EL USUARIO : "))
user=str(input('DIGITE EL ID DE USUARIO DE LA PLATFORMA ES EL TEXTO QUE SIGUE DESPUES DE "https://platzi.com/p/" : '))
usuario=str(input("DIGITE EL CORREO ELECTRONICO : "))
paswword=str(input("DIGITE LA CONTRASEÑA"))

webSc="https://platzi.com"

#CONFIGURACION DE ARCHIVO DE LOG O DE SALIDA
logging.basicConfig(format='%(message)s' ,filename=f'logs-urls-pruebas-{user}.txt', encoding='utf-8', level=logging.INFO)

#DEFINICIO DEL DRIVER DEL NAVEGADOR
edge_path = '.\edgedriver_win64\msedgedriver.exe'

#DEFINICION DE LA RUTA A CONSULTAR 
url = f"https://platzi.com/p/{user}/"
prefs = {"download.default_directory": os.getcwd()}


edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("prefs", prefs)
edge_options.use_chromium = True

driver = webdriver.Edge(executable_path=edge_path, options=edge_options)

driver.get(url)
time.sleep(7)
boton = driver.find_element("xpath",'/html/body/header/div/div[2]/div/div[4]/div/a')
boton.click()

time.sleep(7)
formulario = driver.find_element("xpath",'/html/body/div[3]/div/div/div/div/div[3]/form')
input_usuario = driver.find_element("xpath",'/html/body/div[3]/div/div/div/div/div[3]/form/div[2]/input')

input_usuario.send_keys(usuario)

input_password = driver.find_element("xpath",'/html/body/div[3]/div/div/div/div/div[3]/form/div[3]/input')
input_password.send_keys(paswword)
time.sleep(7)

botonIngreso= driver.find_element("xpath",'/html/body/div[3]/div/div/div/div/div[3]/form/button')
botonIngreso.click()

time.sleep(20)

driver.get(url)

time.sleep(10)

botonVerMas= driver.find_element("xpath",'/html/body/div[4]/div/div[2]/div/div[1]/div[1]/div[6]/div[2]/div/span')
botonVerMas.click()
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

Courses = soup.find_all(class_='Layout--radius icon-download Layout--roundBtn')

print(f"{Courses}")

count = 1
for course in Courses:
    print(f"{count}. {course}")
    course=str(str(course))
    course=str(course.replace('"',''))
    course=str(course.split("=")[-1])
    course=str(course.split(">")[0])
    print(f"{count}. {course}")

    urlcertificiacion=str(webSc+course)
    driver.get(urlcertificiacion)
    time.sleep(3)
    botonDescarga=driver.find_element("xpath",'/html/body/div[5]/div[3]/div[1]/div/div[2]/div[1]/form/button')
    botonDescarga.click()
    time.sleep(3)
    while not any(filename.endswith('.pdf') for filename in os.listdir(os.getcwd())):
        time.sleep(1)



    count+=1


time.sleep(30)
driver.quit()




"""
Importa las librerías necesarias para trabajar con Selenium, BeautifulSoup, logging, y os.
Pide al usuario que ingrese el ID de un usuario de la plataforma "Platzi", su correo electrónico y su contraseña.
Configura un archivo de registro para almacenar los resultados del script.
Configura las opciones para descargar automáticamente los archivos en la carpeta actual.
Define la ruta a la página web del usuario especificado.
Configura y ejecuta el controlador de Microsoft Edge y carga la página del usuario especificado.
Espera a que se cargue la página e inicia sesión en la plataforma con el correo electrónico y la contraseña proporcionados.
Espera a que se cargue la página y hace clic en el botón "Ver más" para mostrar todos los cursos del usuario.
Utiliza BeautifulSoup para buscar los enlaces de descarga de los certificados de los cursos.
Descarga automáticamente los certificados en formato PDF de cada curso y los guarda en la carpeta actual.
Cierra el navegador y finaliza el script.
En resumen, el script automatiza la descarga de los certificados de los cursos de un usuario específico en la plataforma "Platzi".

"""