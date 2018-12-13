from selenium import webdriver
 
from bs4 import BeautifulSoup
 
browser = webdriver.PhantomJS("/home/desarrollo10/Downloads/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
 
browser.get("https://www.python.org/")
 
page = BeautifulSoup(browser.page_source,"html5lib")
slide = page.find("div",{'class':'slide-copy'}).select("p")
print(slide)
