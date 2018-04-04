import sys
import  urllib
from bs4 import BeautifulSoup
import json
from random import randint
import requests
import subprocess
import imghdr
from urllib.request import Request, urlopen
import ctypes

SEARCH_NAME = "motivation"
SEARCH_NAME +=" HD DESKTOP WALLPAPER"
SEARCH_NAME = SEARCH_NAME.replace(' ','+')

#prepare google search url
SEARCH_URL = "https://www.google.co.in/search?q={}&source=lnms&tbm=isch&tbs=isz:ex,iszw:1920,iszh:1080".format(SEARCH_NAME)
print(SEARCH_URL)

#path for storing the photo
PHOTO_PATH = 'D:\\Py\\WallpaperChangephoto.jpg'

#manipulate user agent so as to make them believe we are just normal human downloading some image
hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#make a request and get html in beautiful suop
#req = urllib2.Request(SEARCH_URL,headers=hdr)
req = Request(SEARCH_URL)
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36");
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')


#scrap the html to find link of image (just refer to html printed in above prettify line to find what html google returns)
#google image will give us total 99 images (I think), just pick one randomly. And hope for the best.
invalid_jpeg = True
while invalid_jpeg:
	for child in soup.find("div", {"data-ri":"{}".format(str(randint(0,99)))}).find("div", {"class":"rg_meta"}).children:
	    data_content = json.loads(child)
	    LINK = data_content["ou"]
	     #dowload the photo 
	    print(LINK)
	 	 
	 	
	res = requests.get(LINK, headers=hdr)
	with open(PHOTO_PATH, 'wb') as W:
		W.write(res.content)
	     
	#check if photo is valid, if not, try another photo, keep trying until you get one		
	invalid_jpeg = (imghdr.what(PHOTO_PATH)!="jpeg")



#set as wallpaper
print("Setting wallpaper:",PHOTO_PATH)
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PHOTO_PATH , 0)
