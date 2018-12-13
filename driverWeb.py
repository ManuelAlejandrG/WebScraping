from selenium import webdriver
 
browser = webdriver.Chrome("/home/desarrollo10/Downloads/chromedriver_linux64/chromedriver")
 
browser.get("https://www.python.org/")
 
nav = browser.find_element_by_id("mainnav")
 
print(nav.text)
