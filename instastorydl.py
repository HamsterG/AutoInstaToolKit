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

uname = 'theswen___'#input('What Agent To Use: ')
pswd = 'Obermann1'#input('Agent Password: ')
options = Options()
#options.add_argument('-headless')
driver = Firefox(executable_path='geckodriver', options=options)

usr = 'pornhub'#input('Username: ')

def login():
	try:
		driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
		time.sleep(2)
		username = driver.find_element_by_name("username")
		password = driver.find_element_by_name("password")
		username.send_keys(uname)
		password.send_keys(pswd)
		password.submit()
		# time.sleep(5)
		# driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
		time.sleep(4)
		driver.get('https://instagram.com/'+usr)
		time.sleep(4)

	except:

		pass

def findstory():
	driver.find_element_by_class_name("_6q-tv").click()
	time.sleep(5)
	find_media()


def find_media():

	for i in range(0,99):
		try:
			video_media = driver.find_elements_by_tag_name('video')
			pic_media = driver.find_elements_by_tag_name('img')
			time.sleep(15)
		except:
			print(video_media)
			print(pic_media)
def download():
	urllib.request.urlretrieve(src_list[i],'images/'+full_file_name)



login()
findstory()
time.sleep(10)
driver.quit()
