# Andrew - Adding Token Authentication
# from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

# Andrew - Adding Token Authentication
# from rest_framework.authtoken import views
from django.conf import settings

from api.views import ArtistViewSet, SongViewSet, GenreViewSet

router = DefaultRouter()

router.register(r'artists', ArtistViewSet, base_name='artists')
router.register(r'songs', SongViewSet, base_name='songs')
router.register(r'genres', GenreViewSet, base_name='genres')

urlpatterns = [
    url(r'^docs$', get_swagger_view(title='API Docs'), name='api_docs'),
    url(r'^', include(router.urls)),
    ]
