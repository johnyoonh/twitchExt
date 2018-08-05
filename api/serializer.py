from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField

from api.models import Artist, Song


class ArtistSerializer(serializers.ModelSerializer):

    artist_id = serializers.CharField()
    image = serializers.CharField()
    name = serializers.CharField
    popularity = serializers.FloatField()
    total_tracks  = serializers.IntegerField()
    genre = TagListSerializerField()

    class Meta:
        model = Artist
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):

    artist_id = serializers.CharField()
    image = serializers.CharField()
    name = serializers.CharField
    popularity = serializers.FloatField()
    total_tracks  = serializers.IntegerField()
    genre = TagListSerializerField()

    song_id = serializers.CharField()
    title = serializers.CharField()
    duration = serializers.IntegerField()
    explicit_content = serializers.BooleanField()
    popularity = serializers.FloatField()

    class Meta:
        model = Song
        fields = '__all__'
