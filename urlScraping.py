from urllib.request import urlopen
 
from bs4 import BeautifulSoup
import pandas as pd
def scraping(url,document,div_class)

	html = urlopen(url)
#browser = webdriver.PhantomJS('/home/desarrollo10/Downloads/phantomjs-2.1.1-linux-x86_64/bin/phantomjs') 



 
	page = BeautifulSoup(html.read(),"html5lib")

	lista = []

	nav = page.findAll("div",{"class":"div_class"})
#print(nav.getText())
	for correos in nav:
		lista.append(correos.getText())
#print(lista)
#print(lista)
	Lista=pd.DataFrame(lista, columns=["Correos Chile"])

	

	Lista.to_csv("document.csv")

 
