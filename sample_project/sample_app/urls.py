from django.urls import path

from.views import *
urlpatterns=[
    path('index/',index),
    path('reg/',register),
    path('log/',log),
]