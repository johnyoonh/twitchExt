from rest_framework import viewsets

from api.models import Artist, Song, Genre
from api.serializer import ArtistSerializer, SongSerializer, GenreSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('?')
    serializer_class = ArtistSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('?')
    serializer_class = SongSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('?')
    serializer_class = GenreSerializer

