import os
import csv
import requests
import re
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from api.models import Artist

CSV_COMMENT_PATTERN = re.compile(r'\s*#.*$')

GENRES = ["rock", "pop", "vocals", "soul", "jazz", "country", "ensembles", "instrumental", "funk", "blues", "salsa", "banda", "musicals", "disco", "swing", "r&b", "opera", "wing", "tejano", "metal", "bop"]


class Command(BaseCommand):
    help = 'Creates the initial database'

    def handle(self, *args, **options):

        def skip_comments(lines):
            """
            A filter which skip/strip the comments and yield the
            rest of the lines

            :param lines: any object which we can iterate through such as a file
                object, list, tuple, or generator
            """

            for line in lines:
                line = re.sub(CSV_COMMENT_PATTERN, '', line).strip()
                if line:
                    yield line

        self.stdout.write(self.style.SUCCESS('Starting db creation'))
        genres = {}
        with open(os.path.join(settings.BASE_DIR, 'genres.csv'), 'r') as csvfile:
            for row in csv.reader(csvfile):
                for word in row[-1].lower().split():
                    if word in GENRES:
                        genres[row[0]] = word
                        break

        with open(os.path.join(settings.BASE_DIR, 'artists.csv'), 'r') as csvfile:
            for row in csv.DictReader(csvfile):
                name = row.get("artistname")
                artist_id = row.get("artistid")
                if not artist_id:
                    print name
                csv_data = {
                    "name": name,
                    "artist_id": artist_id,
                    "total_tracks": row.get("Total tracks")
                }
                # popularity, image
                artist, created = Artist.objects.get_or_create(**csv_data)
                if created:
                    try:
                        artist.genre.add(genres[name])
                    except:
                        print "failed to fined the artist with name %s" % name
                        try:
                            headers = {
                                'Accept': 'application/json',
                                'content-type': 'application/json',
                                'Authorization': 'Bearer BQAKgSOEMf7MjH-hV-Bdur_q3xv0B6XC_erFV32y4vBmOGyFVMxNRJRAqOasLpEQJUDTQ7MvNv06kxnami1XoFsCrR16rOfdOwKfD4ilhCW1kg4zzOmrhY9dTVXSIYf7QsbAHc8jcujdma3htRFI9A'
                            }
                            r = requests.get("https://api.spotify.com/v1/search?q=%s&type=artist" % name, headers=headers)
                            if r.status_code == 200:
                                genres = r.json()["artists"]["items"][0]["genres"]
                                genres = " ".join(genres).lower().split()
                                for word in genres:
                                    if word in GENRES:
                                        artist.genre.add(genres[name])
                                        break
                        except Exception as e:
                            print "failed to fined the genre on spotify for artist %s" % name
