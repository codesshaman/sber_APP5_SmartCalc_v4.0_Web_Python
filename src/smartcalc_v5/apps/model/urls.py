from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('calculate', views.calculate, name='calculate'),
    path('calc', views.calc, name='calc')
]