from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('control/',views.control),
    path('dashboard/',views.dashboard),
    path('about-us/',views.about),
]