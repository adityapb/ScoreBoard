import urllib
import json

def score():
	page = urllib.urlopen('http://pipes.yahoo.com/pipes/pipe.run?_id=tMcVGcqn3BGvsT__2R2EvQ&_render=json')
	jsonObj = json.load(page)
	data = []
	for dict in jsonObj["value"]["items"]:
		data.append(dict["title"])
	return data