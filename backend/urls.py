from django.urls import path
from .views import urlInput

# http://0.0.0.0:8000/api/
urlpatterns = [
    path('', urlInput, name='urlInput'),
]
