import os
import csv
import re
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from api.models import Artist

class Command(BaseCommand):
    help = 'Update the database with spotify genre'

    def handle(self, *args, **options):
        for artist in Artist.objects.all():

