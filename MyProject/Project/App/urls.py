from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('2', views.a2, name='2')
]