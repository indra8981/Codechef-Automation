import requests,bs4,selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time, os

def setup():
	dir = r"C:\Users\HP\Desktop\chromedriver_win32"
	chrome_driver_path = dir + "\chromedriver.exe"
	#options = webdriver.ChromeOptions ()
	#options.add_argument ('headless')
	driver = webdriver.Chrome (chrome_driver_path)#options=options)
	#driver.maximize_window ()
	return driver

language=["C++14 (gcc 6.3)","JAVA (HotSpot 8u112)"]

def click(xpath,driver):
	for i in range (10):
		try:
			zz = driver.find_element_by_xpath (xpath)
			zz.click ()
			break
		except Exception as e:
			time.sleep (0.5)

def start(path,lang):
	driver=setup()
	file = open (path,"r")
	#print(file.read())
	url="https://www.codechef.com/ide"
	driver.get(url)

	click("//*[@id='gdpr-cookie-notif']",driver)

	click("//*[@id='gdpr-i-love-cookies']",driver)

	click("/html/body/center/center/table/tbody/tr/td/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[1]/div[4]/div[1]/label",driver)


	language_selector= driver.find_element_by_class_name ("language_selector")
	language_selector.click()


	search_box=driver.find_element_by_xpath('//*[@id="ember387_chosen"]/div/div/input')
	search_box.send_keys(lang)


	option=driver.find_element_by_class_name("chosen-results")
	option.click()

	ff=driver.find_elements_by_class_name("ace_text-input")[0]
	ff.clear()
	'''code_text=driver.find_element_by_class_name("ace_content")
	code_text.click()
	code_text.sendKeys (Keys.CONTROL + "a")'''

	driver.implicitly_wait (200)
	zz=file.read()
	ff.send_keys(zz)


	for i in range(1111111111111111):
		time.sleep(1)

start(r"C:\Users\HP\Desktop\test.txt","c++")