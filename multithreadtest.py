import urllib.request 
from bs4 import BeautifulSoup 
from urllib.request import urlopen as uReq

url = "https://www.instagram.com/model_roz"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")

img = soup.find('img')
print(img)
# print(img['src'])
