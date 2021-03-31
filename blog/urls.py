from .views import *
from django.urls import path

urlpatterns = [
    path('test/', test),
    path('accueil/', principal),
    path('infocommande/', infocommande),
    path('info/', info),
]

