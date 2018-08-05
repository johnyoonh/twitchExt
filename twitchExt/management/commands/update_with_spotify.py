import os
import csv
import re

import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from api.models import Artist

class Command(BaseCommand):
    help = 'Update the database with spotify genre'

    def handle(self, *args, **options):
        for artist in Artist.objects.all():
            url = 'http://api.7digital.com/1.2/artist/toptracks?shopId=2020&oauth_consumer_key=7d4vr6cgb392&artistId=' + artist_id + '&usageTypes=adsupportedstreaming&pagesize=50&page=1'
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
