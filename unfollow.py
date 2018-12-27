from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import time
import threading

uname = "tots_pops_mark"
pswd = "Obermann1"
options = Options()
#ptions.add_argument('-headless')
driver2 = Firefox(executable_path='geckodriver', options=options)
#driver3 = Firefox(executable_path='geckodriver', options=options)





def login():
	try:
		driver2.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
		time.sleep(2)
		username = driver2.find_element_by_name("username")
		password = driver2.find_element_by_name("password")
		username.send_keys(uname)
		password.send_keys(pswd)
		password.submit()
		time.sleep(2)
		driver2.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
		time.sleep(2)
	except:
		time.sleep(2)

def unfollowexec():

	driver2.get("https://www.instagram.com/tots_pops_mark/")
	driver2.find_element_by_xpath("//html/body/span/section/main/div/header/section/ul/li[3]/a").click()
	time.sleep(2)
	nb = driver2.find_elements_by_xpath("//div[@class='                  Igw0E   rBNOH        eGOV_     ybXk5    _4EzTm                                                                                   XfCBB          HVWg4                  _0mzm- ZUqME']")
	print(len(nb))

	for i in range(0,16):
		try:
			driver2.find_element_by_xpath("//button[@class='_0mzm- sqdOP  L3NKy   _8A5w5    ']").click()
			driver2.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
		except:
			time.sleep(2)
	driver2.find_element_by_xpath("//html/body/div[3]/div/div/nav/a[2]/button").click()
	time.sleep(2)
	driver2.find_element_by_xpath("//html/body/div[3]/div/div/nav/a[1]/button").click()
	time.sleep(len(nb)+5)
	driver2.refresh()
	time.sleep(600)


def countdown():
	time.sleep(600)
	unfollowexec()


login()
countdown()