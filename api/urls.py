# Andrew - Adding Token Authentication
# from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

# Andrew - Adding Token Authentication
# from rest_framework.authtoken import views
from django.conf import settings

router = DefaultRouter()

urlpatterns = [
    url(r'^docs$', get_swagger_view(title='API Docs'), name='api_docs'),
    url(r'^', include(router.urls)),
    ]
