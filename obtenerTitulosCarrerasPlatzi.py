from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from bs4 import BeautifulSoup

#UDUARIO A BUSCAR
user=str(input("DIGITE EL USUARIO : "))
#user='elianeduardor451'


#CONFIGURACION DE ARCHIVO DE LOG O DE SALIDA
logging.basicConfig(format='%(message)s' ,filename=f'{user}.txt', encoding='utf-8', level=logging.INFO)

#DEFINICIO DEL DRIVER DEL NAVEGADOR
edge_path = '.\edgedriver_win64\msedgedriver.exe'

#DEFINICION DE LA RUTA A CONSULTAR 
url = f"https://platzi.com/p/{user}/"

#Configuracion de opciones de Edge
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True

# Inicia una sesión de Selenium con Edge
driver = webdriver.Edge(executable_path=edge_path, options=edge_options)

# Accede a una página web
driver.get(url)

# Obtener el HTML de la página cargada
html = driver.page_source

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html, 'lxml')

# Buscar todos los elementos que tengan la clase 'mi-clase'
Courses = soup.find_all(class_='Course-title')



# Imprimir el contenido de cada elemento encontrado.
logging.info(f"-- CURSOS REALIZADOS POR {user}")
count = int(1)
for Course in Courses:
    print(f"{count}. {Course.text} .")
    logging.info(f"--- {count}. {Course.text}")
    count+=1

logging.info(f"-- CARRERAS COMPLETADAS POR  {user}")
count = int(1)

Carreras = soup.find_all(class_='Career-title')
for carrera in Carreras:
    print(f"{count}. {carrera.text} .")
    logging.info(f"--- {count}. {carrera.text}")
    count+=1

driver.quit()
"""
El código es un script de Python que usa la biblioteca Selenium para automatizar la navegación web y extraer información de una página web específica. El script inicia una sesión de Selenium con Microsoft Edge, accede a una página web determinada, extrae el HTML de la página y utiliza BeautifulSoup para analizar el HTML. Luego, el script busca todos los elementos que tengan la clase 'Course-title' y 'Career-title' y extrae el contenido de cada elemento encontrado. Finalmente, el script imprime el contenido de cada elemento encontrado y lo escribe en un archivo de registro.

En resumen, el script se utiliza para extraer y registrar información sobre los cursos y las carreras completadas por un usuario específico en la plataforma educativa Platzi.
"""