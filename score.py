import urllib
from bs4 import BeautifulSoup

def score():
	page = urllib.urlopen('http://static.cricinfo.com/rss/livescores.xml')
	xml_obj = BeautifulSoup(page);
	data = xml_obj.read().find_all('title')
	for i in range(len(data)):
		data[i].replace("<title>", "")
		data[i].replace("</title>", "")
	return data