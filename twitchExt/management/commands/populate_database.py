import csv
import re
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

CSV_COMMENT_PATTERN = re.compile(r'\s*#.*$')

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
        with open('artists.csv', 'r') as csvfile:
            for row in csv.DictReader(skip_comments(csvfile)):
                artistname = row.get("artistname")
                artistid = row.get("artistsid")
                total_tracks = row.get("Total tracks")


