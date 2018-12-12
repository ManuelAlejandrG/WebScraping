__author__='ManuelAlejandro'
#Librerías para usar
from bs4 import BeautifulSoup 
from langdetect import detect
import requests
import re
def funcion(URL):
     #Url que usaremos
    
    # Realizamos la petición a la web
    req = requests.get(URL)

    # Comprobamos  Status Code 
    status_code = req.status_code

    # Comprobamos con un condicional si la página fue cargada correctamente
    if status_code == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")

        # Obtenemos el parrafo donde están las entradas a scrapear
        entradas = html.find_all('p', {'class': 'ProfileHeaderCard-bio u-dir'} )
    
        for entrada in entradas:
       
            texto=entrada.getText()
            print(texto)
        
        
            #Detectar Idioma
            idma=detect(texto)
            #Detectar email
            mailsearch=re.compile(r'[\w\-\.]+@[\w\-\.]+\.+[a-zA-Z]{1,4}')
            for mail in mailsearch.findall(texto):
                email=mail
        
    
        if idma=="es":
                        idioma="español"
        elif idma=="en":
                        idioma="ingles"
        elif idma=="fr":
                        idioma="frances"
                                         
        print("i. Idioma: "+ idioma)
        print("ii. Email: "+ email) 
        print("iii. Telefono") 
        print("iv. URLs.")  
        print("Los url proporcionados en Twitter se tienen que activar  (ver si podemos ir a visitar la URL ) para obtener el destino y obtener información ya sea de usuario de youtube, instagram, etc. ") 
        print("1. ID Usuario Youtube") 
        print("2. Canal de Youtube") 
        print("3. ID Usuario Instagram")  
        print("4. Canal de Instagram")  
        print("5. Pagina Web Personal") 
        print("6. ID Usuario Facebook")  
        print("7. Otro. ¿? v. Otra información")
    
        
    else:
        print ("Status Code %d" % status_code)



#Para usar el programa, use la función llamada funcion
#como parametro, inserte entre comillas el url de una cuenta de twitter
#EJEMPLO: 

funcion("https://twitter.com/ManuelAlejandrG")
