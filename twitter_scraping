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
            
            email = re.findall(r'[\w\.-]+@[\w\.-]+', texto)
            
            telefono = re.findall(r'\(\+[0-9\-){1,9}]+', texto)
        
    
            id_instagram = re.findall(r'INSTAGRAM: [\w\.-]+', texto)
            id_instagram += re.findall(r'Instagram-[\w\.]+', texto)
            id_instagram += re.findall(r'IG: [\w\.]+', texto)
            id_instagram += re.findall(r'Insta: https://[\w\.-/]+', texto)
            id_instagram += re.findall(r' @[\w\.]+', texto)
            
            canal_instagram = re.findall(r'Snapchat: [\w\.-]+', texto)
                
            url = re.findall(r'https://[\w\.-/]+',texto)
            
            contacto = re.findall(r'CONTACTO+', texto)
            contacto += re.findall(r'Contacto+', texto)
            contacto += re.findall(r'contacto+', texto)
            facebook= re.findall(r'FACEBOOK: [\w\.-]+', texto)
            facebook+= re.findall(r'Facebook: [\w\.-]+', texto)
            facebook+= re.findall(r'facebook: [\w\.-]+', texto)
            facebook+= re.findall(r'FB: [\w\.-]+', texto)
            facebook+= re.findall(r'Fb: [\w\.-]+', texto)
            facebook+= re.findall(r'fb: [\w\.-]+', texto)
            
            youtube = re.findall(r'#[\w\.-]+', texto)
            
        if idma=="es":
                        idioma="español"
        elif idma=="en":
                        idioma="ingles"
        elif idma=="fr":
                        idioma="frances"
        else:
                        idioma="no se reconoce"
        
       
        
        Locations = html.find_all('span', {'class': 'ProfileHeaderCard-locationText u-dir'} )
        
        y = html.find_all('span', {'class': 'ProfileHeaderCard-urlText u-dir'} )



        for pais in Locations:
            print("0. Pais: "+ pais.getText())
                                         
        print("i. Idioma: "+ idioma)
        for n in email:
            
            print("ii. Email: " + n) 
        for n  in telefono:
            
            print("iii. Telefono: "+ n) 
        for n in url:
            
            print("iv. URLs: "+ n)  
        for n in y:
          print("1. Usuario de Youtube: "+ n.getText())

        for n in youtube:
                
            print("2. Canal de Youtube: " + n) 
        for n in id_instagram:
            
            print("3. ID Usuario Instagram: " + n)  
        for n in canal_instagram:
            
            print("4. Canal de Instagram: " + n)  
        for n in contacto:
            
            print("5. Pagina Web Personal: "+ n) 
        for n in facebook:
            print("6. ID Usuario Facebook: "+ n)
        
    
        
    else:
        print ("Status Code %d" % status_code)


