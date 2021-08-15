
from .views import index
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index)
]

urlpatterns+=staticfiles_urlpatterns()