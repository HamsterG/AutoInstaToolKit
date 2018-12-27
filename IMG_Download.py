import urllib.request 
from bs4 import BeautifulSoup 
from urllib.request import urlopen as uReq
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import time
import threading
import random

uname = input('What Agent To Use: ')
pswd = input('Agent Password: ')
options = Options()
options.add_argument('-headless')
driver = Firefox(executable_path='geckodriver', options=options)

usr = input('Username: ')

def login():
	try:
		driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
		time.sleep(2)
		username = driver.find_element_by_name("username")
		password = driver.find_element_by_name("password")
		username.send_keys(uname)
		password.send_keys(pswd)
		password.submit()
		time.sleep(2)
		driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
		time.sleep(2)
		driver.get('https://instagram.com/'+usr)
	except:

		pass

def scroll():
	# Get scroll height
	last_height = driver.execute_script("return document.body.scrollHeight")

	while True:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height
    	

def test():
	fn = 1
	src_list = []
	scroll()
	x = driver.find_elements_by_tag_name('img')
	for element in x:
		xxx = len(src_list) -1
		src_list.append(element.get_attribute('src'))
		print(src_list[xxx])
		file_name = usr + str(fn)
		fn = fn + 1
		full_file_name = str(file_name) + '.jpg'
		for i in range(0, len(src_list)):
			urllib.request.urlretrieve(src_list[i],'images/'+full_file_name)



login()
test()
driver.close()