import requests
import xml.etree.ElementTree as ET
from Song import Song
import csv
import sqlite3

def getArtists():
	with open('Artists.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for i in range(1237):
			next(reader)
		for row in reader:
			x = row[1]
			try:	
				int(x)
				get(x)
			except ValueError:
				get(row[2])

def get(artistId):
	conn = sqlite3.connect('song.db')
	c = conn.cursor()
	nonce = True
	page = 1
	pops = []
	totalpop = 0
	while nonce:
		url = 'http://api.7digital.com/1.2/artist/toptracks?shopId=2020&oauth_consumer_key=7d4vr6cgb392&artistId=' + str(artistId) + '&usageTypes=adsupportedstreaming&pagesize=50&page=' + str(page)
		r = requests.get(url)
		tree = ET.fromstring(r.text)
		for child in tree:
			children = child.findall('track')
			if len(children) < 50:
				nonce = False
			for x in children:
				data = [artistId, x.attrib['id'], x.find('title').text, x.find('duration').text, x.find('explicitContent').text, x.find('popularity').text]
				print(data)
				c.execute("insert into songs(artistid, id, title, duration, explicitContent, popularity) values (?, ?, ?, ?, ?, ?)", (data[0],data[1],data[2],data[3],data[4], data[5]))
		page += 1
	conn.commit()

def normalize(val):
	conn = sqlite3.connect('song.db')
	c = conn.cursor()
	c.execute("update songs set normalizedPopularity = (?)")

def createSongDb():
	conn = sqlite3.connect('song.db')
	c = conn.cursor()
	c.execute("create table songs(artistid, id, title, duration, explicitContent, popularity);")
# createSongDb()
getArtists()