import urllib2

import requests
from django.conf import settings
from django.contrib.auth.models import Group
from django.core.files.base import ContentFile
from django.core.mail import send_mail
from django.db import models
from taggit.models import TagBase, \
    TaggedItemBase
from taggit.managers import TaggableManager
from versatileimagefield.fields import VersatileImageField


class Genre(TagBase):
    card_image = VersatileImageField(upload_to='media', blank=True,
                                     verbose_name='Card Image')

    # eKey to be used for determine the uploaded image name
    @property
    def ekey(self):
        return self.slugify(self.name)

    def save(self, *args, **kwargs):
        ret = super(Genre, self).save(*args, **kwargs)
        if not self.card_image:
            slug = self.slugify(self.name)
            flickr_url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=f0edd3f9c4ea875b21cb7015c1b78434&text={slug}&license=5%2C6%2C7%2C8%2C9%2C10&sort=relevance&safe_search=1&content_type=1&media=photos&extras=url_b&format=json&nojsoncallback=1".format(**{"slug":slug})
            r = requests.get(flickr_url)
            rJson = r.json()
            photoObject = rJson["photos"]["photo"][0]
            original_name = "{id}_{secret}_b.jpg".format(**photoObject)
            url = "http://farm{farm}.staticflickr.com/{server}/{id}_{secret}_b.jpg".format(**photoObject)
            content = urllib2.urlopen(url).read()
            ret = self.card_image.save(original_name, ContentFile(content))
        return ret

class TaggedGenre(TaggedItemBase):
    tag = models.ForeignKey(Genre,
                            related_name="%(app_label)s_%(class)s_items")
    # null is set to allow other models to refer to it
    # but those models relationship will be filtered out in ItemBase.tags_for
    content_object = models.ForeignKey('Artist', null=False)

class Artist(models.Model):
    artist_id  = models.PositiveIntegerField(blank=True)
    image = models.TextField(blank=False, )
    name = models.CharField(max_length=100, blank=False, )
    popularity = models.FloatField(default=0.0)
    total_tracks  = models.PositiveIntegerField(blank=True)
    created = models.DateTimeField( auto_now_add=True, verbose_name='created' )
    modified = models.DateTimeField( auto_now=True, verbose_name='modified')
    genre = TaggableManager(through=TaggedGenre, verbose_name="Genre")

class Song(models.Model):
    song_id = models.PositiveIntegerField(blank=True)
    title = models.CharField( max_length=100, blank=False)
    duration = models.SmallIntegerField(blank=True)
    explicit_content = models.BooleanField(blank=True)
    popularity = models.FloatField(default=0.0)

class Timer(models.Model):
    created = models.DateTimeField( auto_now_add=True, verbose_name='created' )
    modified = models.DateTimeField( auto_now=True, verbose_name='modified')
