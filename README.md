# webscraping
 
El código es un script de Python que usa la biblioteca Selenium para automatizar la navegación web y extraer información de una página web específica. El script inicia una sesión de Selenium con Microsoft Edge, accede a una página web determinada, extrae el HTML de la página y utiliza BeautifulSoup para analizar el HTML. Luego, el script busca todos los elementos que tengan la clase 'Course-title' y 'Career-title' y extrae el contenido de cada elemento encontrado. Finalmente, el script imprime el contenido de cada elemento encontrado y lo escribe en un archivo de registro.

En resumen, el script se utiliza para extraer y registrar información sobre los cursos y las carreras completadas por un usuario específico en la plataforma educativa Platzi.


# habilidades en el manejo de tecnologías y herramientas como:

Selenium y webdriver: permiten la automatización de la interacción con sitios web y la navegación por las diferentes páginas y secciones, facilitando la extracción de información de manera eficiente.

BeautifulSoup: facilita la extracción de información específica de un sitio web a través del análisis del HTML.

Trabajo con archivos y directorios: la creación y escritura de archivos, junto con la manipulación de directorios, permite almacenar y organizar la información extraída.

Manejo de excepciones: el manejo de excepciones en Python permite controlar errores y tomar acciones específicas en caso de que se produzca alguno, mejorando la robustez y fiabilidad del programa.

Conocimientos básicos de programación: el uso de estructuras de control de flujo, el manejo de variables y la lógica de programación son fundamentales para la creación de scripts eficientes y eficaces.


#Script de Python para obtener los cursos y carreras completadas por un usuario en Platzi
Este script utiliza la biblioteca Selenium para abrir un navegador, navegar a la página de perfil de un usuario en Platzi y obtener la lista de cursos y carreras completados por ese usuario.

#Requisitos
Python 3.x
Biblioteca Selenium
Biblioteca BeautifulSoup
#Uso
Descargue y extraiga el archivo de Microsoft Edge Driver para su sistema operativo y versión de Microsoft Edge desde: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Instale las bibliotecas necesarias utilizando pip: pip install selenium y pip install beautifulsoup4
Ejecute el script usando el comando python platzi_courses.py
Digite el nombre de usuario que desea buscar
El script creará un archivo de texto con el nombre del usuario y una lista de los cursos y carreras completados por ese usuario. El archivo se guardará en el directorio desde el cual se ejecuta el script.
