from urllib.request import urlopen
import xml.etree.ElementTree

html = urlopen("http://api.7digital.com/1.2/artist/browse?shopId=2020&oauth_consumer_key=7d4vr6cgb392&letter=a&pagesize=50&page=1")
e = xml.etree.ElementTree.parse(html.read()).getroot()
print(e.head())