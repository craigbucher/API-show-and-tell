from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('raw', views.raw),
    path('small', views.small),
    path('thumb', views.thumb),
]