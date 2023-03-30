from django.urls import path
from .views import calc

urlpatterns = [
    path('cal/', calc, name='calc'),
]

