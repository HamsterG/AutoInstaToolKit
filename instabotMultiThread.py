from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import time
import threading
#import unfollow

uname = "tots_pops_mark"
pswd = "Obermann1"
options = Options()
options.add_argument('-headless')
driver = Firefox(executable_path='geckodriver', options=options)
#driver2 = Firefox(executable_path='geckodriver', options=options)

def page():
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
	except:
		time.sleep(2)
	#driver.get("https://www.instagram.com/explore/tags/f4f")



def followReco():
	follow = driver.find_element_by_xpath("//html/body/span/section/main/section/div[3]/div[3]/div[2]/div/div/div/div[1]/div[3]/button").click()
	time.sleep(1)
	follow = driver.find_element_by_xpath("//html/body/span/section/main/section/div[3]/div[3]/div[2]/div/div/div/div[2]/div[3]/button").click()
	time.sleep(1)
	follow = driver.find_element_by_xpath("//html/body/span/section/main/section/div[3]/div[3]/div[2]/div/div/div/div[3]/div[3]/button").click()
	

def followBack():

	driver.get("https://www.instagram.com/accounts/activity/")

	flistx = driver.find_elements_by_xpath("//html/body/span/section/main")
	print(len(flist))
	for i in range(0,len(flist)):
		flist[i].click()			

def like():
	driver.get("https://www.instagram.com")
	time.sleep(3)

	l1 = driver.find_elements_by_xpath("//button[@class='dCJp8 afkep coreSpriteHeartOpen _0mzm-']")
	print(len(l1))
	for i in range(0, len(l1)):
		print(l1[i].click())
	time.sleep(2)

	driver.execute_script("window.scrollTo(0, 750)")
	time.sleep(5)
	l1 = driver.find_elements_by_xpath("//button[@class='dCJp8 afkep coreSpriteHeartOpen _0mzm-']")
	print(len(l1))
	for i in range(1, len(l1)):
		print(l1[i].click())
	time.sleep(3)


def runtime():
	while True:
		followReco()
		like()
		#exec(open("./unfollow.py").read())


page()
runtime()















				