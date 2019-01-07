from selenium import webdriver
from urllib.request import urlopen
 
from bs4 import BeautifulSoup
 
browser = webdriver.Chrome("/home/desarrollo10/Downloads/chromedriver_linux64/chromedriver") #ubicación del webdriver 
 
browser.get("https://pobdirectory.com/directory/") #url 
nombres=browser.find_elements_by_tag_name("td") 
lista=[]
for nombre in nombres:
    
    lista.append(nombre.text)

        
