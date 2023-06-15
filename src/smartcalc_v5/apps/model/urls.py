from django.urls import path
from . import models
from . import views

urlpatterns = [
    path('', views.calc, name='calc'),
    path('process', models.process, name='process')
]